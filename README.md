# J_Scraper
A web scraping API for scraping jobs
# Job Scraping Tool with Daily Email Notifications

## Overview
This project is a Python-based job scraping tool that extracts job listings from the Times Jobs website and sends daily email notifications containing the scraped data. The tool utilizes Beautiful Soup for web scraping and smtplib for email automation.

## Features
- Scrapes job listings from the Times Jobs website.
- Sends daily email notifications with the scraped job data.
- Handles errors and exceptions gracefully.
- Stores scraped data in CSV format for further analysis.

## Installation
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/db-keli/J_scraper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd J_scraper
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the `scrape.py` script to start the job scraping and email automation process:

    ```bash
    python scrape.py
    ```

## Configuration
Modify the `scrape.py` file to customize the following settings:
- Email sender and recipient addresses
- SMTP server settings
- Times Jobs website URL

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Support
For questions, issues, or feedback, please contact [Dompeh Kofi Bright](mailto:kekelidompeh@gmail.com).
