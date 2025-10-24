from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"

def test_get_course_by_id_success():
    resp = client.get("/api/courses/COURSE-123")
    assert resp.status_code == 200
    body = resp.json()
    assert list(body.keys()) == ["course_id"]
    assert body["course_id"] == "COURSE-123"

def test_get_course_by_id_normalization():
    resp = client.get("/api/courses/   course  123   ")
    assert resp.status_code == 200
    assert resp.json()["course_id"] == "course-123"

def test_get_course_by_id_invalid():
    resp = client.get("/api/courses/!!bad!!")
    assert resp.status_code == 400
