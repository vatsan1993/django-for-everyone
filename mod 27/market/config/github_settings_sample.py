
# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/apps

# Add a New OAuth2 App

# Using PythonAnywhere here are some settings - replace "drchuck" with your account name

# Application name: DJ4E Marketplace
# Homepage Url: https://drchuck.pythonanywhere.com
# Application Description: Whatever
# Authorization callback URL: https://drchuck.pythonanywhere.com/oauth/complete/github/

# When you are given a Client ID, copy it into this file.  Ask to generate a
# "New client secret".

# Also on PythonAnywhere, go into the Web tab and enable "Force HTTPS"
# so you don't get a redirect URI mismatch.

# Then copy the client_key and secret to this file

SOCIAL_AUTH_GITHUB_KEY = 'GITHUB_KEY_HERE'
SOCIAL_AUTH_GITHUB_SECRET = 'GITHUB_SECRET_HERE'

# Ask for the user's email (don't edit this line)
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']

# Note you may not get email for github users that don't make their
# email public - that is OK

# For detail: https://python-social-auth.readthedocs.io/en/latest/configuration/django.html

# If you are running on localhost, here are some settings:

# Application name: ChuckList Local
# Homepage Url: http://localhost:8000
# Application Description: Whatever
# Authorization callback URL: http://127.0.0.1:8000/oauth/complete/github/
