from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def scrape_companies(city, company_type):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    wait = WebDriverWait(driver, 10)

    query = f"{company_type} in {city}"
    url = f"https://www.google.com/maps/search/{query}"

    driver.get(url)
    time.sleep(5)

    scrollable_div = driver.find_element(By.CSS_SELECTOR, "div[role='feed']")

    for _ in range(5):   # scroll multiple times
        driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight",
        scrollable_div
    )
    time.sleep(2)

    companies = []

    results = driver.find_elements(By.CLASS_NAME, "hfpxzc")

    for r in results[:50]:

        try:
            r.click()

            # wait for company name to load
            name = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "DUwDvf"))
            ).text

            # address
            try:
                address = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//div[contains(@class,'Io6YTe')]")
                    )
                ).text
                address = address.encode("ascii", "ignore").decode()
            except:
                address = "Not Available"

            # phone
            try:
                phone = wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '[data-item-id^="phone"]')

                    )
                ).text
                phone = phone.encode("ascii", "ignore").decode()
            except:
                phone = "Not Available"

            maps_link = driver.current_url

            companies.append({
                "City": city,
                "Company Type": company_type,
                "Company Name": name,
                "Address": address,
                "Phone": phone,
                "Google Maps Link": maps_link
            })

        except:
            continue

    driver.quit()

    df = pd.DataFrame(companies)

# Remove duplicates
    df = df.drop_duplicates(subset=["Company Name", "Address"])

    return df