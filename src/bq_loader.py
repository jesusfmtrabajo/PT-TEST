from google.cloud import bigquery


class BigQueryLoader:
    def __init__(self, project_id, dataset_id, table_id):
        self.client = bigquery.Client(project=project_id)
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.table_ref = f"{self.project_id}.{self.dataset_id}.{self.table_id}"

    def create_table_if_not_exists(self):
        schema = [
            bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("url", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("ingestion_date", "TIMESTAMP", mode="REQUIRED"),
        ]

        table = bigquery.Table(self.table_ref, schema=schema)
        self.client.create_table(table, exists_ok=True)
        print(f"Table ready: {self.table_ref}")

    def load_data(self, rows):
        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND
        )

        job = self.client.load_table_from_json(
            rows,
            self.table_ref,
            job_config=job_config
        )

        job.result()
        print(f"Inserted {len(rows)} rows into {self.table_ref}")