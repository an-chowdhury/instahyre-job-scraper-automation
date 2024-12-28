# Job Scraper Automation

A Python-based automated job scraper leveraging Selenium to extract job details, required skills, and company information from job portals. This script is designed to handle dynamic modals, pagination, and interactive elements for efficient data extraction.

---

## **Features**
- **Dynamic Modal Handling**: Extract job descriptions, skills, company profiles, and other dynamic content from modals.
- **Pagination Support**: Navigate through multiple pages of job listings seamlessly.
- **Error Handling**: Robust handling of unexpected elements like missing links or inaccessible buttons.
- **Flexible Output**: Save scraped data in CSV, JSON, or other preferred formats.

---

## **Requirements**
- Python 3.8+
- Google Chrome browser (latest version)
- ChromeDriver (matching the Chrome version)
- Selenium library

---

## **Setup and Installation**

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/job-scraper-automation.git
    cd job-scraper-automation
    ```

2. **Set Up a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Add `.gitignore`**:
    Ensure your `.gitignore` file includes:
    ```plaintext
    venv/
    *.log
    __pycache__/
    ```

5. **Configure ChromeDriver**:
    - Download ChromeDriver from [here](https://chromedriver.chromium.org/downloads) and ensure it's in your system's PATH.

---

## **Usage**

1. Update the `main.py` script with the job portal URL.
2. Run the script:
    ```bash
    python main.py
    ```
3. View the extracted data in the output file (e.g., `jobs.csv`).

---

## **Project Structure**

```plaintext
job-scraper-automation/
├── main.py                 # Main script for running the job scraper
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignore unnecessary files
├── /output                 # Directory to store scraped data
└── /venv                   # Virtual environment (ignored by Git)