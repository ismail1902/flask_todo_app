# 📝 Flask Todo App

A simple and beautiful todo list application built with Flask and SQLite. Perfect for beginners learning web development with Python!

![Flask](https://img.shields.io/badge/Flask-3.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)

## ✨ Features

- ✅ Add new todos
- ✏️ Edit existing todos
- ✓ Mark todos as complete/incomplete
- 🗑️ Delete todos
- 💾 Persistent storage with SQLite database
- 🎨 Beautiful gradient UI with responsive design
- 📱 Mobile-friendly interface

## 📸 Screenshots

The app features a clean, modern interface with:
- Purple gradient background
- Card-based todo items
- Color-coded action buttons
- Flash messages for user feedback

## 🛠️ Technologies Used

- **Flask** - Python web framework
- **Flask-SQLAlchemy** - Database ORM for Flask
- **SQLite** - Lightweight database
- **HTML/CSS** - Frontend styling
- **Jinja2** - Template engine (comes with Flask)

## 📁 Project Structure

```
flask-todo-app/
├── app.py                 # Main application file with routes
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── index.html        # Main todo list page
│   └── edit.html         # Edit todo page
└── instance/             # Created automatically
    └── todos.db          # SQLite database (auto-generated)
```

## 🚀 Getting Started

Follow these steps to set up and run the application on your local machine.

### Prerequisites

- Python 3.7 or higher installed on your computer
- Basic knowledge of command line/terminal
- A text editor or IDE (VS Code, PyCharm, etc.)

### Step 1: Download the Project

Clone or download this repository to your local machine.

```bash
# If using git
git clone <repository-url>
cd flask-todo-app

# Or simply download and extract the ZIP file
```

### Step 2: Create Project Structure

Make sure your project has the following structure:

```
flask-todo-app/
├── app.py
├── models.py
├── requirements.txt
└── templates/
    ├── index.html
    └── edit.html
```

### Step 3: Create a Virtual Environment

A virtual environment keeps your project dependencies isolated from other Python projects.

**On Windows:**
```bash
python3 -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear at the beginning of your command line, indicating the virtual environment is active.

### Step 4: Install Dependencies

With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask 3.0.0
- Flask-SQLAlchemy 3.1.1
- python-dotenv 1.0.0

### Step 5: Run the Application

Start the Flask development server:

```bash
python app.py
```

You should see output similar to:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 6: Open in Browser

Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

or

```
http://localhost:5000
```

🎉 **Congratulations!** Your todo app is now running!

## 📖 How to Use

### Adding a Todo
1. Type your todo in the input field at the top
2. Click the "Add Todo" button
3. Your todo will appear in the list below

### Marking as Complete
1. Click the green "✓" button next to any todo
2. The todo will be marked with a strikethrough
3. Click "Undo" to mark it as incomplete again

### Editing a Todo
1. Click the orange "Edit" button next to any todo
2. Modify the text in the edit form
3. Click "Save Changes" to update, or "Cancel" to go back

### Deleting a Todo
1. Click the red "Delete" button next to any todo
2. Confirm the deletion in the popup dialog
3. The todo will be permanently removed

## 🗄️ Database

The app uses SQLite, a lightweight database that stores data in a single file.

- Database file: `instance/todos.db`
- Created automatically when you first run the app
- No additional setup required!

### Database Schema

**Todo Table:**
| Column     | Type     | Description                    |
|------------|----------|--------------------------------|
| id         | Integer  | Primary key (auto-increment)   |
| title      | String   | Todo text (max 200 characters) |
| completed  | Boolean  | Completion status (default: False) |
| created_at | DateTime | Timestamp when todo was created |

## 🔧 Configuration

The app configuration is in `app.py`:

```python
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

**Important:** Change the `SECRET_KEY` if you deploy this app to production!

## 📝 Code Explanation

### app.py
The main application file containing:
- Flask app initialization
- Database configuration
- Route handlers for all operations (add, edit, delete, complete)
- Flash messages for user feedback

### models.py
Defines the database structure:
- `Todo` class representing a todo item
- Database columns and their types
- SQLAlchemy ORM setup

### templates/index.html
The main page showing:
- Todo input form
- List of all todos
- Action buttons for each todo
- Flash messages display

### templates/edit.html
The edit page with:
- Form pre-filled with current todo text
- Save and Cancel buttons
- Consistent styling with main page

## 🐛 Troubleshooting

### Port Already in Use
If you see an error about port 5000 being in use:
```bash
# Use a different port
flask run --port 5001
```

### Virtual Environment Not Activating
Make sure you're in the project directory and try:
```bash
# Windows
.\venv\Scripts\activate

# Mac/Linux
source ./venv/bin/activate
```

### Module Not Found Error
Make sure your virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Database Issues
If you encounter database errors, delete the `instance` folder and restart the app. It will create a fresh database.

## 🎓 Learning Resources

If you're new to Flask, check out these resources:
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## 🚀 Next Steps

Want to enhance this app? Try adding:
- User authentication (login/register)
- Todo categories or tags
- Due dates and reminders
- Priority levels
- Search and filter functionality
- Dark mode toggle
- Export todos to CSV/JSON
- Deploy to a cloud platform (Heroku, PythonAnywhere, AWS)

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this project and make your own improvements!

## 💡 Tips for Beginners

1. **Always activate your virtual environment** before working on the project
2. **Read error messages carefully** - they usually tell you what's wrong
3. **Use `print()` statements** to debug and understand the code flow
4. **Experiment!** Try modifying the CSS, adding new features, or changing colors
5. **Check the browser console** (F12) for any JavaScript errors
6. **Use Flask debug mode** (already enabled) to see detailed error pages

## 📞 Need Help?

If you encounter any issues:
1. Check the Troubleshooting section above
2. Read the error message carefully
3. Search for the error on Google or Stack Overflow
4. Make sure all files are in the correct locations
5. Verify your Python version: `python --version`

---

**Happy Coding! 🎉**

Made with ❤️ using Flask
