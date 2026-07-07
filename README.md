# 📚 DarkLibrary: 3D Web-Scraped Digital Library

Welcome to **DarkLibrary**, an open-source online platform designed for reading books for free and staying updated with live global news. The platform features a unique modern dark theme integrated with an interactive 3D environment.

---

## 🌟 Key Features

* **3D Visual Experience:** Immersive frontend featuring an interactive 3D rotating Earth animation powered by **Three.js**.
* **Live News Scraping:** Automatically fetches current, real-time updates and news articles directly into the dashboard using **BeautifulSoup**.
* **Data-Efficient Links:** Uses direct external book links instead of hosting massive files, drastically reducing server database load and improving load speeds.
* **Modern Dark UI:** A fully optimized, sleek, and dark-themed interface built using Bootstrap for clean scannability.
* **Public Library System:** Standard authorization is configured so that any visiting user can freely read books and add new items to their collection.

---

## 🔐 Admin & Superuser Credentials

For demonstration and testing purposes, a fixed Admin login bypass is hardcoded into the system alongside standard Django authentication.

* **Default Admin Username:** `Book`
* **Default Admin Password:** `1234`

> **Note:** To manage the database dynamically or add core book data from the backend, you can generate your own custom superuser account linked with MySQL.

---

## 🛠️ Installation & Setup Guide

Since there is no preset `requirements.txt` file, follow these steps to install all required Python libraries and launch the project locally.

### 1. Install Required Libraries
Open your terminal inside your project directory (with your virtual environment activated) and run the following commands:

```bash
# Install Django framework
pip install django

# Install Web Scraping tools
pip install requests beautifulsoup4

# Install Pillow for handling Book Cover Images
pip install pillow

# Install MySQL connector (If connecting to a MySQL Database)
pip install mysqlclient
