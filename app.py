from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for expenses (for simplicity)
expenses = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tracker')
def tracker():
    return render_template('tracker.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Retrieve data from the form
        amount = request.form.get('amount')
        category = request.form.get('category')
        description = request.form.get('description')
        # Create an expense record and add it to the list
        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }
        expenses.append(expense)
        return redirect(url_for('tracker'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)












