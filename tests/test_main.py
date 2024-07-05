import json
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_location():
    response = client.post(
        "/locations/",
        json={"latitude": 40.712776, "longitude": -74.005974}
    )
    assert response.status_code == 200
    assert response.json()["latitude"] == 40.712776
    assert response.json()["longitude"] == -74.005974

def test_create_category():
    response = client.post(
        "/categories/",
        json={"name": "Restaurant"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Restaurant"

def test_get_locations():
    response = client.get("/locations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_categories():
    response = client.get("/categories/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_location_category_review():
    location_response = client.post(
        "/locations/",
        json={"latitude": 40.712776, "longitude": -74.005974}
    )
    category_response = client.post(
        "/categories/",
        json={"name": "Restaurant"}
    )

    location_id = location_response.json()["id"]
    category_id = category_response.json()["id"]

    response = client.post(
        "/reviews/",
        json={
            "location_id": location_id,
            "category_id": category_id,
            "last_reviewed": "2023-07-01T12:00:00"
        }
    )
    assert response.status_code == 200
    assert response.json()["location_id"] == location_id
    assert response.json()["category_id"] == category_id
    assert response.json()["last_reviewed"] == "2023-07-01T12:00:00"

def test_get_recommendations():
    response = client.get("/recommendations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
