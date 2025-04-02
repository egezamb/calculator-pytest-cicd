# Calculator Project with CI/CD

A simple calculator project demonstrating:
- Python development in PyCharm
- Unit testing with pytest
- CI/CD integration with GitHub Actions

## Project Structure
- `calculator.py`: Contains basic calculator functions
- `tests/`: Directory containing pytest test files
- `.github/workflows/`: GitHub Actions workflow configuration

## Setup Instructions
1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Tests
Run tests with pytest:
```
pytest
```

For test coverage report:
```
pytest --cov=calculator
```

## CI/CD Pipeline
This project uses GitHub Actions for continuous integration. The workflow:
- Runs on push to main branch
- Sets up Python environment
- Installs dependencies
- Runs tests
- Reports any failures
