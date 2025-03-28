# Python Flask Interview Exercise
**Welcome** to this technical interview. We will step through the exercises together - slowly.

The point is to collaborate and communicate your line of thought. It is perfectly OK to ask questions. Just like if you got this task at work.

## Set up
```bash
pip install uv
```

## Starting the app
```bash
uv run flask --app app.py run --debug
```

## Running the tests

(this will fail by the way)
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

### Fix the Dockerfile
- Review the provided Dockerfile
- Build the image

### Finish up
 - commit your changes with a descriptive message


## Questions

- How would you improve the test coverage?
- What security considerations should we think about?
- How would you document this API?
- How would you monitor streaming connections in production?
- How would Docker fit in to this?
