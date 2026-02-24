def make_album(nome_artista, album):
    disco = {'Nome': nome_artista, 'Album': album}
    return disco

while True:
    nome_artista = input('\nDigite o nome do artista:')
    album = input('Digite o nome do álbum:')
    musico = make_album(nome_artista, album)
    print((musico))