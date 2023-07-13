from twilio.rest import Client

# Twilio account SID and auth token
account_sid = 'AC19d16e346c487738957ac0c251305aa2'
auth_token = '6f4ca12a3ba72f89cbe61d1e166b0f91'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Sending an SMS message
def send_sms(to_number, from_number, message):
    try:
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print("Message sent successfully!")
        print("Message SID:", message.sid)
    except Exception as e:
        print("Error:", str(e))

# Main program
if __name__ == "__main__":
    # Phone numbers
    to_number = '+18622687540'  # Replace with the destination phone number
    from_number = '+18336391244'  # Replace with your Twilio phone number
    
    # Message content
    message = "Hello from Twilio!"

    # Send the SMS message
    send_sms(to_number, from_number, message)