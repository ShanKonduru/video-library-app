from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('video-library.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create
@app.route('/add', methods=['POST'])
def add_item():
    if request.method == 'POST':
        title = request.form['title']
        url = request.form['url']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (title, url) VALUES (?, ?)", (title, url))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

# Read
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()

    return render_template('index.html', items=items)

# Update
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    if request.method == 'GET':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items WHERE id = ?", (id,))
        item = cursor.fetchone()
        conn.close()

        return render_template('edit.html', item=item)
    elif request.method == 'POST':
        title = request.form['title']
        url = request.form['url']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE items SET title = ?, url = ? WHERE id = ?", (title, url, id))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

# Delete
@app.route('/delete/<int:id>')
def delete_item(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
