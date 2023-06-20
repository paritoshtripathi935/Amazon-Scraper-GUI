import os

# Create main directories
os.makedirs('amazon-scraper-web-app/static/css')
os.makedirs('amazon-scraper-web-app/static/js')
os.makedirs('amazon-scraper-web-app/templates')
os.makedirs('amazon-scraper-web-app/scraper')

# Create files
open('amazon-scraper-web-app/app.py', 'w').close()
open('amazon-scraper-web-app/requirements.txt', 'w').close()
open('amazon-scraper-web-app/static/css/style.css', 'w').close()
open('amazon-scraper-web-app/static/js/script.js', 'w').close()
open('amazon-scraper-web-app/templates/base.html', 'w').close()
open('amazon-scraper-web-app/templates/form.html', 'w').close()
open('amazon-scraper-web-app/templates/results.html', 'w').close()
open('amazon-scraper-web-app/scraper/__init__.py', 'w').close()
open('amazon-scraper-web-app/scraper/amazon_scraper.py', 'w').close()

print("Folder structure created successfully!")
