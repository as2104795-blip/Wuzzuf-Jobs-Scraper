# Wuzzuf Python Jobs Scraper 🚀

An automated Python tool specifically designed to search for and scrape **Python-related job postings** from **Wuzzuf** using **Selenium** and **Pandas**.

## 🌟 Features
- **Customizable Page Extraction:** The script asks the user to enter the specific number of pages they want to extract dynamically.
- **Targeted Search:** Automatically filters and extracts jobs tailored for **Python Developers / Data Scientists / AI Engineers**.
- **Auto-Scrolling:** Simulates human behavior to ensure all dynamic elements are fully loaded on each page.
- **Clean Excel Output:** Exports directly into a `.xlsx` file with fully active, clickable links using **xlsxwriter**.

## 🛠️ Tech Stack
- **Python 3.13**
- **Selenium WebDriver**
- **Pandas & XlsxWriter**

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install selenium pandas xlsxwriter
2. Run the script:
   ```bash
   python wuzzuf.py

3. Enter the number of pages you wish to scrape when prompted in the terminal.


4. ## 📊 Sample Output
Here is a preview of how the extracted data looks inside the generated Excel file:

| Job Title | Company Name | Location | Job Type | Date Posted |link
| :--- | :--- | :--- | :--- | :--- |

| Python Developer | Cairo Team - | New Cairo, Cairo | Full Time | 2 days ago |

| Data Analyst (Python) | Tech Corp - | Maadi, Cairo | Remote | 1 week ago |

| Backend Engineer | Software Solutions - | Alexandria | Hybrid | 5 hours ago |

*Note: The generated file also includes direct, clickable links to each job listing on Wuzzuf.*
