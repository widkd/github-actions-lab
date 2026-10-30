import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        port=os.environ.get('DB_PORT', '5432'),
        dbname=os.environ.get('DB_NAME', 'myapp'),
        user=os.environ.get('DB_USER', 'app_user'),
        password=os.environ.get('DB_PASSWORD', 'secure_password')
    )

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/data')
def api_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM items;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({"items": rows}), 200

@app.route('/api/items/count')
def items_count():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM items;')
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return str(count), 200

if __name__ == '__main__':
    port = int(os.environ.get('APP_PORT', 3000))
    app.run(host='0.0.0.0', port=port)
