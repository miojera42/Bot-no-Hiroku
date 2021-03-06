import discord
from random import randint
from ast import literal_eval
import os

client = discord.Client()


async def RegistraMagia(message):
    #le o arquivo(txt) e 'converte' em dicionario
    with open ('testetxt') as le:
        variavel=literal_eval(le.read())
    msgr=message.content.lower().replace("!r","").split()
    #adiciona valor na variavel correspondente ao txt
    #msgr[0]= nome da magia;
    #msgr[-2]= dado da magia;
    #msgr[-1]= quantidade de dados
    variavel[" ".join(msgr[0:-2])]=f'{msgr[-2]} {msgr[-1]}'
    #escreve o valor da variavel no txt
    with open ('testetxt', 'w') as escreve:
        escreve.write(str(variavel))
    await message.channel.send("Sua magia foi registrada no grimório com sucesso")

async def CastMagia(message):
     #le o arquivo(txt) e 'converte' em dicionario
    with open ('testetxt') as le:
        variavel=literal_eval(le.read())

    #recebe os valores da chave em '[]'
    valores=variavel[message.content.lower().replace("!cast","").strip()]

    valores=valores.split()
    await RollDice(message,valores,True)
    
async def CharlieBrown(message):
    await message.channel.send('brown'+message.content.lower().replace("charlie","").replace("!",""))

async def RollDice(x, y, message):
    # x = tipo de dado
    # y = vezes a rolar
    saida = [randint(1, int(x)) for i in range(int(y))]
    apoio='```fix\n'
    apoio+=str(saida)
    apoio+=f'\nTotal = {str(sum(saida))}```'
    await message.channel.send(apoio)
        
    
@client.event
async def on_ready():
     print(f'Logante como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user: return None
    tmp = str(message.content.lower())
    if "d" in tmp:
        qtd = str(tmp[0:tmp.find("d")])
        lados = str(tmp[tmp.find("d")+1:])
        if qtd.isdigit() and lados.isdigit():
            await RollDice(lados, qtd, message)
    if message.content.lower().startswith('!'):
        if message.content.lower().replace("!","").startswith('charlie'):
            await CharlieBrown(message)
        if message.content.lower().replace("!","").startswith('d'):
            await RollDice(message)
        if message.content.lower().replace("!","").startswith('r'):
            await RegistraMagia(message)
        if message.content.lower().replace("!","").startswith('cast'):
            await CastMagia(message)
        comandos = {'!reg':[RPG.RegistraMagia,"!reg 'nome_magia' 'dado' 'quantidade_dado'"], 
              'adbb':[RPG.RollDice,"adbb onde 'a' é um numero e 'b' é um numero "], 
              '!charlie':[CharlieBrown,"!charlie 'qq_texto'"],
              '!cast':[RPG.CastMagia,"!cast 'nome_magia'"]}
  
        if message.content.lower() == "!help":
            await message.channel.send("COMANDOS:")
            for k in list(comandos.keys()): await message.channel.send(comandos[k][1])
        

client.run(os.environ['mudaessafitan'])
