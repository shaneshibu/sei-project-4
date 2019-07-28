from app import app, db
from models.user import UserSchema
from models.image import Image
from models.post import Post, Entry


user_schema = UserSchema()

with app.app_context():
    db.drop_all()
    db.create_all()
    seed = []

    user_1, errors = user_schema.load({
        'username':'user1',
        'email':'email1@email.com',
        'password':'pass',
        'password_confirmation': 'pass'
        })
    if errors:
        raise Exception(errors)
    seed.append(user_1)

    user_2, errors = user_schema.load({
        'username':'user2',
        'email':'email2@email.com',
        'password':'pass',
        'password_confirmation': 'pass'
        })
    if errors:
        raise Exception(errors)
    seed.append(user_2)

    image_1 = Image(
        url='https://pixabay.com/get/52e3d6414853a914f6d1867dda6d49214b6ac3e456577240722c78d390/shadow-4332215_1920.jpg',
        uploader=user_1
    )
    seed.append(image_1)

    image_2 = Image(
        url='https://pixabay.com/get/52e3d1404f56ae14f6d1867dda6d49214b6ac3e456577240722c7fd091/susten-4343542_1920.jpg',
        uploader=user_1
    )
    seed.append(image_2)

    image_3 = Image(
        url='https://pixabay.com/get/55e9d74b4f5bac14f6d1867dda6d49214b6ac3e456577240722c7fdc96/harbour-city-3928590_1920.jpg',
        uploader=user_2
    )
    seed.append(image_3)

    image_4 = Image(
        url='https://pixabay.com/get/52e3d0404a5aae14f6d1867dda6d49214b6ac3e456577240722c7ed596/paris-4353082_1920.jpg',
        uploader=user_2
    )
    seed.append(image_4)
    # image_5 = Image(url='https://pixabay.com/get/52e3d14b4a53a914f6d1867dda6d49214b6ac3e456577240722c7ed69f/moto-4348015_1920.jpg')
    # seed.append(image_5)
    # image_6 = Image(url='https://pixabay.com/get/52e3d6454a56a514f6d1867dda6d49214b6ac3e456577240722c7cd493/berry-breakfast-4336049_1920.jpg')
    # seed.append(image_6)
    # image_7 = Image(url='https://pixabay.com/get/52e3d14b4851af14f6d1867dda6d49214b6ac3e456577240722c7cd691/nettle-4348233_1920.jpg')
    # seed.append(image_7)
    # image_8 = Image(url='https://pixabay.com/get/52e3d0424854aa14f6d1867dda6d49214b6ac3e456577240722c73d590/agriculture-4351266_1920.jpg')
    # seed.append(image_8)
    # image_9 = Image(url='https://pixabay.com/get/52e3d0454852ae14f6d1867dda6d49214b6ac3e456577240722c72d695/firenze-4356202_1920.jpg')
    # seed.append(image_9)

    post_1 = Post(title='Post 1', creator=user_1)
    seed.append(post_1)


    post_2 = Post(title='Post 2', creator=user_1)
    seed.append(post_2)

    post_3 = Post(title='Post 3', creator=user_2)
    seed.append(post_3)

    db.session.add_all(seed)
    db.session.commit()

    entry_1 = Entry(
        post_id=post_1.id,
        image_id=image_1.id,
        caption='Caption 1',
        position=0
    )
    db.session.add(entry_1)

    entry_2 = Entry(
        post_id=post_1.id,
        image_id=image_2.id,
        caption='Caption 2',
        position=1
    )
    db.session.add(entry_2)
    db.session.commit()
