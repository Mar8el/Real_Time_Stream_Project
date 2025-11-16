import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, timezone
import random
import json
import pytz

from config import EVENT_HUB_CONNECTION_STR, EVENT_HUB_NAME

from azure.eventhub import EventHubProducerClient, EventData

def generate_random_data() -> pd.DataFrame:
    num_rows = 8
    print(f"Generating {num_rows} rows of random data...")

    Vehicle_ID = ['001', '002', '003', '004', '005', '006', '007', '008']
    Buckled = ['Yes', 'No']


    utc_now = datetime.now(timezone.utc)
    eastern_timezone = pytz.timezone('America/New_York')

    data = {
        'EventTime': [utc_now.astimezone(eastern_timezone).strftime('%H%M%S')] * num_rows,
        'VehicleID': np.random.choice(Vehicle_ID, size=num_rows),
        'Buckled': np.random.choice(Buckled, size=num_rows),
        'TirePressure': np.random.randint(25, 38, size=num_rows),
        'Speed': np.random.randint(70, 76, size=num_rows),
        'CoolantTemperature': np.random.randint(230, 243, size=num_rows),
    }
    df = pd.DataFrame(data)
    print("Data generation complete.")
    return df

def send_to_event_hub(connection_str: str, eventhub_name: str, data_df: pd.DataFrame):

    producer = None
    try:

        producer = EventHubProducerClient.from_connection_string(
            conn_str=connection_str,
            eventhub_name=eventhub_name
        )


        json_data = data_df.to_json(orient='records')
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData(json_data))

        print(f"Sending data to Event Hub '{eventhub_name}'...")
        producer.send_batch(event_data_batch)
        print("✅ Data sent to Event Hub successfully!")
    except Exception as e:
        print(f"❌ An error occurred during Event Hub send: {e}")
    finally:
        if producer:
            producer.close()
            print("Event Hub producer closed.")

def main():

    

    iot_df = generate_random_data()
    

    send_to_event_hub(EVENT_HUB_CONNECTION_STR, EVENT_HUB_NAME, iot_df)

    print("\nGenerated Data:")
    print(iot_df)
        
if __name__ == "__main__":
    main()  
