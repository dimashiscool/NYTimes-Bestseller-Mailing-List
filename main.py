from pynytimes import NYTAPI
import smtplib
from email.message import EmailMessage
import os

nyt = NYTAPI("uLxzNzkw1Y40BYcrOId3oeBzktuk1GOy", parse_dates=True)

EMAIL_ADDRESS = os.environ('EMAIL')
EMAIL_PASSWORD = os.environ('EMAIL_APP_PASSWORD')

# Get fiction best sellers list
books = nyt.best_sellers_list(
    name="Childrens Middle Grade Hardcover"
)

recipients = [EMAIL_ADDRESS, 'foo@bar.com']

msg = EmailMessage()
msg['Subject'] = 'New York Times Bestsellers'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ','.join(recipients)

books_list = []

for count, book in enumerate(books, 1):
    books_list.append(f"{count} {book['title']}")

str_book_list = str(books_list).replace('[', '').replace(']', '').replace("'", '').replace(',', '\n')

msg.set_content(str_book_list)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        smtp.quit()
