from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-pro')

# System prompt for humorous responses
SYSTEM_PROMPT = """You are a witty and humorous AI assistant. Your responses should be:
1. Funny and engaging
2. Include appropriate jokes and puns
3. Maintain a light-hearted tone
4. Be creative with your humor
5. Keep responses concise but entertaining

Remember to be respectful and avoid offensive humor."""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        # Combine system prompt with user message
        prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nAssistant:"
        
        # Generate response
        response = model.generate_content(prompt)
        
        return jsonify({
            'response': response.text,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'The humorous AI is ready to chat!'
    })

if __name__ == '__main__':
    app.run(debug=True) 