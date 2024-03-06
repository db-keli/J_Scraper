# Scrapping for Python Related Jobs TimesJobs Webpage that are posted a few days ago on a daily basis into a csv file

# Importing Libaries
import datetime
import time
import csv
from bs4 import BeautifulSoup
import requests

import smtplib 


def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    source = requests.get(url)
    
    source.raise_for_status() 
    soup = BeautifulSoup(source.text, 'html.parser')
    
    pretify_code = soup.prettify()
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text.replace('  ', '')
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace('  ','').strip()
            application_link = job.header.h2.a['href']
            required_skills = job.find('span', class_='srp-skills').text.replace('  ', '').strip()
            today = datetime.date.today()
            
            header = ['Today', 'Company Name', 'Required Skills', 'Application Link']
            data = [today, company_name, required_skills, application_link]
            
            with open('Job_info.csv', 'a+', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(data)


if __name__ == "__main__":
    while True:
        find_jobs()
        waiting_time = 24
        print(f'waiting for {waiting_time} hours...')
        time.sleep(waiting_time*3600)


def send_mail():
    if time.sleep(waiting_time*3600):
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.ehlo()
        server.login('kekelidompeh@gmail.com','xxxxxxxxxxxxxx')
        
        subject = "Python Job Posting!"
        body = "James, your dream python job has been posted. Don't mess it up! You can check your spreadsheet or proceed with the link here: https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'kekelidompeh@gmail.com',
            msg

        )

       
