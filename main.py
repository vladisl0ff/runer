import random
import pygame
from player import players
from bd import Table


clock = pygame.time.Clock()
path_apk = 'data/data/com.vlad.runer/files/app/'

person = ["Person 1", "Person 2", "Person 3", "Person 4", "Person 5"]
persons = ["Person 1", "Person 2", "Person 3", "Person 4", "Person 5"]
gamers = ["Россия", "Украина", "Казахстан", "Сербия", "Молдова"]


def bd_clear():
    for per in person:
        bd_players = Table("bd.json")
        bd_players.set_person_points(per, 0)
        bd_players.set_person_chat(per, 0)
        bd_players.set_person_victories(per, 0)


def run():
    bd_clear()
    pygame.init()
    screen = pygame.display.set_mode((360, 640))
    pygame.display.set_caption("TikTokGame")

    bg = pygame.image.load("sprite/bg/bg.png")
    bg2 = pygame.image.load("sprite/bg/bg2.png")
    bg_x = 0

    timer_random = 0

    bd_players = Table("bd.json")

    font = pygame.font.SysFont(None, 25)
    font_win = pygame.font.SysFont(None, 50)
    font_scope = pygame.font.SysFont(None, 20)

    players_info = []
    players_sum_win_text = []
    players_name_text = []

    person_name = ('Mage', 'Knight', 'Rogue', 'Mage', 'Knight')
    player_gift_patch = ["sprite/gift/rose.png", "sprite/gift/bool.png", "sprite/gift/gant.png", "sprite/gift/mor.png", "sprite/gift/tt.png"]
    player_gift_big_patch = ["sprite/gift/beer_100.png", "sprite/gift/mini_kor_99.png", "sprite/gift/konf_100.png", "sprite/gift/shlap_99.png", "sprite/gift/korona_100.png"]
    idel = []
    player_idel = []
    player_idel_max_anim_count = []
    player_jump = []
    player_jump_max_anim_count = []
    player_bust_anim = []
    player_bust_count_max = []
    pleer_anim_count_jump = []
    player_bust_count = []
    pleer_anim_count = []
    player_last_scope = []
    player_gift = []
    player_gift_big = []

    for i in range(0,5):
        info = bd_players.get_person_data(persons[i])
        players_info.append(info)
        players_sum_win_text.append(font_win.render(str(info['victories']), 1, (255, 255, 255)))
        players_name_text.append(font.render(gamers[i], 1, (0, 0, 0)))

        player = players(person_name[i])
        player_idel.append(player.anim_run("Run")[0])
        player_idel_max_anim_count.append(player.anim_run("Run")[1])
        player_jump.append(player.anim_run("High_Jump")[0])
        player_jump_max_anim_count.append(player.anim_run("High_Jump")[1])
        player_bust_anim.append(player.anim_run("Explosion_")[0])
        player_bust_count_max.append(player.anim_run("Explosion_")[1])
        pleer_anim_count_jump.append(0)
        player_bust_count.append(0)
        pleer_anim_count.append(0)
        player_last_scope.append([0, 0])
        player_gift.append(pygame.image.load(player_gift_patch[i]))
        player_gift_big.append(pygame.image.load(player_gift_big_patch[i]))

    win = True
    timer = 0
    pleer_win = "Тест"
    font_win_final = pygame.font.SysFont(None, 80)

    while True:

        if win:
            bd_players = Table("bd.json")

            players_info = []

            for i in range(0, 5):
                info = bd_players.get_person_data(persons[i])
                players_info.append(info)

            screen.blit(bg, (bg_x, 0))
            screen.blit(bg, (bg_x + 360, 0))
            screen.blit(bg2, (0, 0))

            player_text_pos = [0, 0, 0, 0, 0]
            player_win_text_pos = [0, 0, 0, 0, 0]
            player_gift_big_pos = [0, 0, 0, 0, 0]

            text_pos = [[-50, 75], [-50, 75], [-60, 75], [-53, 75], [-53, 75]]
            win_text_pos = [[-85, 135], [-83, 150], [-90, 160], [-90, 155], [-87, 150]]
            gift_big_pos = [[-115, 160], [-117, 182], [-122, 190], [-120, 185], [-120, 180]]
            for i in range(0, 5):
                if players_info[i]['points'] + players_info[i]['chat'] > 130:
                    player_text_pos[i] = text_pos[i][0]
                    player_win_text_pos[i] = win_text_pos[i][0]
                    player_gift_big_pos[i] = gift_big_pos[i][0]
                else:
                    player_text_pos[i] = text_pos[i][1]
                    player_win_text_pos[i] = win_text_pos[i][1]
                    player_gift_big_pos[i] = gift_big_pos[i][1]


            text_position = [135, 200, 260, 325, 390]
            scrin_pos = [[80, 90 , 150, 145, 143],
                         [140, 150, 215, 210, 207],
                         [205, 215, 275, 270, 270],
                         [265, 275, 340, 335, 335],
                         [330, 340, 405, 400, 398]]
            for i in range(0,5):
                # Отрисрвка персонажей и текста
                if player_last_scope[i][0] == players_info[i]['points']:
                    screen.blit(pygame.image.load(player_idel[i][pleer_anim_count[i]]), (players_info[i]['points'] + players_info[i]['chat'], scrin_pos[i][0]))
                    pleer_anim_count_jump[i] = 0
                    player_bust_count[i] = 0
                else:
                    screen.blit(pygame.image.load(player_bust_anim[i][player_bust_count[i]]), (players_info[i]['points'] + players_info[i]['chat'] - 20, scrin_pos[i][1]))
                    screen.blit(pygame.image.load(player_jump[i][pleer_anim_count_jump[i]]), (players_info[i]['points'] + players_info[i]['chat'], scrin_pos[i][0]))
                    pleer_anim_count[i] = 0
                screen.blit(players_name_text[i], (players_info[i]['points'] + players_info[i]['chat'] + player_text_pos[i], scrin_pos[i][2]))
                screen.blit(player_gift[i], (players_info[i]['points'] + players_info[i]['chat'] + player_win_text_pos[i], scrin_pos[i][3]))
                screen.blit(player_gift_big[i], (players_info[i]['points'] + players_info[i]['chat'] + player_gift_big_pos[i], scrin_pos[i][4]))
                player_text_scope = font_scope.render(str(players_info[i]['chat'] + players_info[i]['points']), 1 , (255, 255, 255))
                screen.blit(player_text_scope, (333, text_position[i]))
                screen.blit(players_sum_win_text[i], (330, text_position[i] + 15))

                # Победа
                if players_info[i]['points'] + players_info[i]['chat'] > 270:
                    pleer_win = gamers[i]
                    win = players_info[i]['victories']
                    bd_players.set_person_victories(persons[i], win + 1)
                    players_sum_win_text[i] = font_win.render(str(players_info[i]['victories']), 1 , (255, 255, 255))
                    win = False
                # Анимации
                if pleer_anim_count[i] == player_idel_max_anim_count[i]:
                    pleer_anim_count[i] = 0
                else:
                    pleer_anim_count[i] += 1
                if player_bust_count[i] == player_bust_count_max[i]:
                    player_bust_count[i] = 0
                else:
                    player_bust_count[i] += 1
                if pleer_anim_count_jump[i] == player_jump_max_anim_count[i]:
                    pleer_anim_count_jump[i] = 0
                    player_last_scope[i][0] = players_info[i]['points']
                else:
                    pleer_anim_count_jump[i] += 1

            bg_x -= 2
            if bg_x == -360:
                bg_x = 0

            if timer_random > 300:
                bd_players = Table("bd.json")
                random_index = random.randint(0, len(person) - 1)
                x = person[random_index]
                coinss = bd_players.get_person_data(x)['chat']
                bd_players.set_person_chat(x, 2 + coinss)
                timer_random = 0
            else:
                timer_random += 1

        # Экран выигрыша
        else:
            screen.blit(bg, (0, 0))
            winer1 = font_win_final.render("WIN" , 1 , (0,0,0))
            winer = font_win_final.render(pleer_win , 1 , (0,0,0))
            screen.blit(winer1, (120, 100))
            screen.blit(winer, (50, 200))
            pygame.display.update()

            for per in person:
                bd_players.set_person_points(per, 0)
                bd_players.set_person_chat(per, 0)
            timer +=1
            if timer > 100:
                timer = 0
                win = True

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick(12)

# run()



