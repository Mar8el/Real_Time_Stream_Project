Azure IoT Fleet Safety Analytics Project

In This Project I Designed and implemented a real-time IoT data pipeline using Azure Event Hub, Functions, Cosmos DB, Stream Analytics, ADLS Delta Lake, Databricks (Unity Catalog), and Synapse Analytics.

Workflow 
The PY code used for IoT simulator to stream telemetry (speed, tire pressure, coolant temp, seatbelt status) The data is being pushed directly to Azure Portal in Event Hub

Built Python-based IoT simulator to stream telemetry (speed, tire pressure, coolant temp, seatbelt status) at scale.

Developed Azure Function logic to validate and split events into good vs. flagged, ensuring immediate anomaly capture.

Integrated Cosmos DB for low-latency anomaly storage and Synapse for SQL-based analytics and reporting.

Leveraged Databricks to identify repeat offenders (drivers without seatbelts) by joining telemetry with driver master data.

Implemented Delta Lake on ADLS to enable reliable, open lakehouse storage with ACID compliance and schema evolution.

Applied Unity Catalog to enforce governance and data security across Databricks analytics.
