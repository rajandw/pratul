# Python Hello World CI/CD Demo
A simple Python project with an automated CI/CD pipeline using GitHub Actions to test code and deploy it to an AWS EC2 instance.

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About
This project demonstrates how to set up a complete CI/CD pipeline using **free tools** like GitHub Actions and AWS Free Tier EC2.  
The pipeline:
- Runs automated tests using `pytest` to verify that the program output matches the expected string.
- If tests pass, automatically launches a **t2.micro** EC2 instance, deploys the code, and runs it.
- Uses GitHub Secrets for securely storing AWS credentials and SSH keys.
- Serves as a portfolio-ready example to showcase DevOps skills to potential employers.

**Features:**
- Lightweight Python app (`Hello World ~ Pratul`)
- Automated testing
- Zero-downtime deployment to AWS EC2
- Fully managed pipeline on code push

**Scope:**
Ideal for demonstrating:
- CI/CD concepts
- GitHub Actions workflows
- AWS EC2 automation
- Python testing with pytest

## Installation
Step-by-step instructions to set up the project locally.

```bash
# Clone the repository
git clone https://github.com/rajandw/pratul.git
cd pratul

# Create a Python virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
