import pygame;
import random;

from sys import exit;
from random import randint;

largura = 1000;
altura = 600;

p = 1;
y = 200;
velocidade = 2;

janela = pygame.display.set_mode((largura, altura));

while True:
    janela.fill([0]*3)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit ();
    oponente = pygame.draw.rect(janela, (0, 0, 225), (100, y, 25, 180));
    if p == 1:
        y -= velocidade;
        if y == 0:
            p = 2;
    if p == 2:
        y += velocidade;
        if y == 420:
            p = 1;
    pygame.display.update();
pygame.quit ();