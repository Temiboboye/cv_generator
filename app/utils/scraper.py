import requests
from bs4 import BeautifulSoup
import re

def scrape_job_description(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        job_description = soup.find('div', class_=re.compile('job-description|description|posting-body'))
        
        if job_description:
            return job_description.get_text(strip=True)
        else:
            return "Couldn't find job description. Please check the URL and try again."
    except Exception as e:
        return f"An error occurred while scraping: {e}"