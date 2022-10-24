import pygame;
import random;

from sys import exit;
from random import randint;

largura = 1000;
altura = 600;

y = 200;
p = y;
velocidade = 3;

janela = pygame.display.set_mode((largura, altura));

while True:
    janela.fill([0]*3)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit ();
    personagem = pygame.draw.rect(janela, (225, 0, 0), (900, p, 25, 180));
    comandos = pygame.key.get_pressed();
    if comandos [pygame.K_UP]:
        if p > 0:
            p -= velocidade;
        
    if comandos [pygame.K_DOWN]:
        if p < 420:
            p += velocidade;
    pygame.display.update();
pygame.quit ();