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
    
    Returns:
        JSON: {"success": bool, "message": str}
    """
    def user_ok(user):
        if request.json["username"] != user["username"]:
            return False
        if request.json["password"] != user["password"]:
            return False
        return True

    if any(filter(user_ok, users)):
        return {"success": True, "message": "👍"}, 200
    
    return {"success": False, "message": "Not implemented"}, 401

@app.route('/api/stream-story')
def stream_story():
    """Stream a story line by line with delays
    
    Returns:
        Response: Streaming response with story chunks
    """
    def generator(chunks):
        for chunk in chunks:
            time.sleep(0.1)
            yield chunk

    yield from generator(STORY_CHUNKS)
