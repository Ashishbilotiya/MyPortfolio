from flask import render_template, Blueprint, request, redirect, url_for, flash
import os
import requests
from dotenv import load_dotenv


load_dotenv()

home_page = Blueprint("home", __name__)

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")

def send_email(name, email, message):
    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": "myportfolioapp",
            "email": EMAIL_SENDER
        },
        "to": [
            {
                "email": EMAIL_RECEIVER,
                "name": "Ashish"
            }
        ],
        "subject": "New Portfolio Contact Message",
        "htmlContent": f"""
        <h3>New Contact Message</h3>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Message:</strong><br>{message}</p>
        """
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code not in [200, 201, 202]:
        raise Exception(response.text)


@home_page.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if name and email and message:
            try:
                send_email(name, email, message)
                flash("Message sent successfully! 🚀", "success")
            except Exception as e:
                flash("Error! Message could not be sent.", "danger")
                print(e)

            return redirect(url_for("home.home", _anchor="contact"))

    return render_template("home/home.html")



