from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__, template_folder='/home/maximcode/mysite/templates')
DATA_FILE = "/home/maximcode/mysite/whiteboard_data.json"

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        default_data = {
            "new_products": [],
            "low_products": [],
            "out_of_stock": [],
            "expiring": [],
            "shift_notes": []
        }
        save_data(default_data)
        return default_data

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    data = load_data()
    app.logger.info(f"Looking for template in: {app.jinja_loader.searchpath}")
    return render_template('index.html', data=data)

@app.route('/add_item', methods=['POST'])
def add_item():
    data = load_data()
    section = request.form['section']
    item = request.form['item'].strip()
    if item and section in data:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        full_item = f"{item} (Added: {timestamp})"
        data[section].append(full_item)
        save_data(data)
        return jsonify({'success': True, 'item': full_item})
    return jsonify({'success': False})

@app.route('/delete_item', methods=['POST'])
def delete_item():
    data = load_data()
    section = request.form['section']
    index = int(request.form['index'])
    if section in data and 0 <= index < len(data[section]):
        data[section].pop(index)
        save_data(data)
        return jsonify({'success': True})
    return jsonify({'success': False})