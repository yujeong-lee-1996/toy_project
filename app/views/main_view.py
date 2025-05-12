### app/views/main_view.py
from flask import Blueprint, render_template, request
from app.modules.gemini_api import call_gemini

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def main_view():
    return render_template('index.html')

@main_bp.route('/chat-demo', methods=['GET', 'POST'])
def chat_demo():
    result = ""
    if request.method == 'POST':
        question = request.form['question']
        result = call_gemini(question)
    return render_template('chat_demo.html', result=result)