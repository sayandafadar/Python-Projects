import random
import datetime as dt
import smtplib

MY_EMAIL = "dafadarts@gmail.com"
MY_PASSWORD = "a7U6+cbOc3+h7a"

omi_quotes = [
    '''“When you arise in the morning think of what a privilege it is to be alive, to think, to enjoy, to love…” – 
    Marcus Aurelius''',
    '''“Either you run the day or the day runs you.”– Jim Rohn''',
    '''“Mondays are the start of the work week which offer new beginnings 52 times a year!“– David Dweck''',
    '''“You've got to get up every morning with determination if you're going to go to bed with satisfaction.”– 
    George Lorimer''',
    '''“Be miserable. Or motivate yourself. Whatever has to be done, it's always your choice.”– Wayne Dyer''',
    '''“Your Monday morning thoughts set the tone for your whole week. See yourself getting stronger, and living a 
fulfilling, happier & healthier life.”– Germany Kent''',
    '''“You don’t have to be great to start, but you have to start to be great.”– Zig Ziglar''']

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    quote = random.choice(omi_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="dafadarts@yahoo.com",
                            msg=quote
                            )

