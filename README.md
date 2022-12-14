# Tasker
Task-management solution designed for cross-company utilization. Supports task and project creation and management.


## Design
- [Design](docs/design.md)
- [Data model](docs/data-model.md)

## Methods
- [Methods](docs/methods.md)


## Project Initialization

To fully enjoy this application on your local machine, please make sure to follow these steps:

1. Clone the repository down to your local machine
2. CD into the new project directory
3. Run `python -m venv .venv`
4. Run one of the below to activate virtual environment <br />
macOS: `source ./.venv/bin/activate`   <br/>
Windows: `./.venv/Scripts/Activate.ps1`
5. Run `python -m pip install --upgrade pip`
6. Run `pip install -r requirements.txt`
7. Run `python manage.py migrate`
8. Run `python manage.py runserver`


## Project Deactivation
1. Clost development server
2. Run `deactivate`


## Testing

To verify this application is working on your local machine, please make sure to follow these steps after completing steps 1-7 of Project Initialization:

1. Run `python manage.py test`
