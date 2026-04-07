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