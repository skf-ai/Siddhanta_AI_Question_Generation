# Course API: A Beginner's Guide

This project is a minimal web service built with FastAPI. Its main purpose is to provide an API endpoint that takes a `course_id` and returns it in a structured JSON format. It's a great example for learning the fundamentals of building APIs in Python.

## Core Concepts for New Programmers

Understanding these concepts is key to understanding how this project works.

### FastAPI: The Web Framework

- **What it is:** FastAPI is the Python library we use to build the API. A "web framework" gives you tools to handle web requests and send back responses, so you don't have to build everything from scratch.
- **In this project:** We use FastAPI to create our endpoints (the URLs you can visit) and to manage incoming data. You can see the main FastAPI app object created in `app/main.py`.

### Uvicorn: The Server

- **What it is:** Uvicorn is a "web server." While FastAPI defines *what* the API does, Uvicorn is what actually *runs* it and makes it accessible on your network (like `http://127.0.0.1:8000`).
- **How we use it:** We run the command `uvicorn app.main:app` to tell Uvicorn to start running the `app` object located in our `app/main.py` file.

### Pydantic: Data Validation & Schemas

- **What it is:** Pydantic is a library for data validation. It lets us define the "shape" of our data using classes called "models."
- **In this project:** We use it in `app/models/course.py` to define `CourseIdResponse`. This model tells FastAPI that the response for a course request *must* be a JSON object with a single field: `course_id`, which must be a string. This prevents bugs and makes the API predictable.

### Project Structure: Keeping Code Organized

A clean folder structure is important. Here's what ours means:

- **`app/`**: The main application code.
  - **`main.py`**: The entry point of our app. It creates the FastAPI instance and includes the API routes.
  - **`api/`**: Holds the API logic.
    - **`routes.py`**: Contains the functions for our API endpoints, like `get_course_by_id`.
  - **`models/`**: Where we define our Pydantic data schemas.
    - **`course.py`**: Defines the `CourseIdResponse` model.
  - **`utilities/`**: Contains helper functions that can be used anywhere.
    - **`helpers.py`**: Includes functions for validating and cleaning up the `course_id`.
- **`tests/`**: Contains tests to verify our code works as expected.
  - **`test_course_api.py`**: Tests our API endpoints to make sure they return the correct data and status codes.

## How to Run Locally

Follow these steps to run the project on your own machine.

1.  **Create & Activate a Virtual Environment:**
    A "virtual environment" is an isolated space for a Python project's dependencies. This prevents conflicts between projects.

    ```bash
    # Create the environment folder (named .venv)
    python -m venv .venv

    # Activate it (the command differs by OS)
    # Windows:
    .venv\Scripts\activate
    # Unix/Mac:
    source .venv/bin/activate
    ```

2.  **Install Dependencies:**
    The `requirements.txt` file lists all the Python packages this project needs.

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Development Server:**
    This command tells Uvicorn to start the server. The `--reload` flag makes the server restart automatically when you change the code.

    ```bash
    uvicorn app.main:app --reload
    ```
    You can now access the API at `http://127.0.0.1:8000`.

## Understanding the Endpoints

An "endpoint" is a specific URL on our server that performs an action.

- **`GET /`**
  - **Purpose:** A simple health check to see if the service is running.
  - **Response:** `{"status": "ok", "service": "course-api", "version": "0.1.0"}`

- **`GET /api/courses/{course_id}`**
  - **Purpose:** The main endpoint. It takes a course ID from the URL and returns it.
  - **`{course_id}`** is a "path parameter"—it's a variable part of the URL.
  - **Response:** `{"course_id": "YOUR-ID-HERE"}`

## Running the Tests

Tests are crucial for making sure the code is reliable. We use `pytest` to run them.

```bash
# Install pytest if you haven't already
python -m pip install pytest

# Run the tests (in quiet mode)
pytest -q
```

## Example Requests

You can use a tool like `curl` or just your web browser to interact with the running API.

```bash
# Check service status
curl http://127.0.0.1:8000/

# Get a course by ID
curl http://127.0.0.1:8000/api/courses/COURSE-123
```