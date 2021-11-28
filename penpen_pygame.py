import pygame
import sys
import random
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIME = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 192, 0)
RED = (255, 0, 0)
PINK = (255, 128, 255)
VIOLET = (255, 0, 224)

img_bg = [ #배경1
    pygame.image.load("image_penpen/chip00.png"),
    pygame.image.load("image_penpen/chip01.png"),
    pygame.image.load("image_penpen/chip02.png"),
    pygame.image.load("image_penpen/chip03.png"),
    pygame.image.load("image_penpen/chip04.png"),#생명 아이템
    pygame.image.load("image_penpen/chip15.png")
]
img_bg2=[ #배경2
    pygame.image.load("image_penpen/chip10.png"),
    pygame.image.load("image_penpen/chip11.png"),
    pygame.image.load("image_penpen/chip12.png"),
    pygame.image.load("image_penpen/chip13.png"),
    pygame.image.load("image_penpen/chip14.png"),
    pygame.image.load("image_penpen/chip15.png") #신발 아이템
]
img_bg3=[ #배경3
    pygame.image.load("image_penpen/chip20.png"),
    pygame.image.load("image_penpen/chip21.png"),
    pygame.image.load("image_penpen/chip22.png"),
    pygame.image.load("image_penpen/chip23.png"),
    pygame.image.load("image_penpen/chip24.png"),
    pygame.image.load("image_penpen/chip25.png") #신발 아이템
]
img_pen = [
    pygame.image.load("image_penpen/pen00.png"),
    pygame.image.load("image_penpen/pen01.png"),
    pygame.image.load("image_penpen/pen02.png"),
    pygame.image.load("image_penpen/pen03.png"),
    pygame.image.load("image_penpen/pen04.png"),
    pygame.image.load("image_penpen/pen05.png"),
    pygame.image.load("image_penpen/pen06.png"),
    pygame.image.load("image_penpen/pen07.png"),
    pygame.image.load("image_penpen/pen08.png"),
    pygame.image.load("image_penpen/pen09.png"),
    pygame.image.load("image_penpen/pen10.png"),
    pygame.image.load("image_penpen/pen11.png"),
    pygame.image.load("image_penpen/pen_face.png")
]
img_red = [
    pygame.image.load("image_penpen/red00.png"),
    pygame.image.load("image_penpen/red01.png"),
    pygame.image.load("image_penpen/red02.png"),
    pygame.image.load("image_penpen/red03.png"),
    pygame.image.load("image_penpen/red04.png"),
    pygame.image.load("image_penpen/red05.png"),
    pygame.image.load("image_penpen/red06.png"),
    pygame.image.load("image_penpen/red07.png"),
    pygame.image.load("image_penpen/red08.png"),
    pygame.image.load("image_penpen/red09.png"),
    pygame.image.load("image_penpen/red10.png"),
    pygame.image.load("image_penpen/red11.png"),
    pygame.image.load("image_penpen/pen_face.png")    
]

img_fire = [ #불의정령
    pygame.image.load("image_penpen/f00.png"),
    pygame.image.load("image_penpen/f01.png"),
    pygame.image.load("image_penpen/f02.png"),
    pygame.image.load("image_penpen/f03.png"),
    pygame.image.load("image_penpen/f04.png"),
    pygame.image.load("image_penpen/f05.png"),
    pygame.image.load("image_penpen/f06.png"),
    pygame.image.load("image_penpen/f07.png"),
    pygame.image.load("image_penpen/f08.png"),
    pygame.image.load("image_penpen/f09.png"),
    pygame.image.load("image_penpen/f10.png"),
    pygame.image.load("image_penpen/f11.png")
]


img_kuma = [
    pygame.image.load("image_penpen/kuma00.png"),
    pygame.image.load("image_penpen/kuma01.png"),
    pygame.image.load("image_penpen/kuma02.png")
]

img_firez = [ #불의 거인
    pygame.image.load("image_penpen/fz00.png"),
    pygame.image.load("image_penpen/fz01.png"),
    pygame.image.load("image_penpen/fz02.png"),
    pygame.image.load("image_penpen/fz03.png"),
    pygame.image.load("image_penpen/fz04.png"),
    pygame.image.load("image_penpen/fz05.png"),
    pygame.image.load("image_penpen/fz06.png"),
    pygame.image.load("image_penpen/fz07.png")
   
]

img_knight = [ #기사
    pygame.image.load("image_penpen/kn00.png"),
    pygame.image.load("image_penpen/kn01.png"),
    pygame.image.load("image_penpen/kn02.png"),
    pygame.image.load("image_penpen/kn03.png"),
    pygame.image.load("image_penpen/kn04.png"),
    pygame.image.load("image_penpen/kn05.png"),
    pygame.image.load("image_penpen/kn06.png"),
    pygame.image.load("image_penpen/kn07.png"),
    pygame.image.load("image_penpen/kn08.png"),
    pygame.image.load("image_penpen/kn09.png"),
    pygame.image.load("image_penpen/kn10.png"),
    pygame.image.load("image_penpen/kn11.png")

]
img_title = pygame.image.load("image_penpen/title.png")
img_ending = pygame.image.load("image_penpen/ending.png")

img_track=[
    pygame.image.load("image_penpen/track1.png"),
    pygame.image.load("image_penpen/track2.png"),
    pygame.image.load("image_penpen/track3.png"),
    pygame.image.load("image_penpen/track4.png"),
    pygame.image.load("image_penpen/track5.png"),
    pygame.image.load("image_penpen/track6.png"),
    pygame.image.load("image_penpen/track7.png"),
    pygame.image.load("image_penpen/track8.png"),
    pygame.image.load("image_penpen/track9.png")
]

img_kpen = [ #1스테이지 보스
    pygame.image.load("image_penpen/kpen00.png"),
    pygame.image.load("image_penpen/kpen01.png"),
    pygame.image.load("image_penpen/kpen02.png"),
    pygame.image.load("image_penpen/kpen03.png"),
    pygame.image.load("image_penpen/kpen04.png"),
    pygame.image.load("image_penpen/kpen05.png"),
    pygame.image.load("image_penpen/kpen06.png"),
    pygame.image.load("image_penpen/kpen07.png"),
    pygame.image.load("image_penpen/kpen08.png"),
    pygame.image.load("image_penpen/kpen09.png"),
    pygame.image.load("image_penpen/kpen10.png"),
    pygame.image.load("image_penpen/kpen11.png")
]

img_dragon = [ #드레곤
    pygame.image.load("image_penpen/d00.png"),
    pygame.image.load("image_penpen/d01.png"),
    pygame.image.load("image_penpen/d02.png"),
    pygame.image.load("image_penpen/d03.png"),
    pygame.image.load("image_penpen/d04.png"),
    pygame.image.load("image_penpen/d05.png"),
    pygame.image.load("image_penpen/d06.png"),
    pygame.image.load("image_penpen/d07.png"),
    pygame.image.load("image_penpen/d08.png"),
    pygame.image.load("image_penpen/d09.png"),
    pygame.image.load("image_penpen/d10.png"),
    pygame.image.load("image_penpen/d11.png")
    
]

img_gient = [ #거인
    pygame.image.load("image_penpen/g00.png"),
    pygame.image.load("image_penpen/g01.png"),
    pygame.image.load("image_penpen/g02.png"),
    pygame.image.load("image_penpen/g03.png"),
    pygame.image.load("image_penpen/g04.png"),
    pygame.image.load("image_penpen/g05.png"),
    pygame.image.load("image_penpen/g06.png"),
    pygame.image.load("image_penpen/g07.png"),
    pygame.image.load("image_penpen/g08.png"),
    pygame.image.load("image_penpen/g09.png"),
    pygame.image.load("image_penpen/g10.png"),
    pygame.image.load("image_penpen/g11.png")

]

img_golem = [ #골렘
    pygame.image.load("image_penpen/gl00.png"),
    pygame.image.load("image_penpen/gl01.png"),
    pygame.image.load("image_penpen/gl02.png"),
    pygame.image.load("image_penpen/gl03.png"),
    pygame.image.load("image_penpen/gl04.png"),
    pygame.image.load("image_penpen/gl05.png")

]

img_attackr=[pygame.image.load("image_penpen/atr1.png"),
             pygame.image.load("image_penpen/atr1.5.png"),
             pygame.image.load("image_penpen/atr2.png"),
             pygame.image.load("image_penpen/atr2.5.png"),
             pygame.image.load("image_penpen/atr3.png"),
             pygame.image.load("image_penpen/atr3.5.png")
]
img_attackl=[pygame.image.load("image_penpen/atl1.png"),
             pygame.image.load("image_penpen/atl1.5.png"),
             pygame.image.load("image_penpen/atl2.png"),
             pygame.image.load("image_penpen/atl2.5.png"),
             pygame.image.load("image_penpen/atl3.png"),
             pygame.image.load("image_penpen/atl3.5.png")
]
img_attacku=[pygame.image.load("image_penpen/atu1.png"),
             pygame.image.load("image_penpen/atu1.5.png"),
             pygame.image.load("image_penpen/atu2.png"),
             pygame.image.load("image_penpen/atu2.5.png"),
             pygame.image.load("image_penpen/atu3.png"),
             pygame.image.load("image_penpen/atu3.5.png")
]
img_attackd=[pygame.image.load("image_penpen/atd1.png"),
             pygame.image.load("image_penpen/atd1.5.png"),
             pygame.image.load("image_penpen/atd2.png"),
             pygame.image.load("image_penpen/atd2.5.png"),
             pygame.image.load("image_penpen/atd3.png"),
             pygame.image.load("image_penpen/atd3.5.png")
]

img_boss_hp=pygame.image.load("image_penpen/hp.png")# 보스 체력바

img_boss_skx=pygame.image.load("image_penpen/boss_skx.png")
img_boss_sky=pygame.image.load("image_penpen/boss_sky.png")# 보스 스킬

img_bs=[pygame.image.load("image_penpen/effact/water1.png"),# 보스가 맞는 효과
        pygame.image.load("image_penpen/effact/water2.png"),
        pygame.image.load("image_penpen/effact/water3.png"),
        pygame.image.load("image_penpen/effact/water4.png"),
        pygame.image.load("image_penpen/effact/water5.png"),
        pygame.image.load("image_penpen/effact/water6.png"),
        pygame.image.load("image_penpen/effact/water7.png"),
        pygame.image.load("image_penpen/effact/water8.png"),
        pygame.image.load("image_penpen/effact/water9.png"),
        pygame.image.load("image_penpen/effact/water10.png"),
        pygame.image.load("image_penpen/effact/water11.png"),
        pygame.image.load("image_penpen/effact/water12.png"),
        pygame.image.load("image_penpen/effact/water13.png"),
        pygame.image.load("image_penpen/effact/water14.png"),
        pygame.image.load("image_penpen/effact/water15.png")
        
        
    ]



se_candy = None #사탕 효과음
boss_a=None #보스 맞는 효과음
boss_d=None #보스 죽는 효과음

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0, 1, 0, 2]
BLINK = [(255, 255, 255), (255, 255, 192), (255, 255, 128), (255, 224, 64), (255, 255, 128), (255, 255, 192)]

idx = 0
tmr = 0
stage = 6
score = 0
nokori = 3
candy = 0

pen_x = 0
pen_y = 0
pen_d = 0
pen_a = 0

red_x = 0
red_y = 0
red_d = 0
red_a = 0
red_sx = 0
red_sy = 0

kuma_x = 0
kuma_y = 0
kuma_d = 0
kuma_a = 0
kuma_sx = 0
kuma_sy = 0
kuma_sd = 0

kpen_x = 0 #보스 전역변수
kpen_y = 0
kpen_d = 0
kpen_a = 0
kpen_sx = 0
kpen_sy = 0
kpen_sd=0

track_x=0 #장애물 전역변수
track_y=0
track_a=0
track_d=0
track_sx=0
track_sy=0
track_sd=0

at_x=pen_x #공격 전역변수
at_y=pen_y
at_r=0
at_l=0
at_u=0
at_d=0

sk_x=0
sk_y=0

bs_x=0
bs_y=0
bs_a=0

boss_hp=0 #보스 피통

map_data = []  # 미로 용 리스트


