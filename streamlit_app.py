import streamlit as st
import paho.mqtt.client as mqtt

# MQTT Broker details
MQTT_BROKER = "0.tcp.in.ngrok.io"  # Replace with your ngrok public address
MQTT_PORT = 12493                 # Replace with your ngrok port
MQTT_TOPIC = "test/topic"         # Topic to publish to

# MQTT Publisher function
def publish_message(message):
    try:
        client = mqtt.Client()  # Ensure no outdated API options are used
        client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
        client.loop_start()  # Explicitly start the loop
        client.publish(MQTT_TOPIC, payload=message, qos=1)
        client.loop_stop()  # Stop the loop after publishing
        client.disconnect()
        st.success(f"Message '{message}' sent successfully!")
    except Exception as e:
        st.error(f"Failed to send message: {str(e)}")

# Streamlit interface
st.title("Animal Detection System")
st.write("Press the button below to simulate animal detection.")

if st.button("Detect Animal"):
    publish_message("on")  # Send "on" message to activate the buzzer

if st.button("Turn Off"):
    publish_message("off")  # Send "off" message to deactivate the buzzer
