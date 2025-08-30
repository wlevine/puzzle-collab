# Common CSS and HTML structure
COMMON_CSS = '''
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f5f5f5;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    background: white;
    padding: 20px 0;
    border-bottom: 2px solid #eee;
    margin-bottom: 30px;
    border-radius: 10px;
}

header h1 {
    color: #667eea;
    text-align: center;
}

.nav-buttons {
    display: flex;
    gap: 10px;
    justify-content: center;
    margin-top: 15px;
    flex-wrap: wrap;
}

.nav-button {
    padding: 10px 20px;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    transition: background 0.3s;
}

.nav-button:hover {
    background: #5a67d8;
}

.main-content {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.flash-messages {
    margin-bottom: 20px;
}

.flash-message {
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    background: #d4e6f1;
    color: #2c3e50;
    border: 1px solid #667eea;
}

.page-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(60px, 1fr));
    gap: 10px;
    margin-top: 20px;
}

.page-link {
    padding: 15px 10px;
    background: #f7fafc;
    border: 2px solid #e2e8f0;
    border-radius: 5px;
    text-align: center;
    text-decoration: none;
    color: #4a5568;
    font-weight: bold;
    transition: all 0.3s;
}

.page-link:hover {
    background: #667eea;
    color: white;
    transform: translateY(-2px);
}

.page-link.has-content {
    background: #d4e6f1;
    border-color: #667eea;
}

.subjects-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    margin-top: 20px;
}

.subject-item {
    background: #f7fafc;
    border: 2px solid #e2e8f0;
    border-radius: 5px;
    padding: 15px;
    text-decoration: none;
    color: #4a5568;
    transition: all 0.3s;
}

.subject-item:hover {
    background: #667eea;
    color: white;
    transform: translateY(-2px);
}

.subject-name {
    font-weight: bold;
    margin-bottom: 5px;
}

.subject-pages {
    font-size: 0.9em;
    opacity: 0.7;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 10px;
    border: 2px solid #e2e8f0;
    border-radius: 5px;
    font-size: 16px;
}

.form-group textarea {
    min-height: 150px;
    resize: vertical;
}

.btn {
    padding: 10px 20px;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    margin-right: 10px;
    text-decoration: none;
    display: inline-block;
}

.btn:hover {
    background: #5a67d8;
}

.btn-secondary {
    background: #718096;
}

.btn-secondary:hover {
    background: #4a5568;
}

.cross-reference {
    color: #667eea;
    text-decoration: underline;
}

.cross-reference:hover {
    background: #667eea;
    color: white;
    padding: 2px 4px;
    border-radius: 3px;
}

.notes-preview {
    margin-top: 30px;
    padding: 20px;
    background: #f7fafc;
    border-radius: 5px;
}
'''

COMMON_HEADER = '''
<div class="container">
    <header>
        <h1>🧩 Puzzle Solver</h1>
        <div class="nav-buttons">
            <a href="{{ url_for('index') }}" class="nav-button">All Pages</a>
            <a href="{{ url_for('subjects_list') }}" class="nav-button">All Subjects</a>
            <a href="{{ url_for('logout') }}" class="nav-button">Logout</a>
        </div>
    </header>
    
    <main class="main-content">
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="flash-messages">
                    {% for message in messages %}
                        <div class="flash-message">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
'''

COMMON_FOOTER = '''
    </main>
</div>
</body>
</html>
'''

