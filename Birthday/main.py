import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "dafadarts@gmail.com"
MY_PASSWORD = "a7U6+cbOc3+h7a"


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'],
                            msg=f"Subject: Happy Birthday\n\n{name}")


today = dt.datetime.now()
today_tuple = (today.month, today.day)
print(today_tuple)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        name = contents.replace("[NAME]", birthday_person['name'])
        send_mail()
