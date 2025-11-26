# Statistics and Probability Assignments

A lightweight Python toolkit for working through statistics and probability assignments. The project bundles reusable helper functions, reproducible notebooks/workflows, and a testing scaffold so solutions stay organized and ready to publish on GitHub.

## Features
- Reusable descriptive statistics, probability, and simulation helpers inside `src/statprob`.
- Ready-to-run unit tests powered by `pytest`.
- `ruff` configuration for linting/formatting feedback.
- Simple Makefile commands for common developer workflows.
- Documentation for setting up a virtual environment and pushing the project to GitHub.

## Getting Started
1. **Clone or create the repo**
   ```bash
   git clone <your-repo-url> statistics_and_probability_assignments
   cd statistics_and_probability_assignments
   ```
2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the test suite**
   ```bash
   make test
   ```

## Project Structure
```
.
├── src/statprob        # Library code for assignments
├── tests               # Pytest-based unit tests
├── requirements.txt    # Runtime + dev dependencies
├── pyproject.toml      # Tooling configuration (pytest, ruff)
└── Makefile            # Shortcuts for linting, testing, formatting
```

## Common Tasks
- `make lint` – run `ruff` to lint the codebase.
- `make format` – auto-format using `ruff`'s formatter.
- `make test` – run the unit tests via `pytest`.
- `make check` – lint + test in one command.

## Debug / Launch
- Use `make test` or `pytest` to execute the suite locally inside the virtual environment.
- In VS Code, run the `pytest` task from the `Terminal > Run Task…` menu for repeatable test execution.
- For ad-hoc debugging, set breakpoints in `src/statprob` modules and run `pytest` with `-k <test_name>` to focus on a specific scenario.

## Publishing to GitHub
1. Initialize Git and commit your work:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
2. Create a new repository on GitHub (or reuse an existing one).
3. Add the remote origin and push:
   ```bash
   git remote add origin git@github.com:<username>/statistics_and_probability_assignments.git
   git branch -M main
   git push -u origin main
   ```

## Next Steps
- Add new assignment-specific scripts/notebooks under `src/` or `notebooks/` (create as needed).
- Expand `tests/` with cases that mirror coursework questions so results stay verifiable.
- Share the repository link when submitting assignments to keep an auditable history.
