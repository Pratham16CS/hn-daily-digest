# HN Daily Digest Automator

A lightweight, automated Python script that scrapes the top stories from [Hacker News](https://news.ycombinator.com/), formats them into a clean HTML digest, and dispatches them directly to your inbox via SMTP.

This repository serves as a practical demonstration of core backend utilities: web scraping, HTML formatting, and secure communication pipelines.

---

## 🚀 Features

* **Web Scraping:** Parses the front page of Hacker News efficiently using `BeautifulSoup4`.
* **HTML Content Pipeline:** Dynamically generates a clean, readable HTML email body with the day's headlines.
* **Secure Credential Injection:** Decouples secrets from source code by pulling credentials strictly from environment variables via `python-dotenv`.
* **Robust Delivery:** Leverages Python's native `smtplib` combined with TLS encryption for secure email transport.
* **Single-File Execution:** Built with an `if __name__ == "__main__":` entry point, making it highly portable and modular.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Libraries:**
  * `requests` - For handling HTTP GET requests.
  * `beautifulsoup4` - For parsing and extracting HTML elements.
  * `python-dotenv` - For loading environment configurations.
  * `smtplib` & `email` - For composing and transmitting multi-part MIME emails.

---

## ⚙️ Installation & Configuration

Follow these steps to set up and run the script locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/hn-daily-digest.git](https://github.com/your-username/hn-daily-digest.git)
cd hn-daily-digest
