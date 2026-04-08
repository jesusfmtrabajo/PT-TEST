# Prueba Técnica - Mini Proyecto de Pipeline de Datos

Repositorio para la prueba técnica de pipeline de datos.

## Estructura
- src/: scripts Python
- sql/: consultas SQL de transformación
- airflow/: DAG y operadores de Airflow

## Pipeline

1. Extracción desde PokeAPI
2. Carga en BigQuery (SANDBOX)
3. Transformación SQL idempotente hacia capa integration

## ¿Qué es un Hook? ¿En qué se diferencia de una conexión?
Una conexión en Airflow almacena las credenciales o configuración necesarias para acceder a un servicio externo.
Puede ser de dos tipos:
- **`google_cloud_default`**:  
  No tiene credenciales explícitas. Delega la autenticación en la Service Account del entorno (por ejemplo, en GCP).
- **`Conexión creada manualmente`**:  
  Contiene credenciales explícitas (como JSON de una Service Account, usuario/contraseña, etc.), normalmente usadas para acceder a proyectos o entornos específicos.
  
Un Hook es el componente que utiliza una conexión para interactuar con un servicio.

Por ejemplo,
```python
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook

# Usando la conexión por defecto del entorno
client = BigQueryHook(gcp_conn_id="google_cloud_default").get_client()

query_job = client.query("SELECT * FROM tabla")
results = query_job.result()
```
