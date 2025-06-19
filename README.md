# 🧪 Blog Website Automated Testing

This repository contains automated test scripts for a Blog Website using **Selenium WebDriver** and **Pytest**. It includes UI validations, functional checks, and structured HTML test reports.

## ✅ Features

- Automated UI testing using **Selenium**
- Test execution and management via **Pytest**
- HTML reporting using **pytest-html**
- Easily maintainable page object structure

---

## 🛠️ Tech Stack

- Python 3.8+
- Selenium
- Pytest
- Pytest-HTML
- (Optional) Allure, Pytest-xdist for parallel testing

---

## 📂 Project Structure

```bash
blog-automation/
│
├── tests/
│   ├── test_home_page.py
│   ├── test_blog_details.py
│   └── ...
│
├── pages/
│   ├── base_page.py
│   ├── blog_page.py
│   ├── blog_details_page.py
|   ├── category_page.py
|   ├── contact_page.py
|   └── search_page.py
│
│── report.html
├── conftest.py
├── requirements.txt
└── README.md


