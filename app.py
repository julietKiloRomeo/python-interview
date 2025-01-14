from flask import Flask, request, Response
import time

# Mock database - in production this would be a proper database
users = [{"username": "user", "password": "password"}]

# Sample story chunks for streaming demo
STORY_CHUNKS = [
    "Once upon a time in a digital realm...\n",
    "There was a mysterious API endpoint...\n",
    "It had the power to stream data slowly...\n",
    "And developers would watch in anticipation...\n",
    "As each line appeared, one by one...\n"
]

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    """Authenticate user login
    
    Expected request body: {"username": "user", "password": "pass"}
    
    Tasks:
    1. Get username and password from request
    2. Check if user exists and password matches
    3. Return appropriate success/error response with status code
    
    Returns:
        JSON: {"success": bool, "message": str}
    """
    return {"success": False, "message": "Not implemented"}, 401

@app.route('/api/stream-story')
def stream_story():
    """Stream a story line by line with delays
    
    Tasks:
    1. Create a generator function that yields story chunks
    2. Add 1-second delay between chunks
    3. Return streaming response with text/plain mime type
    4. (Bonus) Handle client disconnection gracefully
    
    Returns:
        Response: Streaming response with story chunks
    """
    return