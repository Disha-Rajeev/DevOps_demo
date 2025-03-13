# DevOps_demo
This is my first project where I am testing out the DevOps knowledge I gained from past few months.
What I am looking forward to achieve-.\
      ✅ End-to-end DevOps pipeline from development to deployment.\
      ✅ CI/CD automation with GitHub Actions/Jenkins.\
      ✅ Containerization & orchestration with Docker & Kubernetes.\
      ✅ AWS infrastructure provisioning using Terraform.\
      ✅ Monitoring & logging for application health tracking.

This project is a great portfolio builder.

########################################################################
# Expense Tracker Web App

This is a simple Expense Tracker web application built using **Flask** with SQLite as the database. It allows users to manage their expenses with features like adding, updating, and deleting expenses. The app also calculates the total expense.

## Features

✅ Add new expenses with details like amount, category, and description.\
✅ View total expenses on the home page.\
✅ Update or delete existing expenses.\
✅ Uses SQLite for efficient data management.\
✅ Dockerized for easy deployment and scalability.\
✅ CI/CD integration with GitHub Actions.\

---

## Project Structure

```
/DevOps_demo
 ├── /templates
 │   ├── home.html
 │   ├── add.html
 │   ├── tracker.html
 ├── app.py
 ├── requirements.txt
 ├── Dockerfile
 ├── .github/workflows
 │   ├── ci-cd.yaml
 ├── tests
 │   ├── test_app.py
 ├── README.md
 ├── .gitignore
 ├── instance/
 │   ├── expenses.db (auto-generated during setup)
```

---

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.9 or above**
- **Flask**
- **SQLite**
- **Docker**
- **Git**

---

## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/Disha-Rajeev/DevOps_demo.git
cd DevOps_demo
```

2. **Create a Virtual Environment**

```bash
python -m venv env
source env/bin/activate     # On Mac/Linux
env\Scripts\activate        # On Windows
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Database Setup**

Since the `expenses.db` file is not tracked in Git (added to `.gitignore`), you need to regenerate it:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

**Note:** If `db.create_all()` fails, ensure your `instance/` folder exists. If not, manually create it in the project root.

5. **Run the Flask App**

```bash
python app.py
```

6. **Access the Application**\
   Open your browser and visit:\
   **[http://localhost:5000](http://localhost:5000)**

---

## Docker Setup

1. **Build the Docker Image**

```bash
docker build -t expense-tracker .
```

2. **Run the Container**

```bash
docker run -d -p 5000:5000 expense-tracker
```

---

## Running Tests

1. Install **pytest** if not already installed:

```bash
pip install pytest
```

2. Run the tests:

```bash
pytest
```

---

## CI/CD Pipeline

This project includes a GitHub Actions CI/CD pipeline:

- Runs tests using `pytest`.
- Builds the Docker image.
- Deploys the application to a specified environment (if configured).

Workflow file path: `.github/workflows/ci-cd.yaml`

---

## Future Enhancements

🔹 Implement user authentication.\
🔹 Add filtering and sorting features for better expense management.\
🔹 Improve UI with enhanced Bootstrap styling.\
🔹 CI/CD automation with Jenkins.\
🔹 Containerization & orchestration with Kubernetes.\
🔹 AWS infrastructure provisioning using Terraform.\
🔹 Monitoring & logging for application health tracking.\
🔹 Enhanced database migration handling to ensure seamless updates.

---

## Contributing

Contributions are welcome! If you'd like to improve the project, please fork the repository and create a pull request.

---

## Author

**Disha Rajeev**

---

## License

This project is licensed under the GNU General Public License v3. See the [LICENSE](LICENSE) file for details.



