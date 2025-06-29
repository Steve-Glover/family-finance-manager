# CHANGELOG

## [0.2.0] - 2025-06-29
### Added
- Implemented all core SQLAlchemy data models:
  - `User` model in `app/models/user.py`
  - `Category` model in `app/models/category.py`
  - `Budget` model in `app/models/budget.py`
  - `Transaction` model in `app/models/transaction.py`


### Changed
- Refined project structure under `app/models/` for clarity and maintainability.

### Security
- Reviewed all new code for security best practices and input validation.

## [0.1.2] - 2025-06-28
### Added
- Added SQLAlchemy, Plotly, Dash, pytest, flake8, black, and coverage to project dependencies.
- Updated requirements.txt to reflect new dependencies.

## [0.1.1] - 2025-06-28
### Added
- Expanded README.md with setup instructions, environment variable documentation, and development workflow.
- Confirmed .env.example is present and correct.

## [0.1.0] - 2025-06-28
### Added
- Initial project setup, .gitignore, .env.example, and updated README.md.