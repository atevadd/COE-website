import smtplib

email = 'coe.rccg@gmail.com'
password = 'coerccg1234'


def mailer(name, request):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)

        subject = 'A request from the website'
        body = f"Name: {name} \n PrayerRequest: {request}"

        msg = f"Subject: {subject} \n\n {body}"

        smtp.sendmail('Thewebsite@gmail.com', email, msg)

        print("Email sent sucessfully")