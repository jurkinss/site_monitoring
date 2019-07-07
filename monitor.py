import boto3
import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get
EMAIL_PASSWORD = os.environ.get
MY_EC2_INSTANCE_ID = os.environ.get

def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'YOUR site is down!'
        body = 'Say Hi to Karlis :))))'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, 'kinss@gmail.com', msg)     #enter correct email
        print('I have sent email')


def reboot_ec2(ec2_instance_id):
    client = boto3.client('ec2')
    response = client.reboot_instances(InstanceIds=[ec2_instance_id],
    DryRun=False)                                      # change to false to usd)
    return response


try:
    r=requests.get('http://52.56.211.00/', timeout=5)

    if r.status_code != 200:
        notify_user()                                  
        reboot_ec2(MY_EC2_INSTANCE_ID)
        print(reboot_ec2(MY_EC2_INSTANCE_ID))
except Exception as e:
    notify_user()
    reboot_ec2(MY_EC2_INSTANCE_ID)
    print(reboot_ec2(MY_EC2_INSTANCE_ID))


