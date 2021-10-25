from time import sleep

print('COMPIUTER diz: "Olá, me chamo COMPIUTER"')
sleep(0.7)
nome = str(input('COMPIUTER diz: "Qual o seu nome?" ')).capitalize()
sleep(0.7)
print(f'COMPIUTER diz: "Muito prazer, {nome}"')
print('COMPIUTER diz: "Eu sou uma Inteligência Artificial criada por Semlua. Minha função é..."')
sleep(0.7)
print('COMPIUTER diz: "Bem, não tenho uma função, mas eu estou aqui para conhecer melhor as pessoas, eu acho..."')
print('COMPIUTER diz: "Você gostaria de me ajudar em uma pesquisa que estou fazendo para o Semlua?" ')
decisao = str(input('[S] [N] ')).capitalize()
if decisao == 'S':
    print('COMPIUTER diz: "LEGAL! Primeiro vamos começar pelo básico  "')
    sleep(0.7)
    idade = int(input('COMPIUTER diz: "Quantos anos você tem?" '))
    print('COMPIUTER diz: "Certo, a idade foi computada" ')
    sleep(0.7)
    print('COMPIUTER diz: "Eu gostaria de saber um pouco mais de você" ')
    sleep(0.7)
    livros = str(input('COMPIUTER diz: "Você gosta de ler? [S] [N]" ')).capitalize()
    if livros == 'S':
        livros = "Gosta de ler"
        sleep(0.7)
        livroFavorito = str(input('COMPIUTER diz: "Qual o seu livro favorito? "'))
    else:
        livros = "Não gosta de ler"
    print("--------------------------------------------------------------------")
    sleep(0.7)
    print('COMPIUTER diz: "Você me ajudou bastante! O Semlua está fazendo uma pesquisa meio doida relacionada a livros"')
    sleep(0.7)
    print('COMPIUTER diz: "Se você gosta de ler e de criar seu próprio mundo, aqui vai uma lista de livros que o Semlua me pediu para passar adiante: "')
    print('[1] As Crônicas de Nárnia \n[2] Do Coração de TELMAH \n[3] Ponte para Terabítia \n[3] O Hobbit \n[4] Ninfeias Negras')
    sleep(0.8)
    print('COMPIUTER diz: "Aqui vai mais uma lista, porém de músicas: "')
    print('[1] Exist for love \n[2] I see fire \n[3] Shine on you crazy diamond \n[4] Winter bird')
    print('COMPIUTER diz: "Muito obrigado por me ajudar nessa pesquisa. Verifique abaixo as informações que você digitou "')
    print(f'Nome: {nome} \nIdade: {idade} \nGosta de ler? {livros} ')
else:
    sleep(0.7)
    print('COMPIUTER diz: "Tudo bem, vou aguardar outra pessoa que queira participar"')
sleep(1)
print('COMPIUTER diz: "Cuide-se!"')