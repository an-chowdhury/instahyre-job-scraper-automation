from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
import time
import getpass

email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")

login_url = "https://www.instahyre.com/login/"

target_url = "https://www.instahyre.com/candidate/opportunities/?matching=true&status=1"

def get_job_details():


    jobs = driver.find_elements(By.CLASS_NAME, "employer-row")

    for job in jobs:

        buttons = job.find_elements(By.TAG_NAME, "button")

        
        driver.execute_script("arguments[0].click();", job.find_element(By.ID, "interested-btn"))
        time.sleep(5) 
        

        modal = driver.find_element(By.CLASS_NAME, "application-modal-wrap")
            
        # Company name
        company = modal.find_element(By.CLASS_NAME, "profile-info").find_element(By.CSS_SELECTOR, ".company-name.ng-binding").text
        
        # Company Summary
        summary_element = modal.find_element(By.XPATH, "//div[@id='employer-summary']//p")
        company_summary = summary_element.text

        # Job Role
        role = modal.find_element(By.CLASS_NAME, "profile-info").find_element(By.CSS_SELECTOR, ".ng-binding").text
        
        # Required Skills
        try:
            expand_button = driver.find_element(By.ID, "expand-skills-description")
            expand_button.click()
        except:
            print("No additional skills to expand.")

        skills_list = modal.find_element(By.ID, "job-skills-description")
        skills = skills_list.find_elements(By.TAG_NAME, "li")

        # Extract the text from each <li> and store it in a list
        skills_text = [skill.text for skill in skills]

        skills_string = ', '.join(skills_text)



        # Employer Website
        try:
            website_element = modal.find_element(By.ID, "employer-website")

            # Get the employer website URL from the ng-href attribute
            employer_website = website_element.get_attribute("ng-href")

            # If ng-href is not available, you can use href as a fallback
            if not employer_website:
                employer_website = website_element.get_attribute("href")
        except:
            employer_website = None



        # YOE requirement range
        yoe_element = modal.find_element(By.XPATH, "//span[@class='experience ng-binding ng-scope']")

        # Get the text content from the element
        experience_text = yoe_element.text


        # location
        location_element = driver.find_element(By.XPATH, "//div[@class='job-locations']//span[contains(@class, 'ng-binding') and not(contains(@class, 'experience'))]")

        # Get the text content from the element
        location_text = location_element.text



        # applied on
        applied_on_element = driver.find_element(By.XPATH, "//div[@class='apply applied ng-scope']//span[contains(@class, 'ng-binding')]")

        # Get the text content from the element
        applied_on_text = applied_on_element.text



        # Recruiter Info
        rec_info_element = driver.find_element(By.XPATH, "//span[contains(@class, 'rec-info')]")

        rec_info_text = rec_info_element.text

        job_data.append({
            "Company name": company,
            "Company Summary": company_summary,
            "Job Role": role,
            "Required Skills": skills_string,
            "Employer Website": employer_website,
            "YOE Range": experience_text,
            "Location": location_text,
            "Date Applied": applied_on_text,
            "Recruiter Info": rec_info_text,
        })

        
        
        close_button = modal.find_element(By.CSS_SELECTOR, ".application-modal-close.back-button-modal-close")
        close_button.click()
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(3)



# Set up Selenium and start the driver with the user-agent
driver = webdriver.Chrome()

# Step 1: Go to Instahyre login page
driver.get(login_url)
time.sleep(2)

# Step 2: Enter email and password

email_input = driver.find_element(By.ID, "email")
email_input.send_keys(email)
time.sleep(2)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)
time.sleep(2)

login_button = driver.find_element(By.ID,"login-form")
login_button.click()

time.sleep(5)

driver.get(target_url)
time.sleep(3)


# Step 3: Scrape job details
job_data = []

while True:
    # Extract job details from the current page
    get_job_details()

    # Check for and click the "Next" button to go to the next page
    try:
        next_button = driver.find_element(By.XPATH, "//li[not(contains(@class, 'hidden')) and contains(text(), 'Next')]")
        time.sleep(3)
        next_button.click()
        time.sleep(3)

    except NoSuchElementException:
        print("No more pages left.")
        break

get_job_details

df = pd.DataFrame(job_data)
df.to_excel("applied_jobs.xlsx", index=False)

driver.quit()