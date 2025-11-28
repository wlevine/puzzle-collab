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
            {% for user in workspace_users %}
                <a href="{{ url_for('user_workspace', username=user) }}" class="nav-button">{{ user }}</a>
            {% endfor %}
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

WORKSPACE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Solver - {{ username }}'s Workspace</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #edf2f7;
            overflow: hidden;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }

        .navbar {
            background: white;
            padding: 0.5rem 1.5rem;
            border-bottom: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            display: flex;
            align-items: center;
            gap: 1.5rem;
            font-size: 0.9rem;
            flex-wrap: wrap;
        }

        .navbar .title {
            color: #667eea;
            font-weight: 600;
            font-size: 1rem;
        }

        .navbar a {
            color: #4a5568;
            text-decoration: none;
            padding: 0.25rem 0.5rem;
            border-radius: 3px;
            transition: background 0.2s;
        }

        .navbar a:hover {
            background: #f7fafc;
            color: #667eea;
        }

        .navbar .divider {
            color: #cbd5e0;
        }

        .workspace-container {
            flex: 1;
            position: relative;
            overflow: hidden;
            background: #edf2f7;
            cursor: grab;
        }

        .workspace-container.panning {
            cursor: grabbing;
        }

        .workspace {
            position: absolute;
            width: 100000px;
            height: 100000px;
            transform-origin: 0 0;
            left: -50000px;
            top: -50000px;
        }

        .workspace.creating {
            cursor: crosshair !important;
        }

        .page-box {
            position: absolute;
            width: 80px;
            height: 50px;
            background: white;
            border: 2px solid #cbd5e0;
            border-radius: 6px;
            display: flex;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: box-shadow 0.2s;
            user-select: none;
        }

        .page-box:hover {
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }

        .page-box.dragging {
            opacity: 0.7;
            cursor: grabbing;
            z-index: 1000;
        }

        .page-drag-area {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: grab;
            font-size: 1.1rem;
            font-weight: 600;
            color: #2d3748;
            border-right: 1px dashed #cbd5e0;
        }

        .page-link-area {
            width: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            background: #f7fafc;
            border-radius: 0 4px 4px 0;
            transition: background 0.2s;
        }

        .page-link-area:hover {
            background: #667eea;
        }

        .page-link-area:hover::after {
            filter: brightness(0) invert(1);
        }

        .page-link-area::after {
            content: '🔗';
            font-size: 0.9rem;
        }

        .zoom-indicator {
            position: absolute;
            bottom: 1rem;
            right: 1rem;
            background: white;
            padding: 0.4rem 0.8rem;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            font-size: 0.8rem;
            color: #718096;
            pointer-events: none;
        }

        .add-textbox-btn {
            padding: 0.4rem 0.8rem;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: background 0.2s;
        }

        .add-textbox-btn:hover {
            background: #5568d3;
        }

        .add-textbox-btn.active {
            background: #48bb78;
        }

        .text-box {
            position: absolute;
            background: rgba(255, 255, 255, 0.05);
            border: 2px dashed #cbd5e0;
            padding: 8px;
            font-size: 1.1rem;
            font-weight: 600;
            color: #2d3748;
            font-family: inherit;
            resize: none;
            overflow: hidden;
            word-wrap: break-word;
            white-space: pre-wrap;
            user-select: none;
            cursor: default;
            z-index: 1;
        }

        .text-box:hover {
            border-color: #a0aec0;
        }

        .text-box.active {
            border: 3px solid #667eea;
            background: rgba(102, 126, 234, 0.08);
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
            user-select: text;
        }

        .text-box.moving {
            cursor: move !important;
        }

        .text-box.active .text-box-textarea {
            cursor: text !important;
        }

        .text-box-textarea {
            width: 100%;
            background: transparent;
            border: none;
            padding: 0;
            font-size: inherit;
            font-weight: inherit;
            color: inherit;
            font-family: inherit;
            resize: none;
            overflow: hidden;
            outline: none;
        }

        /* Border hit targets - these create generous clickable areas */
        .border-top, .border-left, .border-bottom, .border-right {
            position: absolute;
            background: transparent;
            z-index: 10;
        }

        /* Top border - for moving */
        .border-top {
            top: -8px;
            left: -8px;
            right: -8px;
            height: 16px;
            cursor: move !important;
        }

        /* Left border - for moving */
        .border-left {
            top: -8px;
            left: -8px;
            bottom: -8px;
            width: 16px;
            cursor: move !important;
        }

        /* Bottom border - for moving */
        .border-bottom {
            bottom: -8px;
            left: -8px;
            right: -8px;
            height: 16px;
            cursor: move !important;
        }

        /* Right border - for resizing */
        .border-right {
            top: -8px;
            right: -8px;
            bottom: -8px;
            width: 16px;
            cursor: ew-resize !important;
        }

        /* Visual feedback on hover */
        .border-right:hover {
            background: rgba(102, 126, 234, 0.3);
        }

        .hint {
            position: absolute;
            top: 1rem;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.95);
            padding: 0.5rem 1rem;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            font-size: 0.85rem;
            color: #4a5568;
            pointer-events: none;
            opacity: 0;
            animation: fadeInOut 4s ease-in-out;
        }

        @keyframes fadeInOut {
            0%, 100% { opacity: 0; }
            10%, 90% { opacity: 1; }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <span class="title">Workspace: {{ username }}</span>
        <span class="divider">|</span>
        <button class="add-textbox-btn" id="addTextBoxBtn">+ Text Box</button>
        <span class="divider">|</span>
        <a href="{{ url_for('index') }}">All Pages</a>
        <a href="{{ url_for('subjects_list') }}">All Subjects</a>
        <span class="divider">|</span>
        {% for user in workspace_users %}
            <a href="{{ url_for('user_workspace', username=user) }}">{{ user }}</a>
        {% endfor %}
        <span class="divider">|</span>
        <a href="{{ url_for('logout') }}">Logout</a>
    </nav>

    <div class="workspace-container">
        <div class="workspace" id="workspace"></div>
        <div class="zoom-indicator" id="zoomIndicator">100%</div>
        <div class="hint" id="hint">💡 Drag background to pan | Scroll to zoom | Drag boxes to arrange</div>
    </div>

    <script>
        // Configuration
        const TOTAL_PAGES = 100;
        const BOX_WIDTH = 80;
        const BOX_HEIGHT = 50;
        const SPACING_X = 140;
        const SPACING_Y = 100;
        const MARGIN_X = 100;
        const MARGIN_Y = 80;
        const USERNAME = {{ username|tojson }};
        const SAVED_POSITIONS = {{ positions|tojson }};
        const VIEW_STATE = {{ view_state|tojson }};
        const TEXT_BOXES = {{ text_boxes|tojson }};

        // State - load from saved view state, or use sensible defaults
        let scale = VIEW_STATE.zoom || 1;
        // If no saved view state, center on the initial grid
        // The workspace is offset at (-50000, -50000), and boxes start around (100, 80)
        // So we need to pan by ~50000 to bring them into view, centered nicely
        const defaultPanX = 50000 - 200; // Offset to roughly center the grid
        const defaultPanY = 50000 - 200;
        let panX = (VIEW_STATE.pan_x !== 0 || VIEW_STATE.pan_y !== 0 || VIEW_STATE.zoom !== 1) ? VIEW_STATE.pan_x : defaultPanX;
        let panY = (VIEW_STATE.pan_x !== 0 || VIEW_STATE.pan_y !== 0 || VIEW_STATE.zoom !== 1) ? VIEW_STATE.pan_y : defaultPanY;
        let isPanning = false;
        let panStartX = 0;
        let panStartY = 0;
        let draggedElement = null;
        let dragOffsetX = 0;
        let dragOffsetY = 0;

        const workspace = document.getElementById('workspace');
        const zoomIndicator = document.getElementById('zoomIndicator');

        // Calculate optimal rectangular layout based on screen size
        function calculateLayout() {
            const container = document.querySelector('.workspace-container');
            const viewWidth = container.clientWidth;
            const viewHeight = container.clientHeight;

            const availableWidth = viewWidth - 2 * MARGIN_X;
            const boxesPerRow = Math.max(8, Math.min(15, Math.floor(availableWidth / SPACING_X)));
            const numRows = Math.ceil(TOTAL_PAGES / boxesPerRow);

            return { boxesPerRow, numRows };
        }

        // Save position to database
        async function savePosition(pageId, x, y) {
            try {
                const response = await fetch(`/user/${USERNAME}/update-position`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        page_id: pageId,
                        x: x,
                        y: y
                    })
                });

                const data = await response.json();
                if (!data.success) {
                    console.error('Failed to save position:', data.error);
                }
            } catch (error) {
                console.error('Error saving position:', error);
            }
        }

        // Debounced view state save
        let viewStateSaveTimeout = null;
        async function saveViewState() {
            try {
                const response = await fetch(`/user/${USERNAME}/update-view`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        pan_x: panX,
                        pan_y: panY,
                        zoom: scale
                    })
                });

                const data = await response.json();
                if (!data.success) {
                    console.error('Failed to save view state:', data.error);
                }
            } catch (error) {
                console.error('Error saving view state:', error);
            }
        }

        function debouncedSaveViewState() {
            if (viewStateSaveTimeout) {
                clearTimeout(viewStateSaveTimeout);
            }
            viewStateSaveTimeout = setTimeout(saveViewState, 500);
        }

        // Create page boxes
        function createPageBoxes() {
            workspace.innerHTML = '';
            const layout = calculateLayout();

            for (let i = 1; i <= TOTAL_PAGES; i++) {
                const box = document.createElement('div');
                box.className = 'page-box';
                box.dataset.page = i;

                // Calculate default position in rectangular layout
                const row = Math.floor((i - 1) / layout.boxesPerRow);
                const col = (i - 1) % layout.boxesPerRow;
                const defaultX = MARGIN_X + col * SPACING_X;
                const defaultY = MARGIN_Y + row * SPACING_Y;

                // Use saved position or default
                const pos = SAVED_POSITIONS[i] || { x: defaultX, y: defaultY };
                box.style.left = pos.x + 'px';
                box.style.top = pos.y + 'px';

                // Drag area (left side)
                const dragArea = document.createElement('div');
                dragArea.className = 'page-drag-area';
                dragArea.textContent = i;
                dragArea.addEventListener('mousedown', startDrag);

                // Link area (right side) - use real <a> tag
                const linkArea = document.createElement('a');
                linkArea.className = 'page-link-area';
                linkArea.href = `/pages/${i}`;
                linkArea.target = '_blank';
                linkArea.addEventListener('mousedown', (e) => {
                    // Prevent drag from starting when clicking the link
                    e.stopPropagation();
                });

                box.appendChild(dragArea);
                box.appendChild(linkArea);
                workspace.appendChild(box);
            }
        }

        // Drag functionality for page boxes
        function startDrag(e) {
            if (e.button !== 0) return;
            e.preventDefault();
            e.stopPropagation();

            draggedElement = e.target.closest('.page-box');
            draggedElement.classList.add('dragging');

            const rect = draggedElement.getBoundingClientRect();
            const workspaceRect = workspace.getBoundingClientRect();

            dragOffsetX = (e.clientX - rect.left) / scale;
            dragOffsetY = (e.clientY - rect.top) / scale;

            document.addEventListener('mousemove', doDrag);
            document.addEventListener('mouseup', stopDrag);
        }

        function doDrag(e) {
            if (!draggedElement) return;

            const workspaceRect = workspace.getBoundingClientRect();
            const x = (e.clientX - workspaceRect.left) / scale - dragOffsetX;
            const y = (e.clientY - workspaceRect.top) / scale - dragOffsetY;

            draggedElement.style.left = x + 'px';
            draggedElement.style.top = y + 'px';
        }

        function stopDrag(e) {
            if (draggedElement) {
                draggedElement.classList.remove('dragging');

                // Save position to database
                const pageId = parseInt(draggedElement.dataset.page);
                const x = parseFloat(draggedElement.style.left);
                const y = parseFloat(draggedElement.style.top);
                savePosition(pageId, x, y);

                draggedElement = null;
            }
            document.removeEventListener('mousemove', doDrag);
            document.removeEventListener('mouseup', stopDrag);
        }

        // Pan functionality - handle at container level so you can pan anywhere
        document.querySelector('.workspace-container').addEventListener('mousedown', (e) => {
            if (e.button !== 0) return;
            // Only start panning if clicking on workspace or container background (not on page boxes)
            if (e.target === workspace ||
                e.target.classList.contains('workspace') ||
                e.target.classList.contains('workspace-container')) {
                isPanning = true;
                panStartX = e.clientX - panX;
                panStartY = e.clientY - panY;
                document.querySelector('.workspace-container').classList.add('panning');
            }
        });

        document.addEventListener('mousemove', (e) => {
            if (isPanning) {
                panX = e.clientX - panStartX;
                panY = e.clientY - panStartY;
                updateTransform();
            }
        });

        document.addEventListener('mouseup', () => {
            if (isPanning) {
                isPanning = false;
                document.querySelector('.workspace-container').classList.remove('panning');
                // Save view state after panning
                debouncedSaveViewState();
            }
        });

        // Zoom functionality
        const WORKSPACE_OFFSET_X = -50000;
        const WORKSPACE_OFFSET_Y = -50000;

        document.querySelector('.workspace-container').addEventListener('wheel', (e) => {
            e.preventDefault();

            const delta = e.deltaY > 0 ? 0.9 : 1.1;
            const newScale = Math.max(0.1, Math.min(3, scale * delta));

            // Zoom toward mouse position (relative to viewport/container)
            const container = document.querySelector('.workspace-container');
            const containerRect = container.getBoundingClientRect();
            const mouseX = e.clientX - containerRect.left;
            const mouseY = e.clientY - containerRect.top;

            // Calculate workspace coordinate under mouse
            // viewport = WORKSPACE_OFFSET + panX + workspace_x * scale
            // workspace_x = (viewport - WORKSPACE_OFFSET - panX) / scale
            const workspaceX = (mouseX - WORKSPACE_OFFSET_X - panX) / scale;
            const workspaceY = (mouseY - WORKSPACE_OFFSET_Y - panY) / scale;

            // Adjust pan so that the same workspace point stays under the mouse
            // mouseX = WORKSPACE_OFFSET + newPanX + workspaceX * newScale
            panX = mouseX - WORKSPACE_OFFSET_X - workspaceX * newScale;
            panY = mouseY - WORKSPACE_OFFSET_Y - workspaceY * newScale;

            scale = newScale;
            updateTransform();

            // Save view state after zooming
            debouncedSaveViewState();
        }, { passive: false });

        function updateTransform() {
            workspace.style.transform = `translate(${panX}px, ${panY}px) scale(${scale})`;
            zoomIndicator.textContent = `${Math.round(scale * 100)}%`;
        }

        // ===================
        // TEXT BOX FUNCTIONALITY
        // ===================

        let isCreatingTextBox = false;
        let activeTextBox = null;
        let textBoxes = new Map();
        let resizingTextBox = null;
        let resizeStartX = 0;
        let resizeStartWidth = 0;
        let movingTextBox = null;
        let moveStartX = 0;
        let moveStartY = 0;

        // Create text box element
        function createTextBoxElement(id, x, y, width, text) {
            const box = document.createElement('div');
            box.className = 'text-box';
            box.dataset.id = id;
            box.style.left = x + 'px';
            box.style.top = y + 'px';
            box.style.width = width + 'px';

            const textarea = document.createElement('textarea');
            textarea.className = 'text-box-textarea';
            textarea.value = text;
            textarea.readOnly = true;

            // Create four border hit targets
            const borderTop = document.createElement('div');
            borderTop.className = 'border-top';

            const borderLeft = document.createElement('div');
            borderLeft.className = 'border-left';

            const borderBottom = document.createElement('div');
            borderBottom.className = 'border-bottom';

            const borderRight = document.createElement('div');
            borderRight.className = 'border-right';

            box.appendChild(textarea);
            box.appendChild(borderTop);
            box.appendChild(borderLeft);
            box.appendChild(borderBottom);
            box.appendChild(borderRight);

            // Right border = resize
            borderRight.addEventListener('mousedown', (e) => {
                e.stopPropagation();
                e.preventDefault();
                startResize(e, box);
            });

            // Top, left, bottom borders = move
            [borderTop, borderLeft, borderBottom].forEach(border => {
                border.addEventListener('mousedown', (e) => {
                    e.stopPropagation();
                    e.preventDefault();
                    if (!box.classList.contains('active')) {
                        activateTextBox(box);
                    }
                    startMove(e, box);
                });
            });

            // Click on box or textarea to activate (not on borders)
            box.addEventListener('mousedown', (e) => {
                // If click was on a border, let the border handle it
                if (e.target.classList.contains('border-top') ||
                    e.target.classList.contains('border-left') ||
                    e.target.classList.contains('border-bottom') ||
                    e.target.classList.contains('border-right')) {
                    return;
                }

                // Click on textarea or box body
                if (!box.classList.contains('active')) {
                    e.stopPropagation();
                    activateTextBox(box);
                    // Start moving if not clicking on textarea
                    if (e.target !== textarea) {
                        startMove(e, box);
                    }
                }
                // If already active and clicking textarea, allow text editing
            });

            // Auto-resize height as text changes
            textarea.addEventListener('input', () => {
                adjustTextBoxHeight(box);
                debouncedSaveTextBox(box);
            });

            workspace.appendChild(box);
            textBoxes.set(id, box);
            adjustTextBoxHeight(box);
            return box;
        }

        // Adjust text box height to fit content
        function adjustTextBoxHeight(box) {
            const textarea = box.querySelector('textarea');
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        }

        // Activate text box for editing
        function activateTextBox(box) {
            // Deactivate any currently active box
            if (activeTextBox && activeTextBox !== box) {
                deactivateTextBox(activeTextBox);
            }

            box.classList.add('active');
            const textarea = box.querySelector('textarea');
            textarea.readOnly = false;
            textarea.focus();
            activeTextBox = box;
        }

        // Deactivate text box
        function deactivateTextBox(box) {
            box.classList.remove('active');
            const textarea = box.querySelector('textarea');
            textarea.readOnly = true;
            activeTextBox = null;
        }

        // Start text box creation mode
        document.getElementById('addTextBoxBtn').addEventListener('click', () => {
            if (isCreatingTextBox) {
                exitCreatingMode();
            } else {
                enterCreatingMode();
            }
        });

        function enterCreatingMode() {
            isCreatingTextBox = true;
            document.getElementById('addTextBoxBtn').classList.add('active');
            document.querySelector('.workspace-container').style.cursor = 'crosshair';
            workspace.classList.add('creating');
        }

        function exitCreatingMode() {
            isCreatingTextBox = false;
            document.getElementById('addTextBoxBtn').classList.remove('active');
            document.querySelector('.workspace-container').style.cursor = '';
            workspace.classList.remove('creating');
        }

        // Handle click to place text box
        document.querySelector('.workspace-container').addEventListener('click', (e) => {
            if (isCreatingTextBox && (e.target.classList.contains('workspace') ||
                e.target.classList.contains('workspace-container'))) {
                const containerRect = document.querySelector('.workspace-container').getBoundingClientRect();
                const clickX = e.clientX - containerRect.left;
                const clickY = e.clientY - containerRect.top;

                // Convert to workspace coordinates
                const workspaceX = (clickX - WORKSPACE_OFFSET_X - panX) / scale;
                const workspaceY = (clickY - WORKSPACE_OFFSET_Y - panY) / scale;

                createNewTextBox(workspaceX, workspaceY);
                exitCreatingMode();
            }
        });

        // Create new text box via API
        async function createNewTextBox(x, y) {
            try {
                const response = await fetch(`/user/${USERNAME}/text-box`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        x: Math.round(x),
                        y: Math.round(y),
                        width: 200,
                        text: ''
                    })
                });

                const data = await response.json();
                if (data.success) {
                    const box = createTextBoxElement(data.id, x, y, 200, '');
                    activateTextBox(box);
                } else {
                    console.error('Failed to create text box:', data.error);
                }
            } catch (error) {
                console.error('Error creating text box:', error);
            }
        }

        // Resize functionality
        function startResize(e, box) {
            e.preventDefault();
            e.stopPropagation();
            resizingTextBox = box;
            resizeStartX = e.clientX;
            resizeStartWidth = parseInt(box.style.width);

            document.addEventListener('mousemove', doResize);
            document.addEventListener('mouseup', stopResize);
        }

        function doResize(e) {
            if (!resizingTextBox) return;

            const deltaX = (e.clientX - resizeStartX) / scale;
            const newWidth = Math.max(100, resizeStartWidth + deltaX);
            resizingTextBox.style.width = newWidth + 'px';
            adjustTextBoxHeight(resizingTextBox);
        }

        function stopResize() {
            if (resizingTextBox) {
                debouncedSaveTextBox(resizingTextBox);
                resizingTextBox = null;
            }
            document.removeEventListener('mousemove', doResize);
            document.removeEventListener('mouseup', stopResize);
        }

        // Move functionality
        function startMove(e, box) {
            if (e.target.tagName === 'TEXTAREA') return; // Don't move when editing text

            e.preventDefault();
            e.stopPropagation();
            movingTextBox = box;
            moveStartX = e.clientX;
            moveStartY = e.clientY;
            box.classList.add('moving');

            document.addEventListener('mousemove', doMove);
            document.addEventListener('mouseup', stopMove);
        }

        function doMove(e) {
            if (!movingTextBox) return;

            const deltaX = (e.clientX - moveStartX) / scale;
            const deltaY = (e.clientY - moveStartY) / scale;

            const currentX = parseFloat(movingTextBox.style.left);
            const currentY = parseFloat(movingTextBox.style.top);

            movingTextBox.style.left = (currentX + deltaX) + 'px';
            movingTextBox.style.top = (currentY + deltaY) + 'px';

            moveStartX = e.clientX;
            moveStartY = e.clientY;
        }

        function stopMove() {
            if (movingTextBox) {
                movingTextBox.classList.remove('moving');
                debouncedSaveTextBox(movingTextBox);
                movingTextBox = null;
            }
            document.removeEventListener('mousemove', doMove);
            document.removeEventListener('mouseup', stopMove);
        }

        // Save text box to database (debounced)
        let textBoxSaveTimeouts = new Map();

        function debouncedSaveTextBox(box) {
            const id = box.dataset.id;
            if (textBoxSaveTimeouts.has(id)) {
                clearTimeout(textBoxSaveTimeouts.get(id));
            }
            textBoxSaveTimeouts.set(id, setTimeout(() => saveTextBox(box), 500));
        }

        async function saveTextBox(box) {
            const id = box.dataset.id;
            const textarea = box.querySelector('textarea');

            try {
                const response = await fetch(`/user/${USERNAME}/text-box/${id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        x: Math.round(parseFloat(box.style.left)),
                        y: Math.round(parseFloat(box.style.top)),
                        width: Math.round(parseFloat(box.style.width)),
                        text: textarea.value
                    })
                });

                const data = await response.json();
                if (!data.success) {
                    console.error('Failed to save text box:', data.error);
                }
            } catch (error) {
                console.error('Error saving text box:', error);
            }
        }

        // Delete text box
        async function deleteTextBox(box) {
            const id = box.dataset.id;

            try {
                const response = await fetch(`/user/${USERNAME}/text-box/${id}`, {
                    method: 'DELETE'
                });

                const data = await response.json();
                if (data.success) {
                    box.remove();
                    textBoxes.delete(parseInt(id));
                    if (activeTextBox === box) {
                        activeTextBox = null;
                    }
                } else {
                    console.error('Failed to delete text box:', data.error);
                }
            } catch (error) {
                console.error('Error deleting text box:', error);
            }
        }

        // Handle Delete key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Delete' && activeTextBox) {
                // Only delete if not editing text (textarea not focused)
                const textarea = activeTextBox.querySelector('textarea');
                if (document.activeElement !== textarea) {
                    deleteTextBox(activeTextBox);
                }
            } else if (e.key === 'Escape' && activeTextBox) {
                deactivateTextBox(activeTextBox);
            } else if (e.key === 'Escape' && isCreatingTextBox) {
                exitCreatingMode();
            }
        });

        // Deactivate text box when clicking outside
        document.addEventListener('click', (e) => {
            if (activeTextBox && !e.target.closest('.text-box') && !e.target.closest('#addTextBoxBtn')) {
                deactivateTextBox(activeTextBox);
            }
        });

        // Load existing text boxes
        function loadTextBoxes() {
            TEXT_BOXES.forEach(tb => {
                createTextBoxElement(tb.id, tb.x, tb.y, tb.width, tb.text);
            });
        }

        // Initialize
        createPageBoxes();
        loadTextBoxes();
        updateTransform();

        // Show hint on first load
        setTimeout(() => {
            document.getElementById('hint').style.animation = 'fadeInOut 4s ease-in-out';
        }, 500);
    </script>
</body>
</html>
'''

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

WORKSPACE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Puzzle Solver - {{ username }}'s Workspace</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #edf2f7;
            overflow: hidden;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }

        .navbar {
            background: white;
            padding: 0.5rem 1.5rem;
            border-bottom: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            display: flex;
            align-items: center;
            gap: 1.5rem;
            font-size: 0.9rem;
            flex-wrap: wrap;
        }

        .navbar .title {
            color: #667eea;
            font-weight: 600;
            font-size: 1rem;
        }

        .navbar a {
            color: #4a5568;
            text-decoration: none;
            padding: 0.25rem 0.5rem;
            border-radius: 3px;
            transition: background 0.2s;
        }

        .navbar a:hover {
            background: #f7fafc;
            color: #667eea;
        }

        .navbar .divider {
            color: #cbd5e0;
        }

        .workspace-container {
            flex: 1;
            position: relative;
            overflow: hidden;
            background: #edf2f7;
            cursor: grab;
        }

        .workspace-container.panning {
            cursor: grabbing;
        }

        .workspace {
            position: absolute;
            width: 100000px;
            height: 100000px;
            transform-origin: 0 0;
            left: -50000px;
            top: -50000px;
        }

        .workspace.creating {
            cursor: crosshair !important;
        }

        .page-box {
            position: absolute;
            width: 80px;
            height: 50px;
            background: white;
            border: 2px solid #cbd5e0;
            border-radius: 6px;
            display: flex;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: box-shadow 0.2s;
            user-select: none;
        }

        .page-box:hover {
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }

        .page-box.dragging {
            opacity: 0.7;
            cursor: grabbing;
            z-index: 1000;
        }

        .page-drag-area {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: grab;
            font-size: 1.1rem;
            font-weight: 600;
            color: #2d3748;
            border-right: 1px dashed #cbd5e0;
        }

        .page-link-area {
            width: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            background: #f7fafc;
            border-radius: 0 4px 4px 0;
            transition: background 0.2s;
        }

        .page-link-area:hover {
            background: #667eea;
        }

        .page-link-area:hover::after {
            filter: brightness(0) invert(1);
        }

        .page-link-area::after {
            content: '🔗';
            font-size: 0.9rem;
        }

        .zoom-indicator {
            position: absolute;
            bottom: 1rem;
            right: 1rem;
            background: white;
            padding: 0.4rem 0.8rem;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            font-size: 0.8rem;
            color: #718096;
            pointer-events: none;
        }

        .add-textbox-btn {
            padding: 0.4rem 0.8rem;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: background 0.2s;
        }

        .add-textbox-btn:hover {
            background: #5568d3;
        }

        .add-textbox-btn.active {
            background: #48bb78;
        }

        .text-box {
            position: absolute;
            background: rgba(255, 255, 255, 0.05);
            border: 2px dashed #cbd5e0;
            padding: 8px;
            font-size: 1.1rem;
            font-weight: 600;
            color: #2d3748;
            font-family: inherit;
            resize: none;
            overflow: hidden;
            word-wrap: break-word;
            white-space: pre-wrap;
            user-select: none;
            cursor: default;
            z-index: 1;
        }

        .text-box:hover {
            border-color: #a0aec0;
        }

        .text-box.active {
            border: 3px solid #667eea;
            background: rgba(102, 126, 234, 0.08);
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
            user-select: text;
        }

        .text-box.moving {
            cursor: move !important;
        }

        .text-box.active .text-box-textarea {
            cursor: text !important;
        }

        .text-box-textarea {
            width: 100%;
            background: transparent;
            border: none;
            padding: 0;
            font-size: inherit;
            font-weight: inherit;
            color: inherit;
            font-family: inherit;
            resize: none;
            overflow: hidden;
            outline: none;
        }

        /* Border hit targets - these create generous clickable areas */
        .border-top, .border-left, .border-bottom, .border-right {
            position: absolute;
            background: transparent;
            z-index: 10;
        }

        /* Top border - for moving */
        .border-top {
            top: -8px;
            left: -8px;
            right: -8px;
            height: 16px;
            cursor: move !important;
        }

        /* Left border - for moving */
        .border-left {
            top: -8px;
            left: -8px;
            bottom: -8px;
            width: 16px;
            cursor: move !important;
        }

        /* Bottom border - for moving */
        .border-bottom {
            bottom: -8px;
            left: -8px;
            right: -8px;
            height: 16px;
            cursor: move !important;
        }

        /* Right border - for resizing */
        .border-right {
            top: -8px;
            right: -8px;
            bottom: -8px;
            width: 16px;
            cursor: ew-resize !important;
        }

        /* Visual feedback on hover */
        .border-right:hover {
            background: rgba(102, 126, 234, 0.3);
        }

        .hint {
            position: absolute;
            top: 1rem;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.95);
            padding: 0.5rem 1rem;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            font-size: 0.85rem;
            color: #4a5568;
            pointer-events: none;
            opacity: 0;
            animation: fadeInOut 4s ease-in-out;
        }

        @keyframes fadeInOut {
            0%, 100% { opacity: 0; }
            10%, 90% { opacity: 1; }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <span class="title">Workspace: {{ username }}</span>
        <span class="divider">|</span>
        <button class="add-textbox-btn" id="addTextBoxBtn">+ Text Box</button>
        <span class="divider">|</span>
        <a href="{{ url_for('index') }}">All Pages</a>
        <a href="{{ url_for('subjects_list') }}">All Subjects</a>
        <span class="divider">|</span>
        {% for user in workspace_users %}
            <a href="{{ url_for('user_workspace', username=user) }}">{{ user }}</a>
        {% endfor %}
        <span class="divider">|</span>
        <a href="{{ url_for('logout') }}">Logout</a>
    </nav>

    <div class="workspace-container">
        <div class="workspace" id="workspace"></div>
        <div class="zoom-indicator" id="zoomIndicator">100%</div>
        <div class="hint" id="hint">💡 Drag background to pan | Scroll to zoom | Drag boxes to arrange</div>
    </div>

    <script>
        // Configuration
        const TOTAL_PAGES = 100;
        const BOX_WIDTH = 80;
        const BOX_HEIGHT = 50;
        const SPACING_X = 140;
        const SPACING_Y = 100;
        const MARGIN_X = 100;
        const MARGIN_Y = 80;
        const USERNAME = {{ username|tojson }};
        const SAVED_POSITIONS = {{ positions|tojson }};
        const VIEW_STATE = {{ view_state|tojson }};
        const TEXT_BOXES = {{ text_boxes|tojson }};

        // State - load from saved view state, or use sensible defaults
        let scale = VIEW_STATE.zoom || 1;
        // If no saved view state, center on the initial grid
        // The workspace is offset at (-50000, -50000), and boxes start around (100, 80)
        // So we need to pan by ~50000 to bring them into view, centered nicely
        const defaultPanX = 50000 - 200; // Offset to roughly center the grid
        const defaultPanY = 50000 - 200;
        let panX = (VIEW_STATE.pan_x !== 0 || VIEW_STATE.pan_y !== 0 || VIEW_STATE.zoom !== 1) ? VIEW_STATE.pan_x : defaultPanX;
        let panY = (VIEW_STATE.pan_x !== 0 || VIEW_STATE.pan_y !== 0 || VIEW_STATE.zoom !== 1) ? VIEW_STATE.pan_y : defaultPanY;
        let isPanning = false;
        let panStartX = 0;
        let panStartY = 0;
        let draggedElement = null;
        let dragOffsetX = 0;
        let dragOffsetY = 0;

        const workspace = document.getElementById('workspace');
        const zoomIndicator = document.getElementById('zoomIndicator');

        // Calculate optimal rectangular layout based on screen size
        function calculateLayout() {
            const container = document.querySelector('.workspace-container');
            const viewWidth = container.clientWidth;
            const viewHeight = container.clientHeight;

            const availableWidth = viewWidth - 2 * MARGIN_X;
            const boxesPerRow = Math.max(8, Math.min(15, Math.floor(availableWidth / SPACING_X)));
            const numRows = Math.ceil(TOTAL_PAGES / boxesPerRow);

            return { boxesPerRow, numRows };
        }

        // Save position to database
        async function savePosition(pageId, x, y) {
            try {
                const response = await fetch(`/user/${USERNAME}/update-position`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        page_id: pageId,
                        x: x,
                        y: y
                    })
                });

                const data = await response.json();
                if (!data.success) {
                    console.error('Failed to save position:', data.error);
                }
            } catch (error) {
                console.error('Error saving position:', error);
            }
        }

        // Debounced view state save
        let viewStateSaveTimeout = null;
        async function saveViewState() {
            try {
                const response = await fetch(`/user/${USERNAME}/update-view`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        pan_x: panX,
                        pan_y: panY,
                        zoom: scale
                    })
                });

                const data = await response.json();
                if (!data.success) {
                    console.error('Failed to save view state:', data.error);
                }
            } catch (error) {
                console.error('Error saving view state:', error);
            }
        }

        function debouncedSaveViewState() {
            if (viewStateSaveTimeout) {
                clearTimeout(viewStateSaveTimeout);
            }
            viewStateSaveTimeout = setTimeout(saveViewState, 500);
        }

        // Create page boxes
        function createPageBoxes() {
            workspace.innerHTML = '';
            const layout = calculateLayout();

            for (let i = 1; i <= TOTAL_PAGES; i++) {
                const box = document.createElement('div');
                box.className = 'page-box';
                box.dataset.page = i;

                // Calculate default position in rectangular layout
                const row = Math.floor((i - 1) / layout.boxesPerRow);
                const col = (i - 1) % layout.boxesPerRow;
                const defaultX = MARGIN_X + col * SPACING_X;
                const defaultY = MARGIN_Y + row * SPACING_Y;

                // Use saved position or default
                const pos = SAVED_POSITIONS[i] || { x: defaultX, y: defaultY };
                box.style.left = pos.x + 'px';
                box.style.top = pos.y + 'px';

                // Drag area (left side)
                const dragArea = document.createElement('div');
                dragArea.className = 'page-drag-area';
                dragArea.textContent = i;
                dragArea.addEventListener('mousedown', startDrag);

                // Link area (right side) - use real <a> tag
                const linkArea = document.createElement('a');
                linkArea.className = 'page-link-area';
                linkArea.href = `/pages/${i}`;
                linkArea.target = '_blank';
                linkArea.addEventListener('mousedown', (e) => {
                    // Prevent drag from starting when clicking the link
                    e.stopPropagation();
                });

                box.appendChild(dragArea);
                box.appendChild(linkArea);
                workspace.appendChild(box);
            }
        }

        // Drag functionality for page boxes
        function startDrag(e) {
            if (e.button !== 0) return;
            e.preventDefault();
            e.stopPropagation();

            draggedElement = e.target.closest('.page-box');
            draggedElement.classList.add('dragging');

            const rect = draggedElement.getBoundingClientRect();
            const workspaceRect = workspace.getBoundingClientRect();

            dragOffsetX = (e.clientX - rect.left) / scale;
            dragOffsetY = (e.clientY - rect.top) / scale;

            document.addEventListener('mousemove', doDrag);
            document.addEventListener('mouseup', stopDrag);
        }

        function doDrag(e) {
            if (!draggedElement) return;

            const workspaceRect = workspace.getBoundingClientRect();
            const x = (e.clientX - workspaceRect.left) / scale - dragOffsetX;
            const y = (e.clientY - workspaceRect.top) / scale - dragOffsetY;

            draggedElement.style.left = x + 'px';
            draggedElement.style.top = y + 'px';
        }

        function stopDrag(e) {
            if (draggedElement) {
                draggedElement.classList.remove('dragging');

                // Save position to database
                const pageId = parseInt(draggedElement.dataset.page);
                const x = parseFloat(draggedElement.style.left);
                const y = parseFloat(draggedElement.style.top);
                savePosition(pageId, x, y);

                draggedElement = null;
            }
            document.removeEventListener('mousemove', doDrag);
            document.removeEventListener('mouseup', stopDrag);
        }

        // Pan functionality - handle at container level so you can pan anywhere
        document.querySelector('.workspace-container').addEventListener('mousedown', (e) => {
            if (e.button !== 0) return;
            // Only start panning if clicking on workspace or container background (not on page boxes)
            if (e.target === workspace ||
                e.target.classList.contains('workspace') ||
                e.target.classList.contains('workspace-container')) {
                isPanning = true;
                panStartX = e.clientX - panX;
                panStartY = e.clientY - panY;
                document.querySelector('.workspace-container').classList.add('panning');
            }
        });

        document.addEventListener('mousemove', (e) => {
            if (isPanning) {
                panX = e.clientX - panStartX;
                panY = e.clientY - panStartY;
                updateTransform();
            }
        });

        document.addEventListener('mouseup', () => {
            if (isPanning) {
                isPanning = false;
                document.querySelector('.workspace-container').classList.remove('panning');
                // Save view state after panning
                debouncedSaveViewState();
            }
        });

        // Zoom functionality
        const WORKSPACE_OFFSET_X = -50000;
        const WORKSPACE_OFFSET_Y = -50000;

        document.querySelector('.workspace-container').addEventListener('wheel', (e) => {
            e.preventDefault();

            const delta = e.deltaY > 0 ? 0.9 : 1.1;
            const newScale = Math.max(0.1, Math.min(3, scale * delta));

            // Zoom toward mouse position (relative to viewport/container)
            const container = document.querySelector('.workspace-container');
            const containerRect = container.getBoundingClientRect();
            const mouseX = e.clientX - containerRect.left;
            const mouseY = e.clientY - containerRect.top;

            // Calculate workspace coordinate under mouse
            // viewport = WORKSPACE_OFFSET + panX + workspace_x * scale
            // workspace_x = (viewport - WORKSPACE_OFFSET - panX) / scale
            const workspaceX = (mouseX - WORKSPACE_OFFSET_X - panX) / scale;
            const workspaceY = (mouseY - WORKSPACE_OFFSET_Y - panY) / scale;

            // Adjust pan so that the same workspace point stays under the mouse
            // mouseX = WORKSPACE_OFFSET + newPanX + workspaceX * newScale
            panX = mouseX - WORKSPACE_OFFSET_X - workspaceX * newScale;
            panY = mouseY - WORKSPACE_OFFSET_Y - workspaceY * newScale;

            scale = newScale;
            updateTransform();

            // Save view state after zooming
            debouncedSaveViewState();
        }, { passive: false });

        function updateTransform() {
            workspace.style.transform = `translate(${panX}px, ${panY}px) scale(${scale})`;
            zoomIndicator.textContent = `${Math.round(scale * 100)}%`;
        }

        // ===================
        // TEXT BOX FUNCTIONALITY
        // ===================

        let isCreatingTextBox = false;
        let activeTextBox = null;
        let textBoxes = new Map();
        let resizingTextBox = null;
        let resizeStartX = 0;
        let resizeStartWidth = 0;
        let movingTextBox = null;
        let moveStartX = 0;
        let moveStartY = 0;

        // Create text box element
        function createTextBoxElement(id, x, y, width, text) {
            const box = document.createElement('div');
            box.className = 'text-box';
            box.dataset.id = id;
            box.style.left = x + 'px';
            box.style.top = y + 'px';
            box.style.width = width + 'px';

            const textarea = document.createElement('textarea');
            textarea.className = 'text-box-textarea';
            textarea.value = text;
            textarea.readOnly = true;

            // Create four border hit targets
            const borderTop = document.createElement('div');
            borderTop.className = 'border-top';

            const borderLeft = document.createElement('div');
            borderLeft.className = 'border-left';

            const borderBottom = document.createElement('div');
            borderBottom.className = 'border-bottom';

            const borderRight = document.createElement('div');
            borderRight.className = 'border-right';

            box.appendChild(textarea);
            box.appendChild(borderTop);
            box.appendChild(borderLeft);
            box.appendChild(borderBottom);
            box.appendChild(borderRight);

            // Right border = resize
            borderRight.addEventListener('mousedown', (e) => {
                e.stopPropagation();
                e.preventDefault();
                startResize(e, box);
            });

            // Top, left, bottom borders = move
            [borderTop, borderLeft, borderBottom].forEach(border => {
                border.addEventListener('mousedown', (e) => {
                    e.stopPropagation();
                    e.preventDefault();
                    if (!box.classList.contains('active')) {
                        activateTextBox(box);
                    }
                    startMove(e, box);
                });
            });

            // Click on box or textarea to activate (not on borders)
            box.addEventListener('mousedown', (e) => {
                // If click was on a border, let the border handle it
                if (e.target.classList.contains('border-top') ||
                    e.target.classList.contains('border-left') ||
                    e.target.classList.contains('border-bottom') ||
                    e.target.classList.contains('border-right')) {
                    return;
                }

                // Click on textarea or box body
                if (!box.classList.contains('active')) {
                    e.stopPropagation();
                    activateTextBox(box);
                    // Start moving if not clicking on textarea
                    if (e.target !== textarea) {
                        startMove(e, box);
                    }
                }
                // If already active and clicking textarea, allow text editing
            });

            // Auto-resize height as text changes
            textarea.addEventListener('input', () => {
                adjustTextBoxHeight(box);
                debouncedSaveTextBox(box);
            });

            workspace.appendChild(box);
            textBoxes.set(id, box);
            adjustTextBoxHeight(box);
            return box;
        }

        // Adjust text box height to fit content
        function adjustTextBoxHeight(box) {
            const textarea = box.querySelector('textarea');
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
        }

        // Activate text box for editing
        function activateTextBox(box) {
            // Deactivate any currently active box
            if (activeTextBox && activeTextBox !== box) {
                deactivateTextBox(activeTextBox);
            }

            box.classList.add('active');
            const textarea = box.querySelector('textarea');
            textarea.readOnly = false;
            textarea.focus();
            activeTextBox = box;
        }

        // Deactivate text box
        function deactivateTextBox(box) {
            box.classList.remove('active');
            const textarea = box.querySelector('textarea');
            textarea.readOnly = true;
            activeTextBox = null;
        }

        // Start text box creation mode
        document.getElementById('addTextBoxBtn').addEventListener('click', () => {
            if (isCreatingTextBox) {
                exitCreatingMode();
            } else {
                enterCreatingMode();
            }
        });

        function enterCreatingMode() {
            isCreatingTextBox = true;
            document.getElementById('addTextBoxBtn').classList.add('active');
            document.querySelector('.workspace-container').style.cursor = 'crosshair';
            workspace.classList.add('creating');
        }

        function exitCreatingMode() {
            isCreatingTextBox = false;
            document.getElementById('addTextBoxBtn').classList.remove('active');
            document.querySelector('.workspace-container').style.cursor = '';
            workspace.classList.remove('creating');
        }

        // Handle click to place text box
        document.querySelector('.workspace-container').addEventListener('click', (e) => {
            if (isCreatingTextBox && (e.target.classList.contains('workspace') ||
                e.target.classList.contains('workspace-container'))) {
                const containerRect = document.querySelector('.workspace-container').getBoundingClientRect();
                const clickX = e.clientX - containerRect.left;
                const clickY = e.clientY - containerRect.top;

                // Convert to workspace coordinates
                const workspaceX = (clickX - WORKSPACE_OFFSET_X - panX) / scale;
                const workspaceY = (clickY - WORKSPACE_OFFSET_Y - panY) / scale;

                createNewTextBox(workspaceX, workspaceY);
                exitCreatingMode();
            }
        });

        // Create new text box via API
        async function createNewTextBox(x, y) {
            try {
                const response = await fetch(`/user/${USERNAME}/text-box`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        x: Math.round(x),
                        y: Math.round(y),
                        width: 200,
                        text: ''
                    })
                });

                const data = await response.json();
                if (data.success) {
                    const box = createTextBoxElement(data.id, x, y, 200, '');
                    activateTextBox(box);
                } else {
                    console.error('Failed to create text box:', data.error);
                }
            } catch (error) {
                console.error('Error creating text box:', error);
            }
        }

        // Resize functionality
        function startResize(e, box) {
            e.preventDefault();
            e.stopPropagation();
            resizingTextBox = box;
            resizeStartX = e.clientX;
            resizeStartWidth = parseInt(box.style.width);

            document.addEventListener('mousemove', doResize);
            document.addEventListener('mouseup', stopResize);
        }

        function doResize(e) {
            if (!resizingTextBox) return;

            const deltaX = (e.clientX - resizeStartX) / scale;
            const newWidth = Math.max(100, resizeStartWidth + deltaX);
            resizingTextBox.style.width = newWidth + 'px';
            adjustTextBoxHeight(resizingTextBox);
        }

        function stopResize() {
            if (resizingTextBox) {
                debouncedSaveTextBox(resizingTextBox);
                resizingTextBox = null;
            }
            document.removeEventListener('mousemove', doResize);
            document.removeEventListener('mouseup', stopResize);
        }

        // Move functionality
        function startMove(e, box) {
            if (e.target.tagName === 'TEXTAREA') return; // Don't move when editing text

            e.preventDefault();
            e.stopPropagation();
            movingTextBox = box;
            moveStartX = e.clientX;
            moveStartY = e.clientY;
            box.classList.add('moving');

            document.addEventListener('mousemove', doMove);
            document.addEventListener('mouseup', stopMove);
        }

        function doMove(e) {
            if (!movingTextBox) return;

            const deltaX = (e.clientX - moveStartX) / scale;
            const deltaY = (e.clientY - moveStartY) / scale;

            const currentX = parseFloat(movingTextBox.style.left);
            const currentY = parseFloat(movingTextBox.style.top);

            movingTextBox.style.left = (currentX + deltaX) + 'px';
            movingTextBox.style.top = (currentY + deltaY) + 'px';

            moveStartX = e.clientX;
            moveStartY = e.clientY;
        }

        function stopMove() {
            if (movingTextBox) {
                movingTextBox.classList.remove('moving');
                debouncedSaveTextBox(movingTextBox);
                movingTextBox = null;
            }
            document.removeEventListener('mousemove', doMove);
            document.removeEventListener('mouseup', stopMove);
        }

        // Save text box to database (debounced)
        let textBoxSaveTimeouts = new Map();

        function debouncedSaveTextBox(box) {
            const id = box.dataset.id;
            if (textBoxSaveTimeouts.has(id)) {
                clearTimeout(textBoxSaveTimeouts.get(id));
            }
            textBoxSaveTimeouts.set(id, setTimeout(() => saveTextBox(box), 500));
        }

        async function saveTextBox(box) {
            const id = box.dataset.id;
            const textarea = box.querySelector('textarea');

            try {
                const response = await fetch(`/user/${USERNAME}/text-box/${id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        x: Math.round(parseFloat(box.style.left)),
                        y: Math.round(parseFloat(box.style.top)),
                        width: Math.round(parseFloat(box.style.width)),
                        text: textarea.value
                    })
                });

                const data = await response.json();
                if (!data.success) {
                    console.error('Failed to save text box:', data.error);
                }
            } catch (error) {
                console.error('Error saving text box:', error);
            }
        }

        // Delete text box
        async function deleteTextBox(box) {
            const id = box.dataset.id;

            try {
                const response = await fetch(`/user/${USERNAME}/text-box/${id}`, {
                    method: 'DELETE'
                });

                const data = await response.json();
                if (data.success) {
                    box.remove();
                    textBoxes.delete(parseInt(id));
                    if (activeTextBox === box) {
                        activeTextBox = null;
                    }
                } else {
                    console.error('Failed to delete text box:', data.error);
                }
            } catch (error) {
                console.error('Error deleting text box:', error);
            }
        }

        // Handle Delete key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Delete' && activeTextBox) {
                // Only delete if not editing text (textarea not focused)
                const textarea = activeTextBox.querySelector('textarea');
                if (document.activeElement !== textarea) {
                    deleteTextBox(activeTextBox);
                }
            } else if (e.key === 'Escape' && activeTextBox) {
                deactivateTextBox(activeTextBox);
            } else if (e.key === 'Escape' && isCreatingTextBox) {
                exitCreatingMode();
            }
        });

        // Deactivate text box when clicking outside
        document.addEventListener('click', (e) => {
            if (activeTextBox && !e.target.closest('.text-box') && !e.target.closest('#addTextBoxBtn')) {
                deactivateTextBox(activeTextBox);
            }
        });

        // Load existing text boxes
        function loadTextBoxes() {
            TEXT_BOXES.forEach(tb => {
                createTextBoxElement(tb.id, tb.x, tb.y, tb.width, tb.text);
            });
        }

        // Initialize
        createPageBoxes();
        loadTextBoxes();
        updateTransform();

        // Show hint on first load
        setTimeout(() => {
            document.getElementById('hint').style.animation = 'fadeInOut 4s ease-in-out';
        }, 500);
    </script>
</body>
</html>
'''
