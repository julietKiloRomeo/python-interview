import json
from app import app


def test_login_endpoint():
   """Test the /api/login endpoint with valid credentials.
   
   This test verifies that:
   1. The endpoint accepts POST requests with JSON data
   2. Returns 200 status code on success
   3. Handles username/password authentication correctly

   Expected request format:
       POST /api/login
       {"username": "user", "password": "pass"}
   """
   client = app.test_client()
   response = client.post('/api/login', 
       json={"username": "user", "password": "password"})
   assert response.status_code == 200


def test_stream_endpoint():
   """Test the /api/stream-story endpoint's streaming functionality.
   
   This test verifies that:
   1. The endpoint successfully streams data in chunks
   2. Content matches expected story format and content
   3. Proper streaming response is maintained (multiple chunks)
   4. Story content includes expected formatting (newlines)

   The test:
   1. Makes request to streaming endpoint
   2. Collects all chunks from the response
   3. Validates chunk count and content structure
   4. Checks for specific story elements and formatting

   Expected response format:
       - Multiple chunks of story text
       - Each chunk ends with newline
       - Contains specific story elements (e.g. "Once upon a time")
       - At least 3 separate lines in total content
   """
   client = app.test_client()
   response = client.get('/api/stream-story')
   assert response.status_code == 200
   
   # Collect the streaming response chunks
   # Each chunk is decoded from bytes to string
   chunks = []
   for chunk in response.response:
       chunks.append(chunk.decode('utf-8'))
   
   # Combine chunks and verify content structure
   full_text = ''.join(chunks)
   
   # Test 1: Should stream in multiple pieces, not all at once
   assert len(chunks) > 1
   
   # Test 2: Should contain expected story beginning
   assert "Once upon a time" in full_text
   
   # Test 3: Should have proper line breaks formatting
   assert full_text.count('\n') >= 3