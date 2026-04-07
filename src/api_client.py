import requests
from datetime import datetime, timezone


class ApiClient:
    def __init__(self, url):
        self.url = url

    def fetch_data(self, limit=100):
        response = requests.get(f"{self.url}?limit={limit}")
        response.raise_for_status()
        data = response.json()["results"]

        ingestion_date = datetime.now(timezone.utc).isoformat()

        for item in data:
            item["ingestion_date"] = ingestion_date

        return data


if __name__ == "__main__":
    url = "https://pokeapi.co/api/v2/pokemon"
    client = ApiClient(url)

    data = client.fetch_data()

    print(f"Downloaded {len(data)} records")
    print(data[:2])