import os

db_uri = os.getenv('DATABASE_URI', 'postgres://localhost:5432/imagebored')

secret = os.getenv('SECRET', 'VGhlIGZpcnN0IHJ1bGUgb2YgRmlnaHQgQ2x1YiBpczogWW91IGRvIG5vdCB0YWxrIGFib3V0IEZpZ2h0IENsdWIu')
