### app/views/tarot_view.py
from flask import Blueprint, render_template, request
import json
import os
import random

# Blueprint
tarot_bp = Blueprint('tarot', __name__, url_prefix='/tarot')

# Load data once
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'tarot_major_arcana.json')
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    tarot_cards = json.load(f)

@tarot_bp.route('/')
def tarot_menu():
    return render_template('tarot_menu.html')

@tarot_bp.route('/draw-random')
def draw_random():
    selected = random.sample(tarot_cards, 3)
    return render_template('draw_random.html', cards=selected)

@tarot_bp.route('/draw-select', methods=['POST'])
def draw_select():
    selected_names = request.form.getlist('cards')
    selected = [card for card in tarot_cards if card['name'] in selected_names]
    return render_template('draw_select.html', cards=selected)