# Family Finance Manager Application

This project is a web application to manage all aspects of a family budget. It is built using Flask as a backend and manages the front end with HTML, CSS, and Jinja2 templates. The application uses SQLite and SQLAlchemy ORM to manage and store data related to income, expenses, budgets, spending, and planning.

## Features
- Create a spending budget in an on-screen, paginated table.
- Track spending history by budget category.
- View a summary of all spending transactions by category.

## Technology Used
- Python 3.10
- Flask
- Jinja2 
- HTML5 
- CSS

## Data Storage 
- SQLite

## Visualizations
- Plotly
- Dash

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/family-finance-manager.git
   cd family-finance-manager
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies using uv:**
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in the values.

## Required Environment Variables

| Variable           | Description                    | Example Value                        |
|--------------------|--------------------------------|--------------------------------------|
| FLASK_SECRET_KEY   | Secret key for Flask sessions  | your-secret-key-here                 |
| DATABASE_URL       | Database connection string     | sqlite:///family_finance_manager.db  |

## Version Control & Development Workflow

- Use git for version control.
- Follow conventional commit messages.
- Use descriptive branch names for features and bug fixes.
- Commit changes with clear and descriptive messages.
- Use branches for new features or bug fixes.
- Create pull requests for code reviews before merging into the main branch.
- Update `.gitignore` as needed.
- Update `CHANGELOG.md` for every change, following semantic versioning.
