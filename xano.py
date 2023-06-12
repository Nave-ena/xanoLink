import smtplib
import ssl
import os
import requests
import json

def send_email():
    port = 465
    smtp_server = "smtp.gmail.com"
    user_email = os.environ.get("USER_EMAIL")
    user_password = os.environ.get("USER_PASSWORD")
    receiver = os.environ.get("RECEIVER")

    message = """   
    Subject: Welcome 

    This is your welcome email running 
    """

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(user_email, user_password)
        server.sendmail(user_email, receiver, message)

def get_data():
    url = "https://x8ki-letl-twmt.n7.xano.io/api:GSAwrAoy:v1/links/get/today"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        summary = data["summary"]
        text = data["link"]
        print("Summary:", summary)
        print("Text:", text)
    else:
        print("Error occurred with status code:", response.status_code)

# Call the functions
send_email()
get_data()
