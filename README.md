# Bincom Recruitment Test

## Overview
This Django web application was developed as part of the Bincom recruitment technical test. 
The app works with the provided `bincom_test.sql` database containing dummy election results 
for Delta State, Nigeria (2011 elections).  

The application allows users to:

1. View results for an individual polling unit.
2. View summed total results for all polling units under a Local Government (LGA).
3. Add results for a new polling unit across all political parties.


## Technology Stack
- Backend: Python 3.13, Django 5.2.5
- Database: MySQL (bincom_test.sql)
- Frontend: HTML


## Setup Instructions

1. Clone the repository
    ```bash
    git clone <YOUR_GITHUB_REPO_LINK>
    cd <REPO_FOLDER>
2. Install dependencies
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
3. Configure Database
    Create a MySQL database and import the provided bincom_test.sql file.
    Update settings.py in the Django project with your MySQL credentials.
4. Apply Migrations
    python3 manage.py makemigrations
    python3 manage.py migrate
5. Run the Development Server
    python3 manage.py runserver


## Application Features
1. Polling Unit Results

    URL: /polling-unit/<uniqueid>/
    Displays results for an individual polling unit by uniqueid.

2. LGA Results

    URL: /lga-results/
    Allows selection of an LGA from a dropdown.
    Sums all polling unit results under the selected LGA by party.

3. Add Polling Unit Results

    URL: /add-polling-unit/
    Allows entering results for a new polling unit.
    Automatically assigns a unique uniqueid to each new polling unit.


## Notes

    All views have been implemented using Django's classless views for simplicity.
    The application is minimal but fully functional and fulfills the requirements of the test.

## Author
    TECO-BENSON TOCHUKWU
    Python developer intern Applicant

## Submission Links

    Live Solution: [Insert your hosted app URL here]
    Source Code: [Insert GitHub repository URL here]