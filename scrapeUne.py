from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(1)
driver.get("https://handbook.une.edu.au/search")

unit_codes = []
descriptions = []
wait = WebDriverWait(driver, 20)


try:
    while True:
        # Wait for the unit links to be fully loaded
        course_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='result-item-title']/ancestor::a")))
        for element in course_elements:
            href = element.get_attribute('href')
            description = element.find_element(By.CLASS_NAME, 'result-item-title').text  # Assuming the description is directly in this span
            if href:
                unit_code = href.split('/')[-1]
                unit_codes.append(unit_code)
                descriptions.append(description)
                print(f"Unit Code: {unit_code}, Description: {description}")

        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for the 'Next' button to be clickable
        next_button = wait.until(EC.element_to_be_clickable((By.ID, 'pagination-page-next')))
        driver.execute_script("arguments[0].click();", next_button)

        # Wait for the page to update
        wait.until(EC.staleness_of(course_elements[0]))

except NoSuchElementException:
    print("Reached the last page.")
except TimeoutException:
    print("Failed to load a new page or no 'Next' button clickable.")

# Close the driver
driver.quit()

# Output the collected unit codes and descriptions to a text file
with open('unit_codes_and_descriptions.txt', 'w') as file:
    for code, desc in zip(unit_codes, descriptions):
        file.write(f"{code}: {desc}\n")

print("Collected unit codes and descriptions saved to file.")