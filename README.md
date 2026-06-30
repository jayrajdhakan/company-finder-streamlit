# Company Finder

A Streamlit web application that scrapes company details from **Google Maps** based on a selected **city** and **company type**, then displays results and allows exporting to an Excel file.

> Built with Selenium (headless Chrome) + Pandas. Data is exported as `.xlsx`.

---

## Features
- Select a **City** (Gujarat locations)
- Select a **Company Type** (e.g., IT, Automobile, Pharmacy, etc.)
- Click **Find Companies** to scrape matching results
- View company list with:
  - Company Name
  - Address
  - Phone
  - Google Maps link
- Export scraped results to **Excel**

---

## Tech Stack
- **Python**
- **Streamlit** (UI)
- **Selenium** (web automation / scraping)
- **webdriver-manager** (auto-downloads ChromeDriver)
- **Pandas** (data handling)
- **openpyxl** (Excel export)

---

## Project Structure
```text
.
├── app.py
├── requirements.txt
├── config/
│   └── data.py
└── scraper/
    ├── __init__.py
    └── selenium_scraper.py
```
- `app.py`: Streamlit UI (dropdowns, results display, Excel export)
- `config/data.py`: Source lists for `cities` and `company_types`
- `scraper/selenium_scraper.py`: Selenium scraping implementation

---

## Setup

### 1) Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

---

## Run the Application
```bash
streamlit run app.py
```

Then open the URL shown in the terminal (typically `http://localhost:8501`).

---

## How to Use
1. Select a **City** from the dropdown.
2. Select a **Company Type** from the dropdown.
3. Click **Find Companies**.
4. The app will scrape results and display:
   - Company Name
   - Address
   - Phone
   - Link to open in Google Maps
5. Click **Export to Excel** to download `companies.xlsx`.

---

## Output Format
The scraper returns a Pandas DataFrame with the following columns:
- `City`
- `Company Type`
- `Company Name`
- `Address`
- `Phone`
- `Google Maps Link`

---

## Notes / Limitations
- Google Maps pages can change frequently; selector/XPath changes may be required over time.
- Scraping results depend on dynamic content loading and scrolling.
- If Google Maps blocks automation or changes HTML structure, scraping may return incomplete data.
- The scraper uses **headless** Chrome; for debugging, you may remove `--headless` in the Selenium options.

---

## Troubleshooting
- **ChromeDriver / Selenium issues**: Ensure you have Google Chrome installed. `webdriver-manager` will handle driver installation.
- **Empty results / missing fields**:
  - Try again (sometimes Google Maps loads slower).
  - Ensure correct city/type selection.
  - If errors occur, inspect Selenium element locators in `scraper/selenium_scraper.py`.

---

## Disclaimer
This project automates interaction with Google Maps to collect publicly displayed information. Use responsibly and comply with applicable terms, policies, and local regulations.

