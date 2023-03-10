import paho.mqtt.client as mqtt
import datetime
from pymongo import MongoClient
from rtrt import *

client = mqtt.Client()
client.connect("broker.emqx.io", 1883, 60)
client.subscribe("shafina")
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

