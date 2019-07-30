from random import randrange
import requests
from app import app, db
from models.user import UserSchema
from models.image import Image
from models.post import Post, Entry
from config.environment import pixabay_api_key

# get random users from randomuser.me
response = requests.get(
    'https://randomuser.me/api/',
    params={
        'results': 100,
        'nat': 'gb',
        'inc': 'name,email,login,picture',
        'noinfo': True
})
api_users = response.json()['results']

# get images from pixabay
response = requests.get(
    'https://pixabay.com/api/',
    params={
        'key': pixabay_api_key,
        'editors_choice': True,
        'page': 1,
        'per_page': 200
    }
)
api_images = response.json()['hits']

user_schema = UserSchema()

with app.app_context():
    db.drop_all()
    db.create_all()

    # create new users from api users
    users = []
    for user in api_users:
        user, errors = user_schema.load({
            'username': user['login']['username'],
            'email': user['email'],
            'password':'pass',
            'password_confirmation': 'pass',
            'picture': user['picture']['large']
        })
        if errors:
            raise Exception(errors)
        user.save()
        users.append(user)

    user_1, errors = user_schema.load({
        'username':'user1',
        'email':'email1@email.com',
        'password':'pass',
        'password_confirmation': 'pass'
        })
    if errors:
        raise Exception(errors)

    user_2, errors = user_schema.load({
        'username':'user2',
        'email':'email2@email.com',
        'password':'pass',
        'password_confirmation': 'pass'
        })
    if errors:
        raise Exception(errors)

    # create new images from api images
    images = []
    for image in api_images:
        image = Image(
            url=image['webformatURL'],
            uploader=users[randrange(len(users))],
            height=image['webformatHeight'],
            width=image['webformatWidth']
        )
        images.append(image)

    # image_1 = Image(
    #     url='https://pixabay.com/get/52e3d6414853a914f6d1867dda6d49214b6ac3e456577240722c78d390/shadow-4332215_1920.jpg',
    #     uploader=user_1,
    #     height=1080,
    #     width=1920
    # )

    # image_2 = Image(
    #     url='https://pixabay.com/get/52e3d1404f56ae14f6d1867dda6d49214b6ac3e456577240722c7fd091/susten-4343542_1920.jpg',
    #     uploader=user_1,
    #     height=1080,
    #     width=1920
    # )

    # image_3 = Image(
    #     url='https://pixabay.com/get/55e9d74b4f5bac14f6d1867dda6d49214b6ac3e456577240722c7fdc96/harbour-city-3928590_1920.jpg',
    #     uploader=user_2
    # )

    # image_4 = Image(
    #     url='https://pixabay.com/get/52e3d0404a5aae14f6d1867dda6d49214b6ac3e456577240722c7ed596/paris-4353082_1920.jpg',
    #     uploader=user_2
    # )
    # image_5 = Image(url='https://pixabay.com/get/52e3d14b4a53a914f6d1867dda6d49214b6ac3e456577240722c7ed69f/moto-4348015_1920.jpg')
    # image_6 = Image(url='https://pixabay.com/get/52e3d6454a56a514f6d1867dda6d49214b6ac3e456577240722c7cd493/berry-breakfast-4336049_1920.jpg')
    # image_7 = Image(url='https://pixabay.com/get/52e3d14b4851af14f6d1867dda6d49214b6ac3e456577240722c7cd691/nettle-4348233_1920.jpg')
    # image_8 = Image(url='https://pixabay.com/get/52e3d0424854aa14f6d1867dda6d49214b6ac3e456577240722c73d590/agriculture-4351266_1920.jpg')
    # image_9 = Image(url='https://pixabay.com/get/52e3d0454852ae14f6d1867dda6d49214b6ac3e456577240722c72d695/firenze-4356202_1920.jpg')

    # entry_1 = Entry(
    #     image=image_1,
    #     caption='Caption 1',
    #     position=0
    # )
    #
    # entry_2 = Entry(
    #     image=image_2,
    #     caption='Caption 2',
    #     position=1
    # )
    #
    # post_1 = Post(
    #     title='Post 1',
    #     creator=user_1,
    #     post_entries=[
    #     entry_1,
    #     entry_2
    # ])
    #
    # post_2 = Post(
    #     title='Post 2',
    #     creator=user_1,
    #     post_entries=[
    #
    # ])
    #
    # post_3 = Post(
    #     title='Post 3',
    #     creator=user_2,
    #     post_entries=[
    #
    # ])

    # for each user, add all uploaded images to posts, each post no more than 3 entries long
    for user in users:
        if user.uploaded_images:
            i = 0
            while i < len(user.uploaded_images):
                entries = []
                pos = 0
                while pos < randrange(1, 4) and i < len(user.uploaded_images):
                    entry = Entry(
                        image=user.uploaded_images[i],
                        caption=f'Caption {pos}',
                        position=pos
                    )
                    entries.append(entry)
                    pos += 1
                    i += 1
                post = Post(
                    title='New Post',
                    creator=user,
                    post_entries=entries
                )
                post.save()
                print(post.creator, post.post_entries)

    db.session.add_all([
            # image_1,
            # image_2,
            # image_3,
            # image_4,
            # post_1
        ]
        # + users
        # + images
    )
    db.session.commit()
