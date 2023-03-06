from csv_mqtt.csv_mqtt import CsvMqtt
connector = CsvMqtt("broker.emqx.io")
connector.publish_csv_data("./final.csv", "shafina")