def set_stage():  # 스테이지 데이터 설정
    global map_data, candy, skill
    global red_sx, red_sy
    global kuma_sx, kuma_sy, kuma_sd
    global track_sx, track_sy, track_sd
    global boss_hp
    global kpen_sx, kpen_sy, kpen_sd

    if stage == 1:
        map_data = [
            [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
            [0, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 0],
            [0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0],
            [0, 3, 1, 1, 4, 0, 0, 3, 1, 1, 3, 0],
            [0, 3, 2, 2, 3, 0, 0, 3, 2, 2, 3, 0],
            [0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0],
            [0, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 0],
            [0, 2, 3, 3, 2, 0, 0, 2, 3, 3, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 30
        red_sx = 630
        red_sy = 450
        kuma_sd = -1
        track_sx=270 #장애물 위치
        track_sy=270
        kpen_sd=-1 #보스 출현 x
        
        

    if stage == 2:
        map_data = [
            [0,1,1,1,1,1,1,1,1,1,1,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,1,1,2,2,2,2,0],
            [0,2,2,2,2,1,1,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        candy = 1
        red_sx = 630
        red_sy = 450
        kpen_sx = 150
        kpen_sy = 270
        kuma_sx = 330
        kuma_sy = 270
        kuma_sd = DIR_RIGHT
        track_sx=-100
        track_sy=-100
        boss_hp=50
        kpen_sd=1 #보스 출현O

    if stage == 3:
        map_data = [
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 1, 3, 1, 2, 2, 3, 3, 3, 4, 0],
            [0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 0],
            [0, 1, 1, 2, 0, 2, 2, 0, 1, 1, 2, 0],
            [0, 3, 3, 3, 1, 1, 1, 0, 3, 3, 3, 0],
            [0, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 22
        red_sx = 630
        red_sy = 450
        kuma_sx = 330
        kuma_sy = 270
        kuma_sd = DIR_RIGHT
        kpen_sd=-1
        
        

    if stage == 4:
        map_data = [
            [0,1,1,1,1,1,1,1,1,1,1,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,0,2,2,2,2,2,2,0,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,0,2,2,2,2,2,2,0,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        candy = 1
        red_sx = 150
        red_sy = 270
        kuma_sx = 510
        kuma_sy = 270
        kuma_sd = DIR_UP
        kpen_sx = 150
        kpen_sy = 270
        kpen_sd=1
        boss_hp=100

    if stage == 5:
        map_data = [
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 0, 3, 3, 4, 3, 3, 3, 3, 3, 0],
            [0, 2, 0, 3, 0, 1, 3, 3, 1, 0, 3, 0],
            [0, 2, 0, 3, 0, 3, 3, 3, 3, 0, 3, 0],
            [0, 2, 1, 3, 1, 1, 3, 3, 1, 1, 3, 0],
            [0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        candy = 39
        red_sx = 630
        red_sy = 450
        kuma_sx = 390
        kuma_sy = 210
        kuma_sd = DIR_RIGHT
        kpen_sd=-1

    if stage == 6:
        map_data = [
            [0,1,1,1,1,1,1,1,1,1,1,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,2,2,2,2,2,2,2,2,2,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        candy=1
        kpen_sx = 150
        kpen_sy = 270
        kpen_sd=1
        boss_hp=150
    

def set_chara_pos():  # 캐릭터 시작 위치
    global pen_x, pen_y, pen_d, pen_a
    global red_x, red_y, red_d, red_a
    global kuma_x, kuma_y, kuma_d, kuma_a
    global track_x, track_y, track_a, track_d
    global at_x, at_y, at_a, at_d
    global kpen_x, kpen_y, kpen_d, kpen_a
    pen_x = 90
    pen_y = 90
    pen_d = DIR_DOWN
    pen_a = 3
    
    red_x = red_sx
    red_y = red_sy
    red_d = DIR_DOWN
    red_a = 3
    
    kuma_x = kuma_sx
    kuma_y = kuma_sy
    kuma_d = kuma_sd
    kuma_a = 0
    track_x= track_sx
    track_y=track_sy
    track_a=3
    track_d=track_sd
    
    kpen_x=kpen_sx
    kpen_y=kpen_sy
    kpen_d=kpen_sd
    kpen_a=0

    at_x=pen_x
    at_y=pen_y
    at_d=pen_d
    at_a=pen_a



    
    

def draw_txt(scrn, txt, x, y, siz, col):  # 그림자 포함 문자
    fnt = pygame.font.Font(None, siz * 2)
    sur = fnt.render(txt, True, BLACK)
    x = x - sur.get_width() / 2
    y = y - sur.get_height() / 2
    scrn.blit(sur, [x + 2, y + 2])
    sur = fnt.render(txt, True, col)
    scrn.blit(sur, [x, y])


def draw_screen(scrn):
    global at_x, at_y, at_a, at_d, sk_x, sk_y, at_r, at_l, at_u, at_d, bs_x, bs_y, bs_a
    speed=10# 게임 화면 그리기
    for y in range(9):
        for x in range(12):
            scrn.blit(img_bg[map_data[y][x]], [x * 60, y * 60])
            if stage==3 or stage==4:
                scrn.blit(img_bg2[map_data[y][x]], [x * 60, y * 60])
            if stage==5 or stage==6:
                scrn.blit(img_bg3[map_data[y][x]], [x * 60, y * 60])
    scrn.blit(img_track[track_a],[track_x - 30, track_y - 30])
                
    scrn.blit(img_pen[pen_a], [pen_x - 30, pen_y - 30])
    if stage==1 or stage==2:
        scrn.blit(img_red[red_a], [red_x - 30, red_y - 30])
    if stage==3 or stage==4:
        scrn.blit(img_knight[red_a], [red_x - 30, red_y - 30])
    if stage==5 or stage==6:
        scrn.blit(img_fire[red_a], [red_x - 30, red_y - 30])
    
    if kpen_sd != -1 and stage==2:
        scrn.blit(img_kpen[kpen_a], [kpen_x - 30, kpen_y - 30])
    if stage==4:
       scrn.blit(img_gient[kpen_a], [kpen_x - 84, kpen_y - 100])
    if stage==6:
        scrn.blit(img_dragon[kpen_a], [kpen_x - 55, kpen_y - 100])
        
    if kuma_sd != -1 and (stage==1 or stage==2):
        scrn.blit(img_kuma[kuma_a], [kuma_x - 30, kuma_y - 30])
    if stage==3 or stage==4:
        scrn.blit(img_golem[kuma_a], [kuma_x - 30, kuma_y - 45])
    
    if stage==5 or stage==6:
        scrn.blit(img_firez[kuma_a], [kuma_x - 30, kuma_y - 45])
    

    if stage==1 or stage==3 or stage==5:
        draw_txt(scrn, "SCORE " + str(score), 200, 30, 30, WHITE)
    if stage==2 or stage==4 or stage==6:
        
        for j in range(boss_hp):
            scrn.blit(img_boss_hp, [200 + j * 10, 45])
        draw_txt(scrn, "BOSS STAGE " + str(stage), 520, 30, 30, RED) #보스 스테이지 따로표시
        draw_txt(scrn, "BOSS HP X  " + str(boss_hp), 150, 30, 30, PINK) #보스 체력 표시
    else:
        draw_txt(scrn, "STAGE " + str(stage), 520, 30, 30, LIME)
    for i in range(nokori):
        scrn.blit(img_pen[12], [60 + i * 50, 500])
        
    at_x=pen_x
    at_y=pen_y

    

    sk_x=400
    sk_y=310

   
    if stage==2 or stage==4 or stage==6 or stage==1: #보스 스테이지

    
        

        if key[K_z]==1 and key[K_RIGHT]==1: #펭귄 공격 모듈
            for x in range(5):
                at_x=at_x+50
                scrn.blit(img_attackr[at_r],[at_x-30, at_y-30])
                bs_x=pen_x
                bs_y-pen_y
                scrn.blit(img_bs[bs_a],[pen_x-60, pen_y-94])
        
        elif key[K_z]==1 and key[K_LEFT]==1:
            for x in range(5):
                at_x=at_x-50
                scrn.blit(img_attackl[at_l],[at_x-30, at_y-30])
                bs_x=pen_x
                bs_y-pen_y
                scrn.blit(img_bs[bs_a],[pen_x-14, pen_y-94])

        elif key[K_z]==1 and key[K_UP]==1:
            for y in range(5):
                at_y=at_y-50
                scrn.blit(img_attacku[at_u],[at_x-30, at_y-30])
                bs_x=pen_x
                bs_y-pen_y
                scrn.blit(img_bs[bs_a],[pen_x-44, pen_y-90])

        elif key[K_z]==1 and key[K_DOWN]==1:
            for y in range(5):
                at_y=at_y+50
                scrn.blit(img_attackd[at_d],[at_x-30, at_y-30])
                bs_x=pen_x
                bs_y-pen_y
                scrn.blit(img_bs[bs_a],[pen_x-44, pen_y-90])

        if abs(kpen_x - at_x) <= 100 and abs(kpen_y - at_y) <= 100:
            bs_x=kpen_x
            bs_y=kpen_y
            scrn.blit(img_bs[bs_a],[bs_x-30, bs_y-30])




        



def check_wall(cx, cy, di, dot):  # 각 방향에 벽 존재 여부 확인
    chk = False
    if di == DIR_UP:
        mx = int((cx - 30) / 60)
        my = int((cy - 30 - dot) / 60)
        if map_data[my][mx] <= 1:  # 좌상
            chk = True
        mx = int((cx + 29) / 60)
        if map_data[my][mx] <= 1:  # 우상
            chk = True
    if di == DIR_DOWN:
        mx = int((cx - 30) / 60)
        my = int((cy + 29 + dot) / 60)
        if map_data[my][mx] <= 1:  # 좌하
            chk = True
        mx = int((cx + 29) / 60)
        if map_data[my][mx] <= 1:  # 우하
            chk = True
    if di == DIR_LEFT:
        mx = int((cx - 30 - dot) / 60)
        my = int((cy - 30) / 60)
        if map_data[my][mx] <= 1:  # 좌상
            chk = True
        my = int((cy + 29) / 60)
        if map_data[my][mx] <= 1:  # 좌하
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx + 29 + dot) / 60)
        my = int((cy - 30) / 60)
        if map_data[my][mx] <= 1:  # 우상
            chk = True
        my = int((cy + 29) / 60)
        if map_data[my][mx] <= 1:  # 우하
            chk = True
    return chk

def track(): #장애물 함수
    global idx, tmr, track_x, track_y, track_a, track_d
    if idx==1:
        track_a = ANIMATION[tmr % 4]
    if abs(track_x - pen_x) <= 60 and abs(track_y - pen_y) <= 60:
        idx = 2
        tmr = 0
def at():
    global at_x, at_y, at_r, at_l, at_u, at_d, idx, tmr
    if idx==1:
        at_r=ANIMATION[tmr % 4]
        at_l=ANIMATION[tmr % 4]
        at_u=ANIMATION[tmr % 4]
        at_d=ANIMATION[tmr % 4]

def bs():
    global bs_x, bs_y, idx, tmr,bs_a
    if idx==1:
        bs_a=ANIMATION[tmr % 4]


def move_penpen(key):  # 펜펜 움직이기
    global score, candy, nokori,  pen_x, pen_y, pen_d, pen_a, at_x,at_y,at_a,at_d
    if key[K_UP] == 1:
        pen_d = DIR_UP
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y - 20
           
    elif key[K_DOWN] == 1:
        pen_d = DIR_DOWN
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y + 20
    elif key[K_LEFT] == 1:
        pen_d = DIR_LEFT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x - 20
    elif key[K_RIGHT] == 1:
        pen_d = DIR_RIGHT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x + 20
    pen_a = pen_d * 3 + ANIMATION[tmr % 4]
    mx = int(pen_x / 60)
    my = int(pen_y / 60)
    if map_data[my][mx] == 4:
        map_data[my][mx] = 2
        nokori=nokori+1
        se_candy.play()
    if map_data[my][mx] == 3:  # 사탕에 닿았는가?
        score = score + 100
        map_data[my][mx] = 2
        candy = candy - 1
        se_candy.play()                


def move_enemy():  # 레드 움직이기
    global idx, tmr, red_x, red_y, red_d, red_a
    speed = 10
    if red_x % 60 == 30 and red_y % 60 == 30:
        red_d = random.randint(0, 6)
        if red_d >= 4:
            if pen_y < red_y:
                red_d = DIR_UP
            if pen_y > red_y:
                red_d = DIR_DOWN
            if pen_x < red_x:
                red_d = DIR_LEFT
            if pen_x > red_x:
                red_d = DIR_RIGHT
            if track_y < red_y:
                red_d = DIR_RIGHT
            if track_y > red_y:
                red_d = DIR_LEFT
            if track_x < red_x:
                red_d = DIR_UP
            if track_x > red_x:
                red_d = DIR_DOWN
    if red_d == DIR_UP:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y - speed
    if red_d == DIR_DOWN:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y + speed
    if red_d == DIR_LEFT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x - speed
    if red_d == DIR_RIGHT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x + speed
    red_a = red_d * 3 + ANIMATION[tmr % 4]
    if abs(red_x - pen_x) <= 40 and abs(red_y - pen_y) <= 40:
        idx = 2
        tmr = 0




def move_enemy3():  # 스테이지2 보스 움직이기
    global idx, tmr, kpen_x, kpen_y, kpen_d, kpen_a, boss_hp, candy, boss_a, boss_d
    speed = 15
    if kpen_sd == -1:
        return
    if kpen_x % 60 == 30 and kpen_y % 60 == 30:
        kpen_d = random.randint(0, 6)
        if kpen_d >= 4:
            if pen_y < kpen_y:
                kpen_d = DIR_UP
            if pen_y > kpen_y:
                kpen_d = DIR_DOWN
            if pen_x < kpen_x:
                kpen_d = DIR_LEFT
            if pen_x > kpen_x:
                kpen_d = DIR_RIGHT
    if kpen_d == DIR_UP:
        if check_wall(kpen_x, kpen_y, kpen_d, speed) == False:
            kpen_y = kpen_y - speed
    if kpen_d == DIR_DOWN:
        if check_wall(kpen_x, kpen_y, kpen_d, speed) == False:
            kpen_y = kpen_y + speed
    if kpen_d == DIR_LEFT:
        if check_wall(kpen_x, kpen_y, kpen_d, speed) == False:
            kpen_x = kpen_x - speed
    if kpen_d == DIR_RIGHT:
        if check_wall(kpen_x, kpen_y, kpen_d, speed) == False:
            kpen_x = kpen_x + speed
    kpen_a = kpen_d * 3 + ANIMATION[tmr % 4]
    if stage==2:
        if abs(kpen_x - pen_x) <= 55 and abs(kpen_y - pen_y) <= 55:
            idx = 2
            tmr = 0
    elif stage==4:
        if abs(kpen_x - pen_x) <= 45 and abs(kpen_y - pen_y) <= 45:
            idx = 2
            tmr = 0
    elif stage==6:
        if abs(kpen_x - pen_x) <= 45 and abs(kpen_y - pen_y) <= 45:
            idx = 2
            tmr = 0
        
    if abs(kpen_x - at_x) <= 110 and abs(kpen_y - at_y) <= 110 or abs(kpen_x - at_x) <= 65 and abs(kpen_y - at_y) <= 65:
        boss_hp=boss_hp-1
        boss_a.play()
        if boss_hp==0:
            boss_d.play()
            kpen_x=-300
            kpen_y=-300
            if stage==2 or stage==4 or stage==6:
                candy=0
                
        


def move_enemy2():  # 쿠마곤 움직이기
    global idx, tmr, kuma_x, kuma_y, kuma_d, kuma_a
    speed = 5
    if kuma_sd == -1:
        return
    if kuma_d == DIR_UP:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_y = kuma_y - speed
        else:
            kuma_d = DIR_DOWN
    elif kuma_d == DIR_DOWN:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_y = kuma_y + speed
        else:
            kuma_d = DIR_UP
    elif kuma_d == DIR_LEFT:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_x = kuma_x - speed
        else:
            kuma_d = DIR_RIGHT
    elif kuma_d == DIR_RIGHT:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_x = kuma_x + speed
        else:
            kuma_d = DIR_LEFT
    kuma_a = ANIMATION[tmr % 4]
    if stage==5 or stage==6:
        kuma_a = kuma_a*2+ANIMATION[tmr % 4]
    if abs(kuma_x - pen_x) <= 40 and abs(kuma_y - pen_y) <= 40:
        idx = 2
        tmr = 0


def main():  # 메인 루프
    global key, koff, idx, tmr, stage, score, nokori, se_candy, boss_hp, boss_a, boss_d
    pygame.init()
    pygame.display.set_caption("아슬아슬 펭귄 미로")
    screen = pygame.display.set_mode((720, 540))
    clock = pygame.time.Clock()
    se_candy = pygame.mixer.Sound("sound_penpen/candy.ogg")
    boss_a = pygame.mixer.Sound("sound_penpen/boss_a.ogg")
    boss_d = pygame.mixer.Sound("sound_penpen/boss_d.ogg")

    set_stage()
    set_chara_pos()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen = pygame.display.set_mode((720, 540), FULLSCREEN)
                if event.key == K_F2 or event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((720, 540))

        key = pygame.key.get_pressed()
        
        tmr = tmr + 1
        draw_screen(screen)

        if idx == 0:  # 타이틀 화면
            screen.blit(img_title, [360 - 320, 200 - 100])
            if tmr % 10 < 5:
                draw_txt(screen, "Press SPACE !", 360, 380, 30, YELLOW)
            if key[K_SPACE] == 1:
                stage = 1
                score = 0
                nokori = 3
                set_stage()
                set_chara_pos()
                idx = 1
                tmr = 0

        if idx == 1:# 게임 플레이
            move_penpen(key)
            move_enemy()
            move_enemy2()
            move_enemy3()
            track()
            at()
            bs()
            if candy == 0:
                idx = 4
                tmr = 0
            if tmr == 1:
                pygame.mixer.music.load("sound_penpen/bgm.ogg")
                pygame.mixer.music.play(-1)
                if stage==2 or stage==4 or stage==6:
                    pygame.mixer.music.load("sound_penpen/boss_stage.ogg")
                    pygame.mixer.music.play(-1)
                elif stage==3:
                    pygame.mixer.music.load("sound_penpen/stage3.ogg")
                    pygame.mixer.music.play(-1)
                elif stage==5:
                    pygame.mixer.music.load("sound_penpen/stage5.ogg")
                    pygame.mixer.music.play(-1)

        if idx == 2:  # 적에게 당했다
            draw_txt(screen, "MISS", 360, 270, 40, ORANGE)
            if tmr == 1:
                pygame.mixer.music.stop()
                nokori = nokori - 1
            if tmr == 5:
                pygame.mixer.music.load("sound_penpen/miss.ogg")
                pygame.mixer.music.play(0)
            if tmr == 50:
                if nokori == 0:
                    idx = 3
                    tmr = 0
                else:
                    set_chara_pos()
                    idx = 1
                    tmr = 0

        if idx == 3:  # 게임 오버
            draw_txt(screen, "GAME OVER", 360, 270, 40, RED)
            if tmr == 50:
                idx = 0

        if idx == 4:  # 스테이지 클리어
            if stage < 6:
                draw_txt(screen, "STAGE CLEAR", 360, 270, 40, PINK)
            else:
                draw_txt(screen, "ALL STAGE CLEAR!", 360, 270, 40, VIOLET)
            if tmr == 1:
                pygame.mixer.music.stop()
            if tmr == 5:
                pygame.mixer.music.load("sound_penpen/clear.ogg")
                if stage==2 or stage==4 or stage==6:
                    boss_d.play()
                    
                pygame.mixer.music.play(0)
            if tmr == 50:
                if stage < 6:
                    stage = stage + 1
                    set_stage()
                    set_chara_pos()
                    idx = 1
                    tmr = 0
                else:
                    idx = 5
                    tmr = 0

        if idx == 5:  # 엔딩
            if tmr < 60:
                xr = 8 * tmr
                yr = 6 * tmr
                pygame.draw.ellipse(screen, BLACK, [360 - xr, 270 - yr, xr * 2, yr * 2])
            else:
                pygame.draw.rect(screen, BLACK, [0, 0, 720, 540])
                screen.blit(img_ending, [360 - 120, 300 - 80])
                draw_txt(screen, "Congratulations!", 360, 160, 40, BLINK[tmr % 6])
            if tmr == 300:
                idx = 0
    

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
