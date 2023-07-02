import pygame 
import sys
import random
import os

def caminho_arquivo(nome:str):
    caminho = os.path.dirname(os.path.realpath(__file__))
    caminhoImg = os.path.join(caminho, nome)
    return caminhoImg

# Inicialização do Pygame
pygame.init()

# Definindo as dimensões da janela
largura = 750
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Word Zapper")

# Definindo cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
LARANJA = (238, 118, 0)
MAGENTA = (139, 0, 139)
PRETO = (0, 0, 0)
VERDE = 0, 255, 0

# Definindo fonte e tamanho do texto
fonte = pygame.font.Font(caminho_arquivo('montserrat.ttf') , 20)
fonte2 = pygame.font.Font(None, 20)
fonte3 = pygame.font.Font(caminho_arquivo('montserrat.ttf') , 35)

# Carregando a imagem de fundo
fundo = pygame.image.load(caminho_arquivo("cenario.png")).convert()
fundo2 = pygame.image.load(caminho_arquivo("cenario2.png")).convert()
tiro = pygame.image.load(caminho_arquivo("tiro.png")).convert()

tempo = 60


def exibir_menu():
    tela.blit(fundo, (0, 0))
    
    # Desenha o título do jogo
    titulo_surface = fonte.render(" WORD ZAPPER ", fonte2, True, AZUL)
    tela.blit(titulo_surface, (largura // 2 - titulo_surface.get_width() // 2, altura // 30))

    titulo_surface = fonte.render(" SPATIAL ",fonte2, True, AZUL)
    tela.blit(titulo_surface, (largura // 2 - titulo_surface.get_width() // 2, altura // 8))
    
    # Desenha as opções do menu
    opcao1_surface = fonte.render("1 - INICIAR JOGO",fonte2, True, AZUL)
    tela.blit(opcao1_surface, (largura // 7 - opcao1_surface.get_width() // 4, altura // 4 + 150))
    
    opcao2_surface = fonte.render("2 - INFORMAÇÕES ",fonte2, True, AZUL)
    tela.blit(opcao2_surface, (largura // 0.9 - opcao2_surface.get_width() // 0.6, altura // 2 + 1))  
    
    
    opcao3_surface = fonte.render("3 - CONTROLES",fonte2, True, AZUL)
    tela.blit(opcao3_surface, (largura // 4 - opcao3_surface.get_width() // 2, altura // 2 + 200))

    opcao4_surface = fonte.render("4 - SAIR",fonte2, True, AZUL)
    tela.blit(opcao4_surface, (largura // 1.2 - opcao4_surface.get_width() // 1, altura // 2 + 200))

    pygame.display.update()

# Loop do menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    
                    return  # Retorna para iniciar o jogo 
                
                if event.key == pygame.K_2:
                    exibir_informacoes_jogo()  # Chama a função para exibir as informações do jogo
                
                if event.key == pygame.K_3:
                    exibir_controles()

                if event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_RETURN:             
                    exibir_menu()
                    return
                    
def exibir_informacoes_jogo():
    tela.blit(fundo2, (0, 0))
    
    
    tecla_info = fonte.render("BEM VINDO AO WORD ZAPPER SPATIAL!", fonte2, True, AZUL)
    tela.blit(tecla_info, ( 580 - tecla_info.get_width(), 50 - tecla_info.get_height()))


    setas_info = fonte.render(" O JOGO CONSISTE EM DESTRUIR UMA LETRA DA LISTA ROTATIVA; ", fonte2, True, AZUL)
    tela.blit(setas_info, (735 - setas_info.get_width(), 130 - setas_info.get_height()))


    teclas_info = fonte.render("A CADA LETRA DESTRUIDA, VAI REVELANDO A PALAVRA OCULTA;", fonte2, True, AZUL)
    tela.blit(teclas_info, ( 720 - teclas_info.get_width(), 210 - teclas_info.get_height()))

    vidas = fonte.render("O JOGADOR POSSUI 3 VIDAS!", fonte2, True, AZUL)
    tela.blit(vidas, (525 - vidas.get_width(), 290 - vidas.get_height()))

    enter = fonte.render("APÓS AS COLISÕES COM OS ASTEROIDES SERÁ GAME OVER;", fonte2, True, AZUL)
    tela.blit(enter, ( 700 - enter.get_width(), 370 - enter.get_height()))

    espaco_info = fonte.render(" O JOGADOR TAMBÉM PERDE APÓS ESGOTAR TEMPO;", fonte2, True, AZUL)
    tela.blit(espaco_info, ( 650 - espaco_info.get_width(), 450 - espaco_info.get_height()))

    esc_info = fonte.render("DIVIRTA - SE!", fonte2, True, AZUL)
    tela.blit(esc_info, ( 435 - esc_info.get_width(), 530 - esc_info.get_height()))

    pygame.display.update()
    
    # Espera por uma tecla ser pressionada para voltar ao menu
    pygame.event.clear()
    pygame.event.wait()


def exibir_controles():
    tela.blit(fundo2, (0, 0))

    teclas_info = fonte.render("CONTROLES", fonte2, True, AZUL)
    tela.blit(teclas_info, ( 450- teclas_info.get_width(), 320 - teclas_info.get_height()))
    # Carrega a imagem para exibir nas informações
    imagem_info = pygame.image.load(caminho_arquivo("setas.png")).convert()
    tela.blit(imagem_info, (750 - imagem_info.get_width(), 545 - imagem_info.get_height()))

    setas_info = fonte.render("    MOVE A NAVE    ", fonte2, True, AZUL)
    tela.blit(setas_info, (748 - setas_info.get_width(), 580 - setas_info.get_height()))

    tecla_info = pygame.image.load(caminho_arquivo("teclatiro.png")).convert()
    tela.blit(tecla_info, (238 - imagem_info.get_width(), 519 - imagem_info.get_height()))

    teclas_info = fonte.render(" TIROS LATERAIS", fonte2, True, AZUL)
    tela.blit(teclas_info, ( 185 - teclas_info.get_width(), 580 - teclas_info.get_height()))

    enter_info = pygame.image.load(caminho_arquivo("enter.png")).convert()
    tela.blit(enter_info, (208- imagem_info.get_width(), 90 - imagem_info.get_height()))

    enter = fonte.render("  RETORNA  ", fonte2, True, AZUL)
    tela.blit(enter, ( 125 - enter.get_width(), 175 - enter.get_height()))

    enter = fonte.render("  NAVEGAÇÃO DO   ", fonte2, True, AZUL)
    tela.blit(enter, ( 250 - enter.get_width(), 200 - enter.get_height()))

    enter = fonte.render("  MENU   ", fonte2, True, AZUL)
    tela.blit(enter, ( 250 - enter.get_width(), 225 - enter.get_height()))

    espaco_info = pygame.image.load(caminho_arquivo("espaço.png")).convert()
    tela.blit(espaco_info, (800 - imagem_info.get_width(), 85 - imagem_info.get_height()))

    espaco_info = fonte.render(" TIRO CENTRAL", fonte2, True, AZUL)
    tela.blit(espaco_info, ( 750- espaco_info.get_width(), 130 - espaco_info.get_height()))

    esc_info = pygame.image.load(caminho_arquivo("esc.png")).convert()
    tela.blit(esc_info, (500 - imagem_info.get_width(), 85 - imagem_info.get_height()))

    esc_info = fonte.render("FECHA TELA JOGO INICIADO", fonte2, True, AZUL)
    tela.blit(esc_info, ( 510 - esc_info.get_width(), 163 - esc_info.get_height()))

    pygame.display.update()
    
    # Espera por uma tecla ser pressionada para voltar ao menu
    pygame.event.clear()
    pygame.event.wait()

exibir_menu()

def exibir_mensagem():
    game_over_surface = fonte.render("COLISÃO COM ASTEROIDES - Game Over!", True, VERMELHO, 3000)
    tela.blit(game_over_surface, (largura // 2 - game_over_surface.get_width() // 2, altura // 2 - game_over_surface.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    return

def exibir_mensagem2():
    game_over_surface = fonte.render("PALAVRA COMPLETADA - VOCÊ VENCEU!", True, VERDE, 3000)
    tela.blit(game_over_surface, (largura // 2 - game_over_surface.get_width() // 2, altura // 2 - game_over_surface.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    exibir_menu()

def exibir_mensagem3():
    game_over_surface = fonte.render("ACABOU O TEMPO - Game Over!", True, VERMELHO, 3000)
    tela.blit(game_over_surface, (largura // 2 - game_over_surface.get_width() // 2, altura // 2 - game_over_surface.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    return
    
def reiniciar_jogo():
    
    global asteroides, letras_objetos, nave, projeteis, palavras, pontuacao, palavra_atual, palavra_oculta, mostrar_palavra, tempo_mostrar_palavra, cronometro, tempo_atual, tempo_total, game_over, vidas, jogar

    # Reinicializa todas as variáveis e objetos do jogo
    
    asteroides = []
    for _ in range(1):
        velocidade = random.uniform(1, 1)  # Velocidade aleatória para cada asteroide
        x = random.randint(-200, -200)  # Posição inicial aleatória no eixo X
        y = random.randint(-40, altura // 2 - 40)  # Posição inicial aleatória no eixo Y
        direcao = random.choice(['esquerda', 'direita', 'aleatoria'])  # Escolhe uma direção aleatória
        asteroide = Asteroide(x, y, velocidade, direcao)
        asteroides.append(asteroide)

    letras_objetos = []
    posicao_x = 800
    for letra in letras:
        letra_obj = Letra(letra, posicao_x, 60, 1)
        letras_objetos.append(letra_obj)
        posicao_x += espacamento_letras

    nave = NaveEspacial()
    projeteis = []

    palavras = carregar_palavras(caminho_arquivo("palavras.txt"))
    pontuacao = 0

    palavra_atual = random.choice(palavras).upper()
    palavra_oculta = "@" * len(palavra_atual)
    mostrar_palavra = True
    tempo_mostrar_palavra = 1

    tempo_atual = pygame.time.get_ticks()
    tempo_total = tempo_atual + cronometro * 1000

    game_over = False
    vidas = 3
    jogar = True

# Classe para representar a letra
class Letra:
    def __init__(self, letra, x, y, velocidade):
        self.letra = letra
        self.x = x
        self.y = y
        self.velocidade = 0.5
    
    def mover(self):
        self.x -= self.velocidade
    
    def desenhar(self):
        texto_surface = fonte.render(self.letra, fonte3, True, VERDE)
        tela.blit(texto_surface, (self.x, self.y))

# Classe para representar a nave
class NaveEspacial:
    def __init__(self):
        self.imagem = pygame.image.load(caminho_arquivo('nave.png'))
        self.imagem = pygame.transform.scale(self.imagem, (100, 80))
        self.rect = self.imagem.get_rect()
        self.rect.centerx = largura // 2
        self.rect.bottom = altura - 1
        self.velocidade = 1  
        self.movendo_esquerda = False
        self.movendo_direita = False
        self.movendo_cima = False
        self.movendo_baixo = False
    
    def mover(self):
        if self.movendo_esquerda:
            self.rect.x -= self.velocidade
            if self.rect.left < 0:
                self.rect.left = 1
        if self.movendo_direita:
            self.rect.x += self.velocidade
            if self.rect.right > largura:
                self.rect.right = largura
        if self.movendo_cima:
            self.rect.y -= self.velocidade
            if self.rect.top < 0:
                self.rect.top = 1
        if self.movendo_baixo:
            self.rect.y += self.velocidade
            if self.rect.bottom > altura:
                self.rect.bottom = altura
    
    def processar_eventos(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.movendo_esquerda = True
            elif event.key == pygame.K_RIGHT:
                self.movendo_direita = True
            elif event.key == pygame.K_UP:
                self.movendo_cima = True
            elif event.key == pygame.K_DOWN:
                self.movendo_baixo = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.movendo_esquerda = False
            elif event.key == pygame.K_RIGHT:
                self.movendo_direita = False
            elif event.key == pygame.K_UP:
                self.movendo_cima = False
            elif event.key == pygame.K_DOWN:
                self.movendo_baixo = False
                
    def atirar(self):
        projetil = Projetil(self.rect.centerx, self.rect.top,25)
        projeteis.append(projetil)
    
    def atirar_esquerda(self):
        projetil = Projetil(self.rect.left, self.rect.centery, 'esquerda')
        projeteis.append(projetil)

    def atirar_direita(self):
        projetil = Projetil(self.rect.right, self.rect.centery, 'direita')
        projeteis.append(projetil)

    
    def desenhar(self):
        tela.blit(self.imagem, self.rect)
        
direcao = ''

class Projetil:
    def __init__(self, x, y, direcao):
        self.rect = pygame.Rect(x - 25, y - 1, 20, 60)
        self.velocidade = 10
        self.direcao = direcao
        
        if self.direcao == 'esquerda':
            self.imagem = pygame.image.load(caminho_arquivo('tiroE.png'))
        elif self.direcao == 'direita':
            self.imagem = pygame.image.load(caminho_arquivo('tiroD.png'))
        else:
            self.imagem = pygame.image.load(caminho_arquivo('tiro.png'))

    def mover(self):
        if self.direcao == 'esquerda':
            self.rect.x -= self.velocidade
        elif self.direcao == 'direita':
            self.rect.x += self.velocidade
        else:
            self.rect.y -= self.velocidade

    def desenhar(self):
        tela.blit(self.imagem, self.rect)

        
class Asteroide:
    def __init__(self, x, y, velocidade, direcao='aleatoria'):
        self.imagem = pygame.image.load(caminho_arquivo('asteroide.png'))
        self.imagem = pygame.transform.scale(self.imagem, (60, 60))
        self.rect = self.imagem.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade = velocidade
        self.direcao = direcao

        if self.direcao == 'esquerda':
            self.velocidade *= -1  # Inverte a velocidade para mover para a esquerda
        elif self.direcao == 'aleatoria':
            # Define a direção aleatoriamente
            if random.randint(0, 1) == 0:
                self.velocidade *= -1  # Move para a esquerda
            else:
                self.velocidade *= 1  # Move para a direita


    def mover(self):
        self.rect.x += self.velocidade

        # Verifica se o asteroide saiu da tela e o reposiciona aleatoriamente
        if self.direcao in ['esquerda', 'aleatoria'] and self.rect.right < 0:
            self.rect.x = largura + random.randint(650, 800)
            self.rect.y = random.randint(200, altura)
        elif self.direcao in ['direita', 'aleatoria'] and self.rect.left > largura:
            self.rect.x = random.randint(-800, -650)
            self.rect.y = random.randint(200, altura)

        limite_altura = 400
        # Verifica se o asteroide ultrapassou o limite de altura
        if self.rect.y > limite_altura:
            self.rect.y = random.randint(200, limite_altura)

    def desenhar(self):
        tela.blit(self.imagem, self.rect)

# Função para carregar palavras de um arquivo de texto
def carregar_palavras(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras

# Função para atualizar a palavra oculta com a letra acertada
def atualizar_palavra_oculta(palavra, palavra_oculta, letra):
    nova_palavra_oculta = ""
    for i in range(len(palavra)):
        if palavra[i] == letra:
            nova_palavra_oculta += letra
        else:
            nova_palavra_oculta += palavra_oculta[i]
    return nova_palavra_oculta

# Inicialização da lista de asteroides
asteroides = []

# Criação dos objetos Asteroide
for _ in range(1):
    velocidade = random.uniform(1, 1)  # Velocidade aleatória para cada asteroide
    x = random.randint(-200, -200)  # Posição inicial aleatória no eixo X
    y = random.randint(-40, altura // 2 - 40)  # Posição inicial aleatória no eixo Y
    direcao = random.choice(['esquerda', 'direita', 'aleatoria'])  # Escolhe uma direção aleatória
    asteroide = Asteroide(x, y, velocidade, direcao)
    asteroides.append(asteroide)


# Lista de letras do alfabeto em sequência
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Espaçamento entre as letras
espacamento_letras = 30

# Posição inicial das letras
posicao_x = 800

# Inicialização da lista de letras
letras_objetos = []

# Criação dos objetos Letra para cada letra do alfabeto
for letra in letras:
    letra_obj = Letra(letra, posicao_x, 60, 1)
    letras_objetos.append(letra_obj)
    posicao_x += espacamento_letras

# Inicialização da nave e dos projéteis
nave = NaveEspacial()
projeteis = []

# Carregar palavras do arquivo
palavras = carregar_palavras(caminho_arquivo("palavras.txt"))
pontuacao = 0

# Sortear uma palavra aleatória
palavra_atual = random.choice(palavras).upper()
palavra_oculta = "@" * len(palavra_atual,)
mostrar_palavra = True
tempo_mostrar_palavra = 1  # Tempo em segundos

# Inicialização do cronômetro
cronometro = 60 # Tempo em segundos
tempo_atual = pygame.time.get_ticks()
tempo_total = tempo_atual + cronometro * 1000

# Estado do jogo
game_over = False
vidas = 3
jogar = True

# Loop principal do jogo
while not game_over:
    # Exibe o menu quando o jogo for reiniciado
    if game_over:
        exibir_menu()
        game_over = False

    for event in pygame.event.get():
        # Verifica eventos apenas se o jogo não estiver no estado de game over
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit() 

                if event.key == pygame.K_a:
                    nave.atirar_esquerda()

                if event.key == pygame.K_d:
                    nave.atirar_direita()

                if event.key == pygame.K_SPACE:
                    nave.atirar() 
            if nave:
                nave.processar_eventos(event)

    # Verifica se o tempo acabou
    if pygame.time.get_ticks() >= tempo_total:
        game_over = True
    
    
    # Desenha o fundo
    tela.blit(fundo2, (0, 0))
    
    # Desenha as letras do alfabeto
    for letra_obj in letras_objetos:
        letra_obj.desenhar()
    
    # Move e desenha as letras
    for letra_obj in letras_objetos:
        letra_obj.mover()

    
    # Verifica colisão entre os projéteis e as letras
    for projetil in projeteis:
        for letra_obj in letras_objetos:
            if projetil.rect.colliderect(letra_obj.x, letra_obj.y, 45, 30):
                letras_objetos.remove(letra_obj)
                pontuacao += 1
                palavra_oculta = atualizar_palavra_oculta(palavra_atual, palavra_oculta, letra_obj.letra)
    
    # Criar asteroides
    if random.randint(0, 200) < 1:
        # Criar asteroide indo para a esquerda
        asteroide_esquerda = Asteroide(largura, random.randint(10, 800), 1, 'esquerda')
        asteroides.append(asteroide_esquerda)

    # Move e desenha os projéteis
    for projetil in projeteis:
        projetil.mover()
        projetil.desenhar()
        
    # Move e desenha os asteroides
    for asteroide in asteroides:
        asteroide.mover()
        asteroide.desenhar()

        # Verifica colisão entre a nave e os asteroides
        if nave.rect.colliderect(asteroide.rect):
            vidas -= 1
            asteroides.remove(asteroide)
            
            if vidas == 0:
                exibir_mensagem()
                exibir_menu()
                reiniciar_jogo()
              
        # Verifica colisão entre os projéteis e os asteroides
        for projetil in projeteis:
            if projetil.rect.colliderect(asteroide.rect):
                asteroides.remove(asteroide)
                projeteis.remove(projetil)
                pontuacao += 100
                break

    # Desenha a nave
    nave.desenhar()
    
    # Desenha as vidas
    vidas_surface = fonte.render(f"Vidas: {vidas}", fonte, True, LARANJA)
    tela.blit(vidas_surface, (10, 5))

    # Desenha a pontuação
    pontuacao_surface = fonte.render("Pontuação: " + str(pontuacao), fonte, True, VERMELHO)
    tela.blit(pontuacao_surface, (10, 30))

        
    # Desenha as letras do alfabeto
    for letra_obj in letras_objetos:
        letra_obj.desenhar()
    
    # Move e desenha as letras
    for letra_obj in letras_objetos:
        letra_obj.mover()
        
        if letra_obj.x < -50:
            letra_obj.x = largura
    
    # Move e desenha os projéteis
    for projetil in projeteis:
        projetil.mover()
        projetil.desenhar()
        
        if projetil.rect.bottom < 0:
            projeteis.remove(projetil)

    # Move e desenha os asteroides
    for asteroide in asteroides:
        asteroide.mover()
        asteroide.desenhar()
    
    # Desenha a nave
    nave.desenhar()
    if nave:
        nave.mover()

    # Desenha a palavra oculta
    palavra_surface = fonte.render(palavra_oculta,fonte, True, AZUL)
    tela.blit(palavra_surface, (largura // 2 - palavra_surface.get_width() // 2, 10))
    
    
    # Mostra a palavra por um tempo determinado ao acertar uma letra
    if mostrar_palavra:
        tempo_passado = (pygame.time.get_ticks() - tempo_atual) / 1000
        if tempo_passado >= tempo_mostrar_palavra:
            mostrar_palavra = False
            tempo_atual = pygame.time.get_ticks()
            
        else:
            palavra_surface = fonte.render(palavra_atual, True, LARANJA)
            tela.blit(palavra_surface, (largura // 1.2 - palavra_surface.get_width() // 2, 10))

    # Mostra o cronômetro 
    tempo_restante = (tempo_total - pygame.time.get_ticks()) // 1000
    if tempo_restante < 0:
        tempo_restante = 0
        
    tempo_restante = (tempo_total - pygame.time.get_ticks()) // 1000
    if tempo_restante < tempo:
        tempo = tempo_restante

    cronometro_surface = fonte.render(f"Tempo: {tempo_restante}", True, VERMELHO)
    tela.blit(cronometro_surface, (largura - cronometro_surface.get_width() - 10, altura - 50))
    
    # Verifica se o tempo acabou
    if pygame.time.get_ticks() >= tempo_total:
        
        exibir_mensagem3()
        exibir_menu()
        reiniciar_jogo()

    if palavra_oculta == palavra_atual:
        exibir_mensagem2()
        reiniciar_jogo()
        
        
                
    # Atualiza a tela
    pygame.display.update()

# Finalização do Pygame
pygame.quit()
