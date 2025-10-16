# #lab 3 subscriber
# import paho.mqtt.client as mqtt

# # ----- Callbacks -----
# def on_connect(client, userdata, flags, reason_code, properties):
#     print("Connection returned result:", reason_code)
#     # Subscribing in on_connect() means subscriptions are renewed after reconnect
#     client.subscribe("ece180d/team5", qos=1)

# def on_disconnect(client, userdata, disconnect_flags, reason_code, properties=None):
#     if rc != 0:
#         print("Unexpected Disconnect")
#     else:
#         print("Expected Disconnect")

# def on_message(client, userdata, message):
#     print(
#         f'Received message: "{message.payload.decode()}" '
#         f'on topic "{message.topic}" with QoS {message.qos}'
#     )

# # ----- Create and configure MQTT client -----
# client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

# # Attach callback functions
# client.on_connect = on_connect
# client.on_disconnect = on_disconnect
# client.on_message = on_message

# # ----- Connect to broker -----
# client.connect_async("test.mosquitto.org", 1883)

# # Start the network loop
# client.loop_forever()  # Keeps script running to receive messages

import paho.mqtt.client as mqtt


# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc, properties=None):
    print("Connection returned result: "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    
    client.subscribe("ece180d/test", qos=1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, disconnect_flags, rc, properties=None):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')


# The default message callback.
# (you can create separate callbacks per subscribed topic)
def on_message(client, userdata, message):
    print('Received message: "' + str(message.payload) + '" on topic "' + message.topic + '" with QoS ' + str(message.qos))


# 1. create a client instance.
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
# 2. connect to a broker using one of the connect*() functions.
client.connect_async('test.mosquitto.org')
# client.connect("mqtt.eclipse.org")


# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_forever()

# use subscribe() to subscribe to a topic and receive messages.
# use publish() to publish messages to the broker

# use disconnect() to disconnect from the broker.
client.disconnect()