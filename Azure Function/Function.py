import logging
import json
import uuid
import azure.functions as func
from azure.cosmos import CosmosClient
from azure.eventhub import EventHubProducerClient, EventData

COSMOS_URL = "--"
COSMOS_KEY = "--"
DATABASE_NAME = "--" 
CONTAINER_NAME = "--"

cosmos_client = CosmosClient(COSMOS_URL, COSMOS_KEY)
database = 
