import logging
import json
import uuid
import azure.functions as func
from azure.cosmos import CosmosClient
from azure.eventhub import EventHubProducerClient, EventData


COSMOS_URL = "--"
COSMOS_KEY = "--"
DATABASE_NAME = "IOTAlert"
CONTAINER_NAME = "alertevents"


cosmos_client = CosmosClient(COSMOS_URL, COSMOS_KEY)
database = cosmos_client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)


GOOD_EH_CONN_STR = "--"
GOOD_EH_NAME = "goodevents"

# Initialize Event Hub producer
producer = EventHubProducerClient.from_connection_string(
    conn_str=GOOD_EH_CONN_STR,
    eventhub_name=GOOD_EH_NAME
)


app = func.FunctionApp()

@app.function_name(name="ValidateEvents")
@app.event_hub_message_trigger(
    arg_name="event",
    event_hub_name="iotevents",   # Input Event Hub
    connection="EVENT_HUB_CONN_STR"                  # Leave empty since we are hardcoding
)
def validate_events(event: func.EventHubEvent):
    body = event.get_body().decode("utf-8")
    try:
        data = json.loads(body)
    except json.JSONDecodeError as e:
        logging.error(f"❌ Failed to decode JSON: {e}")
        return

    if isinstance(data, list):
        for record in data:
            process_record(record)
    else:
        process_record(data)

def process_record(record):

    

    TirePressure = int(record.get("TirePressure", 0))


    Speed = int(record.get("Speed", 0))
    

    CoolantTemperature = int(record.get("CoolantTemperature", 0))

    if TirePressure > 35 or TirePressure < 25 or Speed > 75 or CoolantTemperature > 240:
        if "id" not in record:
            record["id"] = str(uuid.uuid4())
        try:
            container.create_item(record)
            logging.warning(f"🚩 Flagged event sent to CosmosDB: {record['id']}")
        except Exception as ex:
            logging.error(f"❌ Error writing to CosmosDB: {ex}")
    else:
        try:
            batch = producer.create_batch()
            batch.add(EventData(json.dumps(record)))
            producer.send_batch(batch)
            logging.info(f"✅ Good event sent to Event Hub: {record}")
        except Exception as ex:
            logging.error(f"❌ Error sending to Event Hub: {ex}")
