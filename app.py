from flask import Flask, request, render_template_string, redirect, url_for, session, flash
import psycopg2
import psycopg2.extras
import os
from functools import wraps

from templates import LOGIN_TEMPLATE, PAGES_LIST_TEMPLATE, SUBJECTS_LIST_TEMPLATE, SUBJECT_DETAIL_TEMPLATE, PAGE_DETAIL_TEMPLATE

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-this')

# Configuration
PASSWORD = os.environ.get('APP_PASSWORD', 'puzzle2025')
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://puzzle_user:puzzle_pass@localhost:5432/puzzle_db')

def get_db():
    """Get database connection"""
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def init_db():
    """Initialize the database with tables and initial data"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS pages (
        id INTEGER PRIMARY KEY,
        notes TEXT DEFAULT ''
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE,
        notes TEXT DEFAULT ''
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS page_subjects (
        page_id INTEGER,
        subject_id INTEGER,
        PRIMARY KEY (page_id, subject_id),
        FOREIGN KEY (page_id) REFERENCES pages (id),
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
    )''')
    
    # Insert pages 1-100 if they don't exist
    for i in range(1, 101):
        cursor.execute("INSERT INTO pages (id, notes) VALUES (%s, '') ON CONFLICT (id) DO NOTHING", (i,))
    
    conn.commit()
    conn.close()

def require_auth(f):
    """Authentication decorator"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated_function

def process_notes_for_display(notes):
    """Convert [[Subject]] and {{Page X}} to HTML links"""
    if not notes:
        return ''
    
    import re
    import html
    
    # Escape HTML first
    processed = html.escape(notes)
    
    # Convert [[Subject]] to links - need to get subject ID from DB
    def replace_subject_link(match):
        subject_name = match.group(1)
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM subjects WHERE name = %s', (subject_name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return f'<a href="{url_for("subject_page", subject_id=row[0])}" class="cross-reference">{html.escape(subject_name)}</a>'
        return match.group(0)  # Return original if subject not found
    
    processed = re.sub(r'\[\[([^\]]+)\]\]', replace_subject_link, processed)
    
    # Convert {{Page X}} to links
    processed = re.sub(r'\{\{Page (\d+)\}\}', 
                      lambda m: f'<a href="{url_for("page_detail", page_id=int(m.group(1)))}" class="cross-reference">Page {m.group(1)}</a>', 
                      processed)
    
    # Convert line breaks to HTML
    processed = processed.replace('\n', '<br>')
    
    return processed


# Routes
@app.route('/login')
def login_page():
    error = request.args.get('error')
    return render_template_string(LOGIN_TEMPLATE, error=error)

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    if password == PASSWORD:
        session['authenticated'] = True
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login_page', error=1))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))

@app.route('/')
@require_auth
def index():
    """Homepage with all pages grid"""
    conn = get_db()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cursor.execute('''
        SELECT p.id, p.notes,
               STRING_AGG(s.name, ',') as subjects
        FROM pages p
        LEFT JOIN page_subjects ps ON p.id = ps.page_id
        LEFT JOIN subjects s ON ps.subject_id = s.id
        GROUP BY p.id, p.notes
        ORDER BY p.id
    ''')
    
    pages = cursor.fetchall()
    conn.close()
    
    return render_template_string(PAGES_LIST_TEMPLATE, pages=pages)

@app.route('/pages/<int:page_id>')
@require_auth
def page_detail(page_id):
    """Individual page view/edit"""
    conn = get_db()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cursor.execute('''
        SELECT p.id, p.notes,
               STRING_AGG(s.name, ',') as subjects
        FROM pages p
        LEFT JOIN page_subjects ps ON p.id = ps.page_id
        LEFT JOIN subjects s ON ps.subject_id = s.id
        WHERE p.id = %s
        GROUP BY p.id, p.notes
    ''', (page_id,))
    
    page = cursor.fetchone()
    conn.close()
    
    if not page:
        flash('Page not found')
        return redirect(url_for('index'))
    
    subjects_list = page['subjects'].split(',') if page['subjects'] else []
    notes_html = process_notes_for_display(page['notes'])
    
    return render_template_string(PAGE_DETAIL_TEMPLATE, 
                                page=page, 
                                subjects_list=subjects_list,
                                notes_html=notes_html)

@app.route('/pages/<int:page_id>', methods=['POST'])
@require_auth
def update_page(page_id):
    """Update page data"""
    notes = request.form.get('notes', '')
    subjects_str = request.form.get('subjects', '')
    subjects = [s.strip() for s in subjects_str.split(',') if s.strip()]
    
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        # Update page notes
        cursor.execute('UPDATE pages SET notes = %s WHERE id = %s', (notes, page_id))
        
        # Clear existing subjects for this page
        cursor.execute('DELETE FROM page_subjects WHERE page_id = %s', (page_id,))
        
        # Add subjects
        for subject_name in subjects:
            # Insert subject if it doesn't exist
            cursor.execute('INSERT INTO subjects (name, notes) VALUES (%s, \'\') ON CONFLICT (name) DO NOTHING', (subject_name,))
            
            # Get subject ID
            cursor.execute('SELECT id FROM subjects WHERE name = %s', (subject_name,))
            subject_row = cursor.fetchone()
            
            if subject_row:
                # Link page to subject
                cursor.execute('INSERT INTO page_subjects (page_id, subject_id) VALUES (%s, %s)', 
                             (page_id, subject_row[0]))
        
        conn.commit()
        flash('Page updated successfully!')
        
    except Exception as e:
        conn.rollback()
        flash(f'Error updating page: {str(e)}')
    
    conn.close()
    return redirect(url_for('page_detail', page_id=page_id))

@app.route('/subjects')
@require_auth
def subjects_list():
    """List all subjects (excluding empty ones with no notes)"""
    conn = get_db()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cursor.execute('''
        SELECT s.id, s.name, s.notes,
               STRING_AGG(ps.page_id::text, ',') as pages,
               COUNT(ps.page_id) as page_count
        FROM subjects s
        LEFT JOIN page_subjects ps ON s.id = ps.subject_id
        GROUP BY s.id, s.name, s.notes
        HAVING COUNT(ps.page_id) > 0 OR (s.notes IS NOT NULL AND s.notes != '')
        ORDER BY s.name
    ''')
    
    subjects = cursor.fetchall()
    conn.close()
    
    return render_template_string(SUBJECTS_LIST_TEMPLATE, subjects=subjects)

@app.route('/subjects/<int:subject_id>')
@require_auth
def subject_page(subject_id):
    """Individual subject view/edit"""
    conn = get_db()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cursor.execute('''
        SELECT s.id, s.name, s.notes,
               STRING_AGG(ps.page_id::text, ',') as pages
        FROM subjects s
        LEFT JOIN page_subjects ps ON s.id = ps.subject_id
        WHERE s.id = %s
        GROUP BY s.id, s.name, s.notes
    ''', (subject_id,))
    
    subject = cursor.fetchone()
    conn.close()
    
    if not subject:
        flash('Subject not found')
        return redirect(url_for('subjects_list'))
    
    page_ids = []
    if subject['pages']:
        page_ids = [int(p) for p in subject['pages'].split(',')]
    
    notes_html = process_notes_for_display(subject['notes'])
    
    return render_template_string(SUBJECT_DETAIL_TEMPLATE, 
                                subject=subject, 
                                page_ids=page_ids,
                                notes_html=notes_html)

@app.route('/subjects/<int:subject_id>', methods=['POST'])
@require_auth
def update_subject(subject_id):
    """Update subject notes"""
    notes = request.form.get('notes', '')
    
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute('UPDATE subjects SET notes = %s WHERE id = %s', (notes, subject_id))
        conn.commit()
        flash('Subject updated successfully!')
    except Exception as e:
        conn.rollback()
        flash(f'Error updating subject: {str(e)}')
    
    conn.close()
    return redirect(url_for('subject_page', subject_id=subject_id))

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))
    print(f"Server starting on port {port}")
    print(f"Database: {DATABASE_URL}")
    app.run(host='0.0.0.0', port=port, debug=False)
