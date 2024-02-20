# Django OIDC Authentication Project

## Overview

This project implements OIDC (OpenID Connect) authentication in a Django web application using Okta as the identity provider. It allows users to authenticate using their Okta credentials and provides seamless integration with the Django authentication system.

## Features

- OIDC authentication with Okta
- Secure login and logout functionality
- Integration with Django authentication system
- Easy configuration with environment variables
- API documentation with Swagger

## Setup

### Prerequisites

- Python 3.6+
- Django
- mozilla-django-oidc
- Okta developer account

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/django-oidc-auth.git
2. Navigate to the project directory:
   ```bash
   cd django-oidc-auth
3. Create a virtual environment:
   ```bash
   python -m venv venv
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
6. Set up environment variables:
   - Copy the contents of `.env.example` to a new file named `.env`.
   - Fill in the required values for Okta domain, client ID, and client secret in the `.env` file.

### Usage

1. Run the Django development server:
   ```bash
   python manage.py runserver
2. Access the application in your web browser:
