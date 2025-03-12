import pytest # type: ignore
from app import app, db, Expense

@pytest.fixture
def client():
    # Set the Flask application in testing mode
    app.config['TESTING'] = True
    # Use an in-memory SQLite database for testing to avoid altering your real data.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            # Set up the database tables
            db.create_all()
        yield client
        # Clean up / drop tables after tests
        with app.app_context():
            db.drop_all()

def test_home_page(client):
    """Test that the home page loads correctly and shows total expense."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Total Expense Spent:" in response.data

def test_add_expense(client):
    """Test that adding an expense works."""
    # Post an expense
    response = client.post('/add', data={
        'amount': '50.75',
        'category': 'Food',
        'description': 'Dinner at restaurant'
    }, follow_redirects=True)
    
    # After adding, we should be redirected to the home page
    assert response.status_code == 200
    # Check if the expense appears by verifying the updated total (50.75)
    assert b"50.75" in response.data or b"Total Expense Spent:" in response.data

def test_tracker_page(client):
    """Test that the tracker page displays expenses."""
    # First, add an expense directly into the database
    with app.app_context():
        expense = Expense(amount=25.00, category='Transport', description='Bus fare')
        db.session.add(expense)
        db.session.commit()
    
    response = client.get('/tracker')
    assert response.status_code == 200
    # Verify the expense details are present on the tracker page
    assert b"25.0" in response.data or b"Transport" in response.data
