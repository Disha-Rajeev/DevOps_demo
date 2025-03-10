from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Expense model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<Expense {self.id}>'

# Initialize the database tables manually
with app.app_context():
    db.create_all()

# Home page: Displays total expense and navigation options.
@app.route('/')
def home():
    total_expense = db.session.query(func.sum(Expense.amount)).scalar() or 0
    return render_template('home.html', total_expense=total_expense)

# Tracker page: Lists all expenses with Update, Delete, and an option to add another expense.
@app.route('/tracker')
def tracker():
    expenses = Expense.query.all()
    return render_template('tracker.html', expenses=expenses)

# Add Expense page: Form to create a new expense.
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        amount = request.form.get('amount')
        category = request.form.get('category')
        description = request.form.get('description')
        if amount and category:
            try:
                amount_val = float(amount)
            except ValueError:
                amount_val = 0.0
            expense = Expense(amount=amount_val, category=category, description=description)
            db.session.add(expense)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html')

# Update Expense page: Pre-populated form to update an expense.
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    expense = Expense.query.get_or_404(id)
    if request.method == 'POST':
        amount = request.form.get('amount')
        category = request.form.get('category')
        description = request.form.get('description')
        if amount and category:
            try:
                expense.amount = float(amount)
            except ValueError:
                expense.amount = 0.0
            expense.category = category
            expense.description = description
            db.session.commit()
            return redirect(url_for('tracker'))
    return render_template('update.html', expense=expense)

# Delete Expense route: Removes an expense.
@app.route('/delete/<int:id>')
def delete(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('tracker'))

if __name__ == '__main__':
    app.run(debug=True)
