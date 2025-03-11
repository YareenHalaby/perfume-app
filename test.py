import pytest
import requests

# URL of your backend API
API_URL = "http://localhost:8000/perfumes"

# Sample data to send in the test
new_perfume = {
    "name": "Floral Perfume",
    "brand": "Flora",
    "image_url": "https://example.com/image.jpg",
    "buy_url": "https://example.com/buy",
    "fragrance_notes": "Rose, Jasmine, Vanilla",
    "price": 50,
    "volume": 100,
    "scentIds": [1, 2, 3]
}

def test_create_perfume():
    response = requests.post(API_URL, json=new_perfume)
    
    assert response.status_code == 200
    
    # Check if the response contains the correct data
    response_data = response.json()
    assert response_data["name"] == new_perfume["name"]
    assert response_data["brand"] == new_perfume["brand"]
    assert response_data["image_url"] == new_perfume["image_url"]
    assert response_data["buy_url"] == new_perfume["buy_url"]
    assert response_data["fragrance_notes"] == new_perfume["fragrance_notes"]
    assert response_data["price"] == new_perfume["price"]
    assert response_data["volume"] == new_perfume["volume"]
    assert response_data["scentIds"] == new_perfume["scentIds"]

# Running the test
if __name__ == "__main__":
    pytest.main()
