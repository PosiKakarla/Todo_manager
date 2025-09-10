A Django-based web app for managing daily tasks with full CRUD functionality. I built this project to sharpen my backend development skills and learn the deployment workflow.

*Features:

-Add, view, update, and delete tasks
-Responsive UI with Bootstrap + custom CSS
-Admin panel for task management
-Deployment-ready setup for Render with PostgreSQL (in progress 🚀)

*Setup:

-Create a virtual environment: python -m venv venv
-Activate it:
Windows: venv\Scripts\activate
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Create a superuser: python manage.py createsuperuser
Start the server: python manage.py runserver

*Usage:
-Open http://127.0.0.1:8000/ in your browser
-Use /admin for managing tasks via the admin panel
-Add, edit, or delete tasks through the UI

*Tech Stack:
-Django
-SQLite (local) → PostgreSQL (planned for Render)
-Bootstrap (via CDN) + custom styles.css
*Live Demo:

-Deployment to Render is in progress—stay tuned for a live link!

*Future Plans:

-Complete deployment to Render with PostgreSQL
-Add user authentication for personalized task lists
