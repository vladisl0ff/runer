from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent, ShareEvent, LikeEvent, FollowEvent, MoreShareEvent, EnvelopeEvent, UnknownEvent, EmoteEvent, DisconnectEvent
from bd import Table
from threading import Thread
from main import run


client: TikTokLiveClient = TikTokLiveClient(unique_id="@parts_films")
# nnotochka, lily25881, texob_, ben_toye, promo.ana parts_films
path_apk = 'data/data/com.vlad.runer/files/app/'


@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connect to Room ID:", client.room_id)


#Коментарий
@client.on("comment")
async def on_connect(event: CommentEvent):
    # print(f"{event.user.nickname} -> {event.comment}")
    coment_update(event.comment)


# Отправка смайла
@client.on("emote")
async def on_connect(event: EmoteEvent):
    print(f"{event.user.nickname} -> {event.emote.image.url}")


# Лайк стрима (event.total_likes - всего лайков)
# @client.on("like")
# async def on_like(event: LikeEvent):
#     print(f"@{event.user.unique_id} лайкнул стрим!")


# Подарок
@client.on("gift")
async def on_gift(event: GiftEvent):
    # Streakable gift & streak is over
    if event.gift.streakable and not event.gift.streaking:
        print(f"Пользователь {event.user.unique_id} отправил {event.gift.count}x \"{event.gift.info.name}\" {event.gift.count*event.gift.info.diamond_count}")
        gift_update(event.gift.info.name, event.gift.count*event.gift.info.diamond_count)
        print(event.gift.info.name)
    # Non-streakable gift
    elif not event.gift.streakable:
        print(f"Пользователь {event.user.unique_id} отправил \"{event.gift.info.name}\" стоимостью {event.gift.info.diamond_count}")


# Подписка на стримера
@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"@{event.user.unique_id} Подписался на стримера!")


# Поделился трансляцией
# @client.on("share")
# async def on_share(event: ShareEvent):
#     print(f"@{event.user.unique_id} Поделился стримом!")


# Пришло по ссылке людей от пользователя
@client.on("more_share")
async def on_connect(event: MoreShareEvent):
    print(f"Более чем {event.amount} пользователей присоединились по ссылке общего доступа {event.user.unique_id}!")


# Сундук с подарками
@client.on("envelope")
async def on_connect(event: EnvelopeEvent):
    print(f"Сундук {event.treasure_box_user.unique_id} -> {event.treasure_box_data}")


# Неизвестный ивент
# @client.on("unknown")
# async def on_connect(event: UnknownEvent):
#     print(f"Event Type: {event.type}")
#     print(f"Event Base64: {event.base64}")


# Дисконект, можно постачать в start и перезапустить стрим (но нужно немного подождать)
@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
    print("Произошёл дисконект")


def gift_update(gift, coins):
    if gift == "Rose" or gift == "Mishka Bear":
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 1")['points']
        bd_players.set_person_points("Person 1", coins*3 + player1)
    elif gift == "TikTok" or gift == "Little Crown":
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 5")['points']
        bd_players.set_person_points("Person 5", coins*3 + player1)
    elif gift == "Football" or gift == "Confetti":
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 2")['points']
        bd_players.set_person_points("Person 2", coins*3 + player1)
    elif gift == "Weights" or gift == "Hat and Mustache":
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 3")['points']
        bd_players.set_person_points("Person 3", coins*3 + player1)
    elif gift == "Ice Cream Cone" or gift == "Cap":
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 4")['points']
        bd_players.set_person_points("Person 4", coins*3 + player1)


Person_1 = ['россия', 'роccия', 'poccия', 'poccия', 'rossiya', 'rociya', 'roccya', 'rossya', 'roccia', 'pocciya', 'russia', 'russiya', 'russiia', 'russiaa', 'rusha', 'rusia', 'ruusia', 'russya', 'rusya', 'russsia']
Person_2 = ['украина', 'украина', 'украiна', 'україна', 'українa', 'украинa', 'українe', 'украине', 'украини', 'украинаa', 'ukraine', 'Ukraine', 'UKRAINE', 'ukraina', 'ukrainia', 'ukraiana', 'ukraïna', 'ukraïne', 'ukrayna', 'ukraynna', 'ukrainea', 'ukraeina']
Person_3 = ['казахстан', 'казаxстан', 'казахcтан', 'казахстань', 'казахста', 'казашстан', 'кадахстан', 'казагстан', 'kazakhstan', 'kazakstan', 'kazahstan', 'kazakhatan', 'kazaksthan', 'kasakhstan', 'kazahkstan', 'kazzakstan']
# Person_4 = ['беларусь', 'белорусь', 'беларус', 'белорус', 'belarus', 'belaruss', 'belarous', 'byelarus', 'bielarus', 'belaruz', 'belarous', 'byelorussia', 'bielorussia']
Person_4 = ['сербия', 'Сербия', 'СЕРБИЯ', 'сербская', 'Сербская', 'СЕРБСКАЯ', 'серб', 'Серб', 'СЕРБ', 'serbia', 'Serbia', 'SERBIA', 'serb', 'serbian']
Person_5 = ['молдова', 'молдавия', 'молдов', 'moldova', 'moldavia', 'moldavija', 'moldavie', 'moldovia', 'moldovya', 'moldovy', 'moldau', 'moldawia']


def coment_update(text):
    if text.lower() in Person_1:
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 1")['chat']
        bd_players.set_person_chat("Person 1", 2 + player1)
    elif text.lower() in Person_2:
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 2")['chat']
        bd_players.set_person_chat("Person 2", 2 + player1)
    elif text.lower() in Person_3:
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 3")['chat']
        bd_players.set_person_chat("Person 3", 2 + player1)
    elif text.lower() in Person_4:
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 4")['chat']
        bd_players.set_person_chat("Person 4", 2 + player1)
    elif text.lower() in Person_5:
        bd_players = Table("bd.json")
        player1 = bd_players.get_person_data("Person 5")['chat']
        bd_players.set_person_chat("Person 5", 2 + player1)


if __name__ == '__main__':
    # Запустите клиент и заблокируйте основной поток
    # await client.start() для запуска без блокировки
    thread1 = Thread(target=lambda: run())
    thread2 = Thread(target=lambda: client.run())
    thread1.start()
    thread2.start()



