MERGE seventh-odyssey-417615.INTEGRATION.integration_prueba_tecnica AS target
USING (
  SELECT
    name,
    url,
    DATE(TIMESTAMP(ingestion_date)) AS ingestion_day,
    CURRENT_TIMESTAMP() AS transformation_timestamp
  FROM (
    SELECT
      name,
      url,
      ingestion_date,
      ROW_NUMBER() OVER (
        PARTITION BY name, DATE(TIMESTAMP(ingestion_date))
        ORDER BY TIMESTAMP(ingestion_date) DESC
      ) AS row_num
    FROM seventh-odyssey-417615.SANDBOX_pokemon_api.pokemon_raw
  )
  WHERE row_num = 1
) AS source
ON target.name = source.name
AND target.ingestion_day = source.ingestion_day
WHEN NOT MATCHED THEN
  INSERT (
    name,
    url,
    ingestion_day,
    transformation_timestamp
  )
  VALUES (
    source.name,
    source.url,
    source.ingestion_day,
    source.transformation_timestamp
  );