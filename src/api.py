import requests
from config import API_URL

def fetch_countries():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()