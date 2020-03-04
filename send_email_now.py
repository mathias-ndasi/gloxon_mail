"""
Don't forget to setup your config.py file with valid credentials

Also, remember to sent recipient email address in the send_mail function below. But by default you will be prompted to enter recipient email on the console

"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, datetime, os, jinja2

from config import Config


def render_template(template, **kwargs):
    templateLoader = jinja2.FileSystemLoader(os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'templates'))
    templateEnv = jinja2.Environment(loader=templateLoader)
    templ = templateEnv.get_template(template)
    return templ.render(**kwargs)


def send_mail(bodyContent, subject):
    port = Config.MAIL_PORT
    smtp_server = Config.MAIL_SERVER
    sender_email = Config.MAIL_USERNAME
    recipient = input("Enter recipient email:  ")
    password = Config.MAIL_PASSWORD

    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient
    message.attach(MIMEText(bodyContent, "html"))

    server = smtplib.SMTP_SSL(smtp_server, port)
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient, message.as_string())
    server.quit()


if __name__ == "__main__":
    """
    Two html templates are found in the template folder for the two designs.
    Context can be passed down to the varios templates in the render_template function below...
    
    """
    
    # html = render_template("gloxon_app_access.html", current_year=f"{datetime.date.today().year}")
    html = render_template("gloxon_confirm_account.html",
                           current_year=f"{datetime.date.today().year}")
    send_mail(bodyContent=html, subject="Gloxon Account Confirmation")
    print("Mail sent successfully.")
