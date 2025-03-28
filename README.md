# Humorous AI Chat 🤖

A fun and interactive chat application that uses Google's Gemini AI to create engaging, humorous conversations! This project combines the power of artificial intelligence with a sprinkle of humor to create an entertaining chat experience.

## 🌟 Features

- Real-time chat interface with a modern design
- AI-powered responses with a humorous twist
- Easy-to-use web interface
- Secure API key management
- Responsive design that works on all devices

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- A Google API key (Get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Prathap452000/Humour_Conv_ai.git
   cd Humour_Conv_ai
   ```

2. **Set up the virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Unix/MacOS
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   - Create a `.env` file in the project root
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in your browser**
   - Go to `http://localhost:5000`
   - Start chatting with the humorous AI!

## 💡 How to Use

1. Open the application in your web browser
2. Type your message in the chat box
3. Press Enter or click Send
4. Wait for the AI's witty response!

## 🛠️ Built With

- Python
- Flask
- Google Gemini AI
- HTML/CSS/JavaScript
- Python-dotenv

## 🔒 Security

- API keys are stored securely in environment variables
- No sensitive data is stored or transmitted
- All communication is done over HTTPS

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for providing the powerful language model
- Flask framework for the web application
- All contributors who help improve this project

## 📧 Contact

Your Name - prathap452000@gmail.com.com

Project Link: [https://github.com/Prathap452000/Humour_Conv_ai](https://github.com/Prathap452000/Humour_Conv_ai)

## API Endpoints

- `POST /chat`: Send a message to the AI
- `GET /health`: Check if the server is running

## Note

Make sure to keep your API key secure and never commit it to version control. 
