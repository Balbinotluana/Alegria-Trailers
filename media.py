import webbrowser

class Movie():
    '''
    Esta classe fornece uma maneira de armazenar informacoes relacionadas aos filmes.
    '''
    VALID_RATINGS = ["P", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, movie_genre, movie_release_date, movie_director, poster_image, trailer_youtube):
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
        O metodo 'show_trailer'ira abrir o navegador Web com a Url correta,
        que e a Url que esta armazenada na variavel de instancia "trailer_youtube_url",
        e a forma de acessar essa vriavel de instancia atraves da palavra chave "self".
        '''
        webbrowser.open(self.trailer_youtube_url)
