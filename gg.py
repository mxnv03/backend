import vk_api
import os
from urllib.request import urlretrieve

with open('pythonProject/token.txt') as file:
    token = file.readline()

vk = vk_api.VkApi(token=token)
vk_api = vk.get_api()


def first_task(url):
    album_id = url.split('/')[-1].split('_')[1]
    owner_id = url.split('/')[-1].split('_')[0].replace('album', '')
    if not os.path.exists('saved'):
        os.mkdir('saved')
    photo_folder = f'saved/{album_id}'
    if not os.path.exists(photo_folder):
        os.mkdir(photo_folder)
    photos = vk_api.photos.get(owner_id=owner_id, album_id=album_id, extended=1)['items']
    k = 0
    for photo in photos:
        url_ph = photo['sizes'][-1]['url']
        user = vk.method("users.get", {"user_ids": photo['user_id']})
        fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
        likes = photo['likes']['count']
        urlretrieve(url_ph, photo_folder + "/" + str(k) + '.jpg') # Загружаем и сохраняем файл
        print(f'Мем c url: {url_ph} от автора {fullname} имеет {likes} лайка(ов)')
        k += 1


def second_task(url):
    album_id = url.split('/')[-1].split('_')[1]
    owner_id = url.split('/')[-1].split('_')[0].replace('album', '')
    photos = vk_api.photos.get(owner_id=owner_id, album_id=album_id, extended=1)['items']
    for photo in photos:
        url_ph = photo['sizes'][-1]['url']
        user = vk.method("users.get", {"user_ids": photo['user_id']})
        fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
        likes = photo['likes']['count']
        print(f'Мем c url: {url_ph} от автора {fullname} имеет {likes} лайка(ов)')
        action = input('Like of skip this mem?')
        if action == 'Like' or 'like':
            id = photo['id']
            owner_id = photo['owner_id']
            vk_api.likes.add(type='photo', owner_id=owner_id, item_id=id)

