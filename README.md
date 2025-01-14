# Python Flask Interview Exercise

Welcome! This is a small Flask application with two main tasks to work on during our 20-minute pair programming session.

## Starting the app
```bash
uv run flask --app app.py run --debug
```


## Running the tests
```bash
uv run pytest
```


## Tasks

### Create your branch
 - create a branch to work on with your name as the branch name


### Implement Login Authentication

- Complete the /api/login endpoint
- Think about error cases
- Review the test coverage - what's missing?


### Implement Story Streaming

- Complete the /api/stream-story endpoint
- Test manually using: curl http://localhost:5000/api/stream-story
- Discuss scalability considerations

### Finish up
 - commit your changes with a descriptive message


## Questions

- How would you improve the test coverage?
- What security considerations should we think about?
- How would you document this API?
- How would you monitor streaming connections in production?