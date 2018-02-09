# encoding: utf-8
import webbrowser

class Movie():
    '''
    Esta classe fornece uma maneira de armazenar informacoes relacionadas aos filmes.
    Foi utilizado a classificação etária Brasileira.
    https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_por_edades_(cine)#Brasil
    '''
    VALID_RATINGS = ["L", "10", "12", "14", "16", "18"]

    def __init__(self, movie_title, movie_storyline, movie_genre, movie_release_date,
                movie_director, poster_image, trailer_youtube):
        '''
        O metodo "__init__" inicializa ou cria espaco na memoria para lembrar detalhes como:
        titulo, historia, etc.
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.genre = movie_genre
        self.release_date = movie_release_date
        self.director = movie_director
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''
        O metodo 'show_trailer' irá abrir o navegador Web com a Url correta,
        que é a Url que esta armazenada na variável de instancia "trailer_youtube_url",
        e a forma de acessar essa variável de instancia é através da palavra chave "self".
        '''
        webbrowser.open(self.trailer_youtube_url)
