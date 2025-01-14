import json
from app import app


def test_login_endpoint():
    client = app.test_client()
    response = client.post('/api/login', 
        json={"username": "user", "password": "pass"})
    assert response.status_code == 200


def test_stream_endpoint():
    client = app.test_client()
    response = client.get('/api/stream-story')
    assert response.status_code == 200
    
    # Collect the streaming response
    chunks = []
    for chunk in response.response:
        chunks.append(chunk.decode('utf-8'))
    
    # Verify stream content
    full_text = ''.join(chunks)
    assert len(chunks) > 1  # Should have received multiple chunks
    assert "Once upon a time" in full_text  # Should contain start of story
    assert full_text.count('\n') >= 3  # Should have multiple lines
