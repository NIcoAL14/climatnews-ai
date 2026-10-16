from flask import Flask, render_template, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Configuración de la base de datos
DB_NAME = 'climate_news.db'

def init_db():
    """Inicializa la base de datos"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            source TEXT,
            date TEXT,
            impact_level TEXT,
            keywords TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard con visualizaciones"""
    return render_template('dashboard.html')

@app.route('/api/news')
def get_news():
    """API para obtener noticias"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM news ORDER BY date DESC LIMIT 20')
    news = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(news)

@app.route('/api/stats')
def get_stats():
    """API para obtener estadísticas"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT impact_level, COUNT(*) as count FROM news GROUP BY impact_level')
    stats = dict(cursor.fetchall())
    conn.close()
    return jsonify(stats)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
