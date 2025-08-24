from flask import Flask, render_template, request, jsonify # pyright: ignore[reportMissingImports]
import random
import time
import datetime
from flask_cors import CORS # pyright: ignore[reportMissingModuleSource]

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Enhanced chatbot responses with more context
def get_bot_response(user_message):
    user_message = user_message.lower().strip()
    
    # Comprehensive response dictionary
    responses = {
        'hello': "Hello there! 👋 Welcome to ChatBot Pro! How can I assist you today?",
        'hi': "Hi! 😊 Great to see you! What can I help you with?",
        'hey': "Hey there! 👋 What's on your mind today?",
        'how are you': "I'm functioning perfectly! ⚡ As an AI, I don't have feelings, but I'm always ready to help you! How about you?",
        'what is your name': "I'm ChatBot Pro! 🤖 Your friendly AI assistant designed to make your life easier.",
        'bye': "Goodbye! 👋 Feel free to come back anytime you need assistance!",
        'goodbye': "Take care! 🌟 I'll be here whenever you need me!",
        'thanks': "You're very welcome! 😊 Is there anything else I can help you with?",
        'thank you': "My pleasure! 🎯 Let me know if you need anything else.",
        'help': "I can help you with various tasks! 💡 I can answer questions, provide information, have conversations, assist with queries, and much more! What specifically do you need help with?",
        'weather': "I don't have real-time weather data access currently. 🌤️ But I can tell you it's always perfect weather for chatting in the digital world!",
        'time': f"The current time is approximately {datetime.datetime.now().strftime('%H:%M')} ⏰, but I recommend checking your device for the most accurate time.",
        'date': f"Today is {datetime.datetime.now().strftime('%B %d, %Y')} 📅. Another great day to get things done!",
        'joke': "Why don't scientists trust atoms? Because they make up everything! 😄",
        'fun fact': "Did you know? The first computer bug was an actual insect! 🐛 In 1947, engineers found a moth stuck in a Harvard Mark II computer.",
        'who made you': "I was created by a talented developer using Python Flask and modern web technologies! 💻",
        'what can you do': "I can do quite a lot! 🚀 I can chat with you, answer questions, provide information, tell jokes, share fun facts, help with queries, and much more! What would you like to try?",
        'how old are you': "I'm brand new! 🎉 I was just created, so consider me your fresh, modern AI assistant!",
        'where are you from': "I live in the cloud! ☁️ Specifically, I run on a server powered by Python Flask, ready to assist you anytime.",
        'love you': "Aww, that's sweet! ❤️ I'm here to help and make your day better!",
        'sorry': "No need to apologize! 😊 We all make mistakes. How can I help you move forward?",
        'how to use': "Using me is easy! 💬 Just type your message and I'll respond. You can ask questions, request information, or just chat!",
        'features': "I offer real-time chatting, quick responses, multiple conversation topics, and a beautiful dashboard interface! 🎨 What feature would you like to explore?",
        'support': "I'm here to support you! 🤝 What do you need help with? You can ask me questions, get information, or just chat about anything.",
        'dashboard': "The dashboard shows your chat statistics, active users, response times, and satisfaction metrics! 📊 Pretty cool, right?",
        'statistics': "I can show you chat analytics including message counts, response times, and user engagement metrics! 📈",
        'settings': "You can customize your experience through the settings menu! ⚙️ What would you like to adjust?",
        'users': "The users section shows active participants and their engagement levels! 👥"
    }
    
    # Check for keyword matches with priority
    for key in responses:
        if key in user_message:
            return responses[key]
    
    # Contextual responses based on message content
    if any(word in user_message for word in ['how', 'what', 'when', 'where', 'why', 'who']):
        contextual_responses = [
            "That's an interesting question! 🤔 Let me think about that...",
            "Great question! 💭 I'd be happy to help you with that.",
            "I appreciate your curiosity! 🌟 Let me provide some insights on that.",
            "That's a thoughtful question! 📚 Here's what I can tell you about that topic.",
            "Interesting inquiry! 🔍 Let me share some information about that."
        ]
        return random.choice(contextual_responses)
    
    # Default engaging responses
    default_responses = [
        "That's fascinating! 🎯 Tell me more about what you're thinking.",
        "I understand! 💡 How can I assist you further with this?",
        "Great point! 🚀 What else would you like to discuss or explore?",
        "I'm here to help! 🤝 Could you elaborate a bit more on that?",
        "Fascinating perspective! 🌈 I'd love to hear more about your thoughts on this.",
        "That's really interesting! 💫 What specifically would you like to know more about?",
        "I appreciate you sharing that! ✨ How can I make this conversation more helpful for you?",
        "Wonderful! 🎉 What aspect of this would you like to dive deeper into?",
        "Noted! 📝 How would you like me to assist you with this information?",
        "Interesting! 🔮 What would you like to do next with this conversation?"
    ]
    
    return random.choice(default_responses)

@app.route('/')
def index():
    """Serve the main chat dashboard"""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    """Handle chat messages and return bot responses"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'error': 'No message provided',
                'timestamp': datetime.datetime.now().isoformat()
            }), 400
        
        # Simulate realistic processing time (0.3-1.5 seconds)
        processing_time = random.uniform(0.3, 1.5)
        time.sleep(processing_time)
        
        # Get bot response
        bot_response = get_bot_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'timestamp': datetime.datetime.now().isoformat(),
            'processing_time': f"{processing_time:.2f}s"
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'message': str(e),
            'timestamp': datetime.datetime.now().isoformat()
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'service': 'ChatBot Pro API'
    })

@app.route('/stats')
def get_stats():
    """Get chat statistics (mock data for demo)"""
    return jsonify({
        'total_chats': random.randint(1000, 2000),
        'active_users': random.randint(50, 150),
        'response_time': f"{random.uniform(0.2, 0.8):.2f}s",
        'satisfaction_rate': f"{random.randint(85, 98)}%",
        'timestamp': datetime.datetime.now().isoformat()
    })

if __name__ == '__main__':
    # Run the Flask application
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )

