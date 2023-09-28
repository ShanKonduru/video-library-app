from flask import Flask, request, jsonify
import sqlite3
import datetime

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8888"}})

DBNAME = 'video-library.db'

def setup_database():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    # Check if the calculations table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='items'")
    table_exists = cursor.fetchone()

    if not table_exists:
        cursor.execute('''
            CREATE TABLE items  (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                url TEXT
            )
        ''')
        print("Table 'items' created.")

    conn.commit()
    conn.close()

@app.route('/get_all_records', methods=['GET'])
def get_all_records():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    # Retrieve all records from the items table
    cursor.execute('SELECT * FROM items')
    records = cursor.fetchall()

    conn.close()

    # Convert records to a list of dictionaries
    records_list = []
    for record in records:
        record_dict = {
            'Id': record[0],
            'title': record[1],
            'url': record[2]
        }
        records_list.append(record_dict)

    return jsonify(records_list)


@app.route('/insert', methods=['POST'])
def insert_calculation():
    data = request.get_json()

    title = data['title']
    url = data['url']
    
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    # Insert the record into the database
    cursor.execute('''
        INSERT INTO items (title, url)
        VALUES (?, ?)
    ''', (title, url))

    conn.commit()
    conn.close()

    return jsonify({"message": "Record inserted successfully"})

if __name__ == '__main__':
    setup_database()
    app.run(debug=True, host='0.0.0.0', port=5555)
