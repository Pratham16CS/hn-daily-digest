import requests
import smtplib
import os
import datetime
from bs4 import BeautifulSoup as bs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def extract_news(url):
    print("Extracting Hacker News Stories....")
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = bs(response.content, 'html.parser')
    
    cnt = "<b>HN Top Stories:</b><br>" + "-"*50 + "<br>"
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        if tag.text != 'More':
            cnt += f"{i+1}: {tag.text}<br>"
    
    return cnt + "<br>----------<br><br>End of Message"

def send_email(content):
    now = datetime.datetime.now()
    # Ensure these are set in your environment variables
    from_addr = os.getenv("EMAIL_FROM")
    to_addr = os.getenv("EMAIL_TO")
    password = os.getenv("EMAIL_PASS")

    msg = MIMEMultipart()
    msg['Subject'] = f'Top News Stories HN [Automated email] {now.day}-{now.month}-{now.year}'
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg.attach(MIMEText(content, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587) # Adjust server as needed
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    content = extract_news('https://news.ycombinator.com/')
    send_email(content)
