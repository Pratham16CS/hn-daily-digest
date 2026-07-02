# Hacker News Daily Scraper & Emailer

A lightweight Python script that scrapes the top stories from Hacker News [Hacker News](https://news.ycombinator.com/) and automatically delivers them to your inbox as a clean, formatted HTML email. 

---

## 🚀 Features

* **Web Scraping:** Parses the front page of Hacker News using `BeautifulSoup4`.
* **HTML Emails:** Formats the scraped stories into a readable list before sending.
* **Secure Credentials:** Utilizes `python-dotenv` to keep your email credentials safe and separate from the source code.
* **Timestamped Subjects:** Automatically appends the current date to the email subject line.

---

## 🛠️ Prerequisites

Make sure you have Python 3.x installed on your system. 

If you plan to use Gmail (which the script is configured for by default), you will need to generate an **App Password** rather than using your regular login password. 
* Go to your Google Account -> Security -> 2-Step Verification -> App passwords.

---

## 📦 Installation & Setup

1. **Clone or download this repository** to your local machine.

2. **Install the required dependencies** using pip:
```bash
   pip install -r requirements.txt
```
3. **Configure Environment Variables:**
Create a file named `.env` in the root directory of the project and add your configuration details:
```env
EMAIL_FROM=your_sender_email@gmail.com
EMAIL_TO=your_recipient_email@example.com
EMAIL_PASS=your_gmail_app_password

```



---

## ⚙️ How It Works

* `extract_news(url)`: Sends a request to Hacker News, parses the HTML structure to extract story titles, and bundles them into an HTML string.
* `send_email(content)`: Fetches configuration details from the `.env` file, establishes a secure TLS connection with the Gmail SMTP server, and shoots the structured email over to the designated recipient.

---

## 🏃‍♂️ Running the Script

Execute the script from your terminal:

```bash
python main.py

```

*Note: Replace `main.py` with whatever you named your Python file.*

---

## 🔧 Customization

If you are using an email provider other than Gmail, open the script and update the SMTP settings in the `send_email` function:

```python
# For example, Outlook/Hotmail configuration:
server = smtplib.SMTP('smtp-mail.outlook.com', 587)

```
