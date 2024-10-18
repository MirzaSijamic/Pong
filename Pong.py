import pygame, sys, random

def pomjeranje():
    global brzina_loptice_x, brzina_loptice_y, score_igraca1, score_igraca2, score_timer
    loptica.x += brzina_loptice_x
    loptica.y += brzina_loptice_y

    if loptica.y <= 0 or loptica.y >= visina_ekrana:
        brzina_loptice_y *= -1

    if loptica.x <= 0:
        score_igraca1 += 1
        score_timer = pygame.time.get_ticks()

    if loptica.x >= sirina_ekrana:
        score_igraca2 += 1
        score_timer = pygame.time.get_ticks()

    if loptica.colliderect(igrac1) or loptica.colliderect(igrac2):
        brzina_loptice_x*=-1

def pozicija():
    if igrac1.top <= 0:
        igrac1.top = 0
    if igrac1.bottom >= visina_ekrana:
        igrac1.bottom = visina_ekrana

def AI():
    if igrac2.top < loptica.y:
        igrac2.top += brzina_igraca2
    if igrac2.top > loptica.y:
        igrac2.top -= brzina_igraca2
    if igrac2.top <= 0:
        igrac2.top = 0
    if igrac2.bottom >= visina_ekrana:
        igrac2.bottom = visina_ekrana

def restart():
    global brzina_loptice_x, brzina_loptice_y, score_timer

    trenutni_timer = pygame.time.get_ticks() 

    loptica.center=(sirina_ekrana/2,visina_ekrana/2)

    if trenutni_timer - score_timer < 700:
        tri = game_font.render("3", True, light_grey)
        ekran.blit(tri,(sirina_ekrana/2-10, visina_ekrana/2+20))

    if 700 < trenutni_timer - score_timer < 1400:
        dva = game_font.render("2", True, light_grey)
        ekran.blit(dva,(sirina_ekrana/2-10, visina_ekrana/2+20))

    if 1400< trenutni_timer - score_timer < 2100:
        jedan = game_font.render("1", True, light_grey)
        ekran.blit(jedan,(sirina_ekrana/2-10, visina_ekrana/2+20))

    if trenutni_timer - score_timer < 2100:
        brzina_loptice_x = 0
        brzina_loptice_y = 0
    else:
        brzina_loptice_y =7 * random.choice((1,-1))
        brzina_loptice_x =7 * random.choice((1,-1))
        score_timer = None


pygame.init()
clock = pygame.time.Clock()

sirina_ekrana=1280
visina_ekrana=800
ekran = pygame.display.set_mode((sirina_ekrana,visina_ekrana))
pygame.display.set_caption('Maturski Pong')


loptica = pygame.Rect(sirina_ekrana/2-15, visina_ekrana/2-15, 30, 30)
igrac1 = pygame.Rect(sirina_ekrana-20, visina_ekrana/2-70, 10, 140)
igrac2 = pygame.Rect(10, visina_ekrana/2-70, 10, 140)

pozadina = pygame.Color('grey12')
light_grey = (200,200,200)

brzina_loptice_x = 7
brzina_loptice_y = 7
brzina_igraca = 0
brzina_igraca2 = 6

score_igraca1 = 0
score_igraca2 = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

score_timer = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                brzina_igraca += 7
            if event.key == pygame.K_UP:
                brzina_igraca -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                brzina_igraca -= 7
            if event.key == pygame.K_UP:
                brzina_igraca += 7

    pomjeranje()
    pozicija()
    AI()
    igrac1.y += brzina_igraca  

    ekran.fill(pozadina)
    pygame.draw.rect(ekran, light_grey, igrac1)
    pygame.draw.rect(ekran, light_grey, igrac2)
    pygame.draw.ellipse(ekran, light_grey, loptica)
    pygame.draw.aaline(ekran, light_grey, (sirina_ekrana/2,0), (sirina_ekrana/2,visina_ekrana))

    if score_timer:
        restart()

    tekst_igraca1 = game_font.render(f"{score_igraca1}", True, light_grey)
    ekran.blit(tekst_igraca1,(660,370))
    tekst_igraca2 = game_font.render(f"{score_igraca2}", True, light_grey)
    ekran.blit(tekst_igraca2,(600,370))

    pygame.display.flip()
    clock.tick(60)