# HTML Templates
LOGIN_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Solver - Login</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .login-box {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            text-align: center;
            min-width: 300px;
        }
        h1 { margin-bottom: 30px; color: #333; }
        .error {
            color: #e53e3e;
            margin-bottom: 15px;
            padding: 10px;
            background: #fed7d7;
            border-radius: 5px;
        }
        input {
            width: 100%;
            padding: 15px;
            margin-bottom: 20px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 15px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover { background: #5a67d8; }
    </style>
</head>
<body>
    <div class="login-box">
        <h1>🧩 Puzzle Solver</h1>
        {% if error %}
            <div class="error">Incorrect password. Please try again.</div>
        {% endif %}
        <form method="POST">
            <input type="password" name="password" placeholder="Enter password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>'''

PAGES_LIST_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Solver - All Pages</title>
    <style>''' + COMMON_CSS + '''</style>
</head>
<body>
''' + COMMON_HEADER + '''
        <h2>Pages (1-100)</h2>
        <div class="page-grid">
            {% for page in pages %}
                <a href="{{ url_for('page_detail', page_id=page.id) }}" 
                   class="page-link {% if page.notes or page.subjects %}has-content{% endif %}">
                    {{ page.id }}
                </a>
            {% endfor %}
        </div>
''' + COMMON_FOOTER

SUBJECTS_LIST_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Solver - All Subjects</title>
    <style>''' + COMMON_CSS + '''</style>
</head>
<body>
''' + COMMON_HEADER + '''
        <h2>All Subjects</h2>
        <div class="subjects-list">
            {% for subject in subjects %}
                <a href="{{ url_for('subject_page', subject_id=subject.id) }}" class="subject-item">
                    <div class="subject-name">{{ subject.name }}</div>
                    <div class="subject-pages">
                        {% if subject.pages %}
                            Pages: {{ subject.pages.replace(',', ', ') }}
                        {% else %}
                            No pages yet
                        {% endif %}
                    </div>
                </a>
            {% endfor %}
        </div>
''' + COMMON_FOOTER

PAGE_DETAIL_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Solver - Page Details</title>
    <style>''' + COMMON_CSS + '''</style>
</head>
<body>
''' + COMMON_HEADER + '''
        <h2>Page {{ page.id }}</h2>

        <form method="POST">
            <div class="form-group">
                <label for="subjects">Subjects (comma-separated):</label>
                <input type="text" id="subjects" name="subjects" value="{{ ', '.join(subjects_list) }}" 
                       placeholder="e.g. Alexander, Paris, Murder">
                <small>Enter character names, locations, events, etc.</small>
            </div>
            
            <div class="form-group">
                <label for="notes">Notes:</label>
                <textarea id="notes" name="notes" placeholder="Add your notes about this page here...">{{ page.notes }}</textarea>
                <small>You can reference other subjects like: [[Alexander]] or pages like: {{ '{{Page 25}}' }}</small>
            </div>
            
            <button type="submit" class="btn">Save</button>
            <a href="{{ url_for('index') }}" class="btn btn-secondary">Back to Pages</a>
        </form>

        {% if notes_html %}
            <div class="notes-preview">
                <h3>Notes Preview:</h3>
                <div>{{ notes_html|safe }}</div>
            </div>
        {% endif %}
''' + COMMON_FOOTER

SUBJECT_DETAIL_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Solver - Subject Details</title>
    <style>''' + COMMON_CSS + '''</style>
</head>
<body>
''' + COMMON_HEADER + '''
        <h2>Subject: {{ subject.name }}</h2>

        <div style="margin-bottom: 20px; padding: 15px; background: #e6fffa; border-radius: 5px;">
            <strong>Appears on:</strong>
            {% if page_ids %}
                {% for page_id in page_ids %}
                    <a href="{{ url_for('page_detail', page_id=page_id) }}" class="cross-reference">Page {{ page_id }}</a>{% if not loop.last %}, {% endif %}
                {% endfor %}
            {% else %}
                Not mentioned on any pages yet
            {% endif %}
        </div>

        <form method="POST">
            <div class="form-group">
                <label for="notes">Notes about {{ subject.name }}:</label>
                <textarea id="notes" name="notes" placeholder="Add your notes about this subject here...">{{ subject.notes }}</textarea>
                <small>You can reference other subjects like: [[Paris]] or pages like: {{ '{{Page 25}}' }}</small>
            </div>
            
            <button type="submit" class="btn">Save</button>
            <a href="{{ url_for('subjects_list') }}" class="btn btn-secondary">Back to Subjects</a>
        </form>

        {% if notes_html %}
            <div class="notes-preview">
                <h3>Notes Preview:</h3>
                <div>{{ notes_html|safe }}</div>
            </div>
        {% endif %}
''' + COMMON_FOOTER
