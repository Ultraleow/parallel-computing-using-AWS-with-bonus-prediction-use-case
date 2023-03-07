#!/usr/bin/env python3
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import smtplib
import sys

email = 'demo.parallelc.2022@gmail.com'
email_pw = 'repq chbr xjqc fopb'
pw = "tafaubbkblbyrxxa"
email_title = "~~Prediction Result~~"


def send_email(send_to, df):
    send_from = email
    password = pw
    print(password)
    message = """\
    <p><strong>This is your result</strong></p>
    <p><br/></p>
    <p><strong>Greetings</strong><br/><strong>From us</strong></p>
    """

    multipart = MIMEMultipart()
    multipart["From"] = send_from
    multipart["To"] = send_to
    multipart["Subject"] = email_title
    attachment = MIMEApplication(df.to_csv())
    attachment["Content-Disposition"] = "attachment; filename={}".format(f"result.csv")
    multipart.attach(attachment)
    multipart.attach(MIMEText(message, "html"))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(multipart["From"], password)
    server.sendmail(multipart["From"], multipart["To"], multipart.as_string())
    server.quit()

args = sys.argv[1].split(";")
path = args[0]
input_path = args[0]
email_to = args[1]
csv_path = input_path+"/predicted_email.csv"
df = pd.read_csv(csv_path)
send_email(email_to, df)

# if __name__ == "__main__":
#     args = sys.argv[1].split(";")
#     path = args[0]
#     input_path = args[0]
#     email = args[1]
#     df = pd.read_csv("/home/ubuntu/src/shared/scripts/raw.csv")
#     send_email("ultraleow@gmail.com", df)