import time
from paho.mqtt import client as mqtt_client
# Import library 'platform'
broker = 'broker.emqx.io'
port = 1883
topic = "topicName/weather"
client_id = 'iot'
username = 'test'
password = ''

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

def publish(client):
    # Define publish() function
    my_system = platform.uname()
    system = "OS:"+ my_system.system
    system_name = 'Sys Name:' + my_system.node
    system_prcessor = 'Sys Name:' + my_system.node
    client.publish(topic,system)
    print(system)
    time.sleep(7)
    client.publish(system_name,system_prcessor)
    print(system)
    time.sleep(7)


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()