
## Template Overview

### `base.html`
- **Purpose:** Acts as the common layout for all pages.
- **Features:**
  - Includes Bootstrap CSS & JS via CDN.
  - Contains the navigation bar with links to Home, Tracker, and Add Expense pages.
  - Defines a block (`{% block content %}{% endblock %}`) for child templates to inject page-specific content.

### `home.html`
- **Purpose:** Serves as the landing page of the application.
- **Features:**
  - Extends `base.html`.
  - Displays a welcome message and brief instructions on navigating the app.

### `tracker.html`
- **Purpose:** Displays the list of expenses.
- **Features:**
  - Extends `base.html`.
  - Iterates over the expense entries and displays them in a Bootstrap-styled table.
  - Provides **Update** and **Delete** buttons for each expense entry (using the expense’s index).

### `add.html`
- **Purpose:** Provides a form for users to add new expenses.
- **Features:**
  - Extends `base.html`.
  - Contains a form with fields for **Amount**, **Category**, and **Description**.
  - Submits form data via POST to the `/add` route.




