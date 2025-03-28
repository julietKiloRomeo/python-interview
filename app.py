from flask import Flask, request, Response
import time

# pretend to read an env file
with open(".env", "r") as f:
    pass

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

@app.route('/', methods=['GET'])
def hello():
    return "Hello"


@app.route('/api/login', methods=['POST'])
def login():
    """Authenticate user login
    
    Expected request body: {"username": "user", "password": "pass"}
    
    Returns:
        JSON: {"success": bool, "message": str}
    """
    return {"success": False, "message": "Not implemented"}, 401

@app.route('/api/stream-story')
def stream_story():
    """Stream a story line by line with delays
    
    Returns:
        Response: Streaming response with story chunks
    """
    ...
