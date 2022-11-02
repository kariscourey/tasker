# Tasker
Task-management solution designed for cross-company utilization. Supports task and project creation and management.


## Tools, techniques, languages

### Tools
Django <br/>

### Techniques
Templating <br/>
Monolith <br/>

### Languages
Python 3 <br/>
HTML <br/>
CSS <br/>


## Get started

### Activate virtual environment
macOS: source ./.venv/bin/activate   <br/>
Windows: ./.venv/Scripts/Activate.ps1

### Run development server
python manage.py runserver



## Design

### Tasker monolith
Single-tiered task-management application within the projects directory.

#### Accounts
Leverages Django's UserCreationForm, LoginView, and LogoutView to be able to create instances of users with accounts, present a login interface, and present a logout interface.

#### Tasks
Centers on the Task model, instances of which describe tasks, with views permitting users to list, update, and create tasks through various means.

#### Projects
Centers on the Project model, instances of which describe projects, with views permitting users to list, update, and create projects through various means. Company model permits cross-company utilization.
