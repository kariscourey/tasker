from django.test import SimpleTestCase


class FeatureTests(SimpleTestCase):
    def test_tasker_project_created(self):
        try:
            from tasker.settings import INSTALLED_APPS  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find the Django project 'tasker'")

    def test_accounts_app_created(self):
        try:
            from accounts.apps import AccountsConfig  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find the Django app 'accounts'")

    def test_projects_app_created(self):
        try:
            from projects.apps import ProjectsConfig  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find the Django app 'projects'")

    def test_tasks_app_created(self):
        try:
            from tasks.apps import TasksConfig  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find the Django app 'tasks'")

    def test_accounts_app_installed(self):
        try:
            from tasker.settings import INSTALLED_APPS

            self.assertIn("accounts.apps.AccountsConfig", INSTALLED_APPS)
        except ModuleNotFoundError:
            self.fail("Could not find 'accounts' installed in 'tasker'")

    def test_projects_app_installed(self):
        try:
            from tasker.settings import INSTALLED_APPS

            self.assertIn("projects.apps.ProjectsConfig", INSTALLED_APPS)
        except ModuleNotFoundError:
            self.fail("Could not find 'projects' installed in 'tasker'")

    def test_tasks_app_installed(self):
        try:
            from tasker.settings import INSTALLED_APPS

            self.assertIn("tasks.apps.TasksConfig", INSTALLED_APPS)
        except ModuleNotFoundError:
            self.fail("Could not find 'tasks' installed in 'tasker'")
