"""
Flask Todo List Application
A complete beginner-friendly todo app with database integration
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Todo
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with our app
db.init_app(app)


@app.route('/')
def index():
    """Home page - displays all todos"""
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    """Add a new todo item"""
    title = request.form.get('title')
    
    if not title or not title.strip():
        flash('Todo title cannot be empty!', 'error')
        return redirect(url_for('index'))
    
    new_todo = Todo(title=title.strip())
    db.session.add(new_todo)
    db.session.commit()
    
    flash('Todo added successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    """Toggle a todo's completion status"""
    todo = Todo.query.get_or_404(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    
    status = "completed" if todo.completed else "uncompleted"
    flash(f'Todo marked as {status}!', 'success')
    
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    """Delete a todo item"""
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    
    flash('Todo deleted successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    """Edit a todo item"""
    todo = Todo.query.get_or_404(todo_id)
    
    if request.method == 'POST':
        new_title = request.form.get('title')
        
        if not new_title or not new_title.strip():
            flash('Todo title cannot be empty!', 'error')
            return redirect(url_for('edit_todo', todo_id=todo_id))
        
        todo.title = new_title.strip()
        db.session.commit()
        
        flash('Todo updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit.html', todo=todo)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)