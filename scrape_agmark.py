import time
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore

init(autoreset=True)

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def wait_for_option(driver, element_id, visible_text, timeout=20):
    def option_loaded(driver):
        try:
            dropdown = Select(driver.find_element(By.ID, element_id))
            return visible_text in [o.text.strip() for o in dropdown.options]
        except:
            return False
    WebDriverWait(driver, timeout).until(option_loaded)

def set_dropdown(driver, element_id, visible_text):
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        wait_for_option(driver, element_id, visible_text)
        dropdown = Select(driver.find_element(By.ID, element_id))
        dropdown.select_by_visible_text(visible_text)
        print(f"{Fore.GREEN}✅ Selected '{visible_text}' in '{element_id}'")
        time.sleep(1)
    except Exception as e:
        print(f"{Fore.RED}❌ Error selecting '{visible_text}' in dropdown '{element_id}': {e}")
        raise

def set_dates(driver, from_date, to_date):
    try:
        from_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtDate"))
        )
        to_input = driver.find_element(By.ID, "txtDateTo")
        driver.execute_script("arguments[0].value = arguments[1];", from_input, from_date)
        driver.execute_script("arguments[0].value = arguments[1];", to_input, to_date)
        print(f"{Fore.CYAN}📅 Dates set from {from_date} to {to_date}")
        time.sleep(1)
    except Exception as e:
        print(f"{Fore.RED}❌ Error setting dates: {e}")
        raise

def click_search(driver):
    try:
        go_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnGo"))
        )
        go_button.click()
        print(f"{Fore.YELLOW}🔍 Searching... please wait")
        time.sleep(4)
    except Exception as e:
        print(f"{Fore.RED}❌ Error clicking search button: {e}")
        raise

def extract_table(driver):
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "cphBody_paneltabular"))
        )

        if "No Records Found" in driver.page_source:
            print(f"{Fore.RED}❌ No records found.")
            return pd.DataFrame()

        table = driver.find_element(By.ID, "cphBody_GridPriceData")
        rows = table.find_elements(By.TAG_NAME, "tr")
        headers = [th.text.strip() for th in rows[0].find_elements(By.TAG_NAME, "th")]
        data = []
        for row in rows[1:]:
            cols = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
            if cols:
                data.append(cols)

        print(f"{Fore.GREEN}✅ Table extracted.")
        return pd.DataFrame(data, columns=headers)

    except Exception as e:
        print(f"{Fore.RED}⚠️ Error extracting table: {e}")
        return pd.DataFrame()

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name).replace(" ", "_")

def main():
    print(f"{Fore.CYAN}📥 Enter details to fetch Agmarknet data:")
    commodity = input("Commodity: ").strip()
    state = input("State: ").strip()
    district = input("District: ").strip()
    market = input("Market: ").strip()
    date_from = input("From Date (e.g. 01-Jan-2024): ").strip()
    date_to = input("To Date (e.g. 31-May-2024): ").strip()

    driver = init_driver()
    driver.get("https://agmarknet.gov.in/")

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ddlCommodity"))
        )

        set_dropdown(driver, "ddlCommodity", commodity)
        set_dropdown(driver, "ddlState", state)
        set_dropdown(driver, "ddlDistrict", district)
        set_dropdown(driver, "ddlMarket", market)
        set_dates(driver, date_from, date_to)
        click_search(driver)

        df = extract_table(driver)
        if not df.empty:
            filename = sanitize_filename(
                f"{commodity}_{district}_{market}_{date_from}_to_{date_to}.xlsx"
            )
            df.to_excel(filename, index=False)
            print(f"\n{Fore.GREEN}📁 Data saved to {filename}")
            print(df.head())
        else:
            print(f"\n{Fore.YELLOW}⚠️ No data extracted.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
