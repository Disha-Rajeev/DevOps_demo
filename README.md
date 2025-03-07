# DevOps_demo
This is my first project where I am testing out the DevOps knowledge I gained from past few months.
What I am looking forward to achieve-
      ✅ End-to-end DevOps pipeline from development to deployment
      ✅ CI/CD automation with GitHub Actions/Jenkins
      ✅ Containerization & orchestration with Docker & Kubernetes
      ✅ AWS infrastructure provisioning using Terraform
      ✅ Monitoring & logging for application health tracking

This project is a great portfolio builder.

# Expense Tracker - Flask Project

This is a simple Expense Tracker web application built with Flask. The project demonstrates basic CRUD operations (Create, Read, Update, Delete) along with a modular template structure using Flask's template inheritance. It is designed as a learning project to practice web development and DevOps concepts.

## Project Structure

DevOps_Demo/ 
   │ 
   ├── app.py 
   ├── README.md 
   └── templates/ 
         ├── base.html # Common base template that includes the navbar and Bootstrap setup. 
         ├── home.html # Home page template with a welcome message. 
         ├── tracker.html # Tracker page template that displays a table of all recorded expenses. 
         └── add.html # Template for adding a new expense via a form. 

## Running the Project

1. **Install Dependencies:**
   Ensure you have Python installed. Then, install Flask:
   ```bash
   pip install flask
   pip install flask flask_sqlalchemy

2. **Run the Flask App:** 
   From the project root directory, run:
   ```bash
   python app.py

The application will start in debug mode at http://127.0.0.1:5000/.

## Navigate the App:

Home Page: http://127.0.0.1:5000/
Add Expense: http://127.0.0.1:5000/add
Expense Tracker: http://127.0.0.1:5000/tracker
Update Expense Page: Accessible via the Update button on the Tracker page.

---

This **README** provides clear documentation about templates, project structure, usage instructions, and potential next steps. Adjust or expand the content as needed for specific project details or additional features you implement.
