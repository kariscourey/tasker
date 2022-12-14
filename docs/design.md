# Design

## Tasker monolith
Single-tiered task-management application within the projects directory.

### Accounts
Leverages Django's UserCreationForm, LoginView, and LogoutView to be able to create instances of users with accounts, present a login interface, and present a logout interface.

### Tasks
Centers on the Task model, instances of which describe tasks, with views permitting users to list, update, and create tasks through various means.

### Projects
Centers on the Project model, instances of which describe projects, with views permitting users to list, update, and create projects through various means. Company model permits cross-company utilization.
