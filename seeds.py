from app import app, db
from models.image import Image

with app.app_context():
    db.drop_all()
    db.create_all()
    seed = []

    image_1 = Image(url='https://pixabay.com/get/52e3d6414853a914f6d1867dda6d49214b6ac3e456577240722c78d390/shadow-4332215_1920.jpg')
    seed.append(image_1)
    image_2 = Image(url='https://pixabay.com/get/52e3d1404f56ae14f6d1867dda6d49214b6ac3e456577240722c7fd091/susten-4343542_1920.jpg')
    seed.append(image_2)
    image_3 = Image(url='https://pixabay.com/get/55e9d74b4f5bac14f6d1867dda6d49214b6ac3e456577240722c7fdc96/harbour-city-3928590_1920.jpg')
    seed.append(image_3)
    image_4 = Image(url='https://pixabay.com/get/52e3d0404a5aae14f6d1867dda6d49214b6ac3e456577240722c7ed596/paris-4353082_1920.jpg')
    seed.append(image_4)
    image_5 = Image(url='https://pixabay.com/get/52e3d14b4a53a914f6d1867dda6d49214b6ac3e456577240722c7ed69f/moto-4348015_1920.jpg')
    seed.append(image_5)
    image_6 = Image(url='https://pixabay.com/get/52e3d6454a56a514f6d1867dda6d49214b6ac3e456577240722c7cd493/berry-breakfast-4336049_1920.jpg')
    seed.append(image_6)
    image_7 = Image(url='https://pixabay.com/get/52e3d14b4851af14f6d1867dda6d49214b6ac3e456577240722c7cd691/nettle-4348233_1920.jpg')
    seed.append(image_7)
    image_8 = Image(url='https://pixabay.com/get/52e3d0424854aa14f6d1867dda6d49214b6ac3e456577240722c73d590/agriculture-4351266_1920.jpg')
    seed.append(image_8)
    image_9 = Image(url='https://pixabay.com/get/52e3d0454852ae14f6d1867dda6d49214b6ac3e456577240722c72d695/firenze-4356202_1920.jpg')
    seed.append(image_9)

    db.session.add_all(seed)
    db.session.commit()
