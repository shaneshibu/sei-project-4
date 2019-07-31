import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/imagebored')

secret = os.getenv('SECRET', 'Shhh.. It\'s a secret')

pixabay_api_key = os.getenv('PIXABAY_API_KEY')
