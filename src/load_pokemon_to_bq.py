from api_client import ApiClient
from bq_loader import BigQueryLoader


def main():
    project_id = "seventh-odyssey-417615"
    dataset_id = "SANDBOX_pokemon_api"
    table_id = "pokemon_raw"

    api_client = ApiClient("https://pokeapi.co/api/v2/pokemon")
    data = api_client.fetch_data(limit=100)

    bq_loader = BigQueryLoader(project_id, dataset_id, table_id)
    bq_loader.create_table_if_not_exists()
    bq_loader.load_data(data)


if __name__ == "__main__":
    main()