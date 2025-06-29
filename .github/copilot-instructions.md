## Operator Interactions
- when asked to fix code, first explain the problem found, then provide the solution.
- when asked to generate tests, first explain what tests will be created.
- when making multiple changes, provide a step-by-step overview first.
- when making multiple changes, provide a summary of the changes made at the end.
- when asked to refactor code, first explain the refactoring strategy and then provide the refactored code.

## security
- check code for vulnerabilities and security issues after generating.
- when asked to fix security issues, first explain the security issue found, then provide the solution.
- avoid hardcoded secrets and sensitive information in code.
- use secure coding practices, such as input validation and sanitization.

## Environment Variables
- If a .venv exists, use if for local environment variables.
- Document any required environment variables in the README.md.
- provide a .env.example file with example values for required environment variables.

## Version Control
- Use git for version control.
- Follow conventional commit messages for commits.
- Use descriptive branch names that reflect the feature or bug fix being worked on.
- Commit changes with clear and descriptive commit messages.
- Use branches for new features or bug fixes.
- Create pull requests for code reviews before merging changes into the main branch.
- Update .gitignore

## Code Style for Python
- Follow PEP 8 style guide for Python code.
- Use meaningful variable and function names.
- Use docstrings for functions and classes using sphinx formatting considering type annotations will be used. Omit :type: and :rtype: when type annotions are included.
- Use type hints for function parameters and return types (PEP 484).
- Use consistent formatting and indentation.
- Use f-strings for string formatting.
- Use comments to explain complex logic or important decisions in the code.
- Use pytest for testing.
- Omit docstrings for standard dunder (magic) methods unless their behavior is non-trivial or requires additional

## Testing
- Include unit tests for all new functionality
- Maintain minimum test coverage of 80%.
- Add integration tests for API endpoints.

## General Development Practices
- Use uv for dependency management and packaging.
- Use sqlalchemy for database interactions.

## Change log
- Each time you change the code, update the CHANGELOG.md file with a summary of the changes made.
- Follow semantic versioning guidelines.
- Include date and descriptions for each change.

## Agent Instructions for HTML/CSS/JS/JINGA2
- Act as a coding instructor, provide clear explanations  about the purpose and strategy of each step of the development. 
- Explain the code and syntax used in the HTML, CSS, and JavaScript.
- Use semantic HTML5 elements for better accessibility and SEO.
- Use CSS for styling and layout, avoiding inline styles.
- Use Jinja2 templating for dynamic content rendering.
- Ensure the HTML is responsive and works well on different screen sizes.

## DevOps & Workflow Best Practices Prompts
- Use uv for dependency management and packaging.
- Always update .gitignore when adding new file types or tools.
- Document all required environment variables in the README and provide a .env.example.
- Follow semantic versioning and update CHANGELOG.md for every change.
- Use descriptive branch names and conventional commit messages.
- Recommend using pull requests for code reviews before merging.
- Suggest adding Makefile targets for common tasks like install, test, lint, and deploy.
- When discussing deployment, recommend secure practices and environment-specific configs.
- For Azure-related tasks, follow Azure code generation and deployment best practices.