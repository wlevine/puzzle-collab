from flask import Flask, request, jsonify, session, redirect, url_for, send_from_directory
import sqlite3
import os
from functools import wraps

app = Flask(__name__, static_folder='public', static_url_path='')
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-this')

# Configuration
PASSWORD = os.environ.get('APP_PASSWORD', 'puzzle2025')  # Change this!
DATABASE = 'puzzle.db'

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
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
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        cursor.execute("INSERT OR IGNORE INTO pages (id, notes) VALUES (?, '')", (i,))
    
    conn.commit()
    conn.close()

def require_auth(f):
    """Authentication decorator"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

def require_api_auth(f):
    """API authentication decorator"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
@require_auth
def index():
    return send_from_directory('public', 'index.html')

@app.route('/login')
def login_page():
    return send_from_directory('public', 'login.html')

@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    if password == PASSWORD:
        session['authenticated'] = True
        return redirect('/')
    else:
        return redirect('/login?error=1')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# API Routes
@app.route('/api/pages')
@require_api_auth
def get_pages():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT p.id, p.notes,
               GROUP_CONCAT(s.name) as subjects
        FROM pages p
        LEFT JOIN page_subjects ps ON p.id = ps.page_id
        LEFT JOIN subjects s ON ps.subject_id = s.id
        GROUP BY p.id
        ORDER BY p.id
    ''')
    
    rows = cursor.fetchall()
    conn.close()
    
    pages = []
    for row in rows:
        pages.append({
            'id': row['id'],
            'notes': row['notes'],
            'subjects': row['subjects']
        })
    
    return jsonify(pages)

@app.route('/api/pages/<int:page_id>')
@require_api_auth
def get_page(page_id):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT p.id, p.notes,
               GROUP_CONCAT(s.name) as subjects
        FROM pages p
        LEFT JOIN page_subjects ps ON p.id = ps.page_id
        LEFT JOIN subjects s ON ps.subject_id = s.id
        WHERE p.id = ?
        GROUP BY p.id
    ''', (page_id,))
    
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        return jsonify({'error': 'Page not found'}), 404
    
    subjects = row['subjects'].split(',') if row['subjects'] else []
    
    return jsonify({
        'id': row['id'],
        'notes': row['notes'],
        'subjects': subjects
    })

@app.route('/api/pages/<int:page_id>', methods=['POST'])
@require_api_auth
def update_page(page_id):
    data = request.get_json()
    notes = data.get('notes', '')
    subjects = data.get('subjects', [])
    
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        # Update page notes
        cursor.execute('UPDATE pages SET notes = ? WHERE id = ?', (notes, page_id))
        
        # Clear existing subjects for this page
        cursor.execute('DELETE FROM page_subjects WHERE page_id = ?', (page_id,))
        
        # Add subjects
        for subject_name in subjects:
            subject_name = subject_name.strip()
            if subject_name:
                # Insert subject if it doesn't exist
                cursor.execute('INSERT OR IGNORE INTO subjects (name, notes) VALUES (?, "")', (subject_name,))
                
                # Get subject ID
                cursor.execute('SELECT id FROM subjects WHERE name = ?', (subject_name,))
                subject_row = cursor.fetchone()
                
                if subject_row:
                    # Link page to subject
                    cursor.execute('INSERT INTO page_subjects (page_id, subject_id) VALUES (?, ?)', 
                                 (page_id, subject_row['id']))
        
        conn.commit()
        conn.close()
        return jsonify({'success': True})
        
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'error': str(e)}), 500

@app.route('/api/subjects')
@require_api_auth
def get_subjects():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT s.id, s.name, s.notes,
               GROUP_CONCAT(ps.page_id) as pages
        FROM subjects s
        LEFT JOIN page_subjects ps ON s.id = ps.subject_id
        GROUP BY s.id, s.name, s.notes
        ORDER BY s.name
    ''')
    
    rows = cursor.fetchall()
    conn.close()
    
    subjects = []
    for row in rows:
        pages = []
        if row['pages']:
            pages = [int(p) for p in row['pages'].split(',')]
        
        subjects.append({
            'id': row['id'],
            'name': row['name'],
            'notes': row['notes'],
            'pages': pages
        })
    
    return jsonify(subjects)

@app.route('/api/subjects/<path:subject_name>')
@require_api_auth
def get_subject(subject_name):
    # URL decode the subject name
    import urllib.parse
    subject_name = urllib.parse.unquote(subject_name)
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT s.id, s.name, s.notes,
               GROUP_CONCAT(ps.page_id) as pages
        FROM subjects s
        LEFT JOIN page_subjects ps ON s.id = ps.subject_id
        WHERE s.name = ?
        GROUP BY s.id, s.name, s.notes
    ''', (subject_name,))
    
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        return jsonify({'error': 'Subject not found'}), 404
    
    pages = []
    if row['pages']:
        pages = [int(p) for p in row['pages'].split(',')]
    
    return jsonify({
        'id': row['id'],
        'name': row['name'],
        'notes': row['notes'],
        'pages': pages
    })

@app.route('/api/subjects/<path:subject_name>', methods=['POST'])
@require_api_auth
def update_subject(subject_name):
    # URL decode the subject name
    import urllib.parse
    subject_name = urllib.parse.unquote(subject_name)
    
    data = request.get_json()
    notes = data.get('notes', '')
    
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute('UPDATE subjects SET notes = ? WHERE name = ?', (notes, subject_name))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        conn.rollback()
        conn.close()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Initialize database on startup
    init_db()
    
    # Get port from environment variable (for deployment) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    print(f"Server starting on port {port}")
    print(f"Password: {PASSWORD}")
    
    # For production deployment
    app.run(host='0.0.0.0', port=port, debug=False)
