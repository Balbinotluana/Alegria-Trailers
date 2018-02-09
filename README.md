# Alegria-Trailers
Como criar um site de trailers

# Como rodar o projeto
Abrir o terminal de comando abaixo:
```
python entertainment_center.py
```
Irá gerar um arquivo nomeado fun.html, esse arquivo irá abrir no browser exibindo o site.

# Como o site é gerado

## `media.py`
No arquivo `media.py` esta definida a classe `Movie`, esta classe fornece uma maneira de armazenar informações relacionadas aos filmes.
  Na classe `Movie` está definido o construtor `_init_` que recebe as variáveis listadas abaixo.
  - movie_title,
  - movie_storyline, 
  - movie_genre, 
  - movie_release_date,
  - movie_director,
  - poster_image,
  - trailer_youtube.
  Estas variáveis vão armazenar os valores dos filmes que posteriormente serão exibidos no html.
  Na classe `Movie` também está definido o metodo `show_trailer` que irá abrir o navegador Web com a Url correta, que é a Url que esta  armazenada na variável de instancia "trailer_youtube_url", e a forma de acessar essa variável de instancia é através da palavra chave
"self".

## `entertainment_center.py`
No arquivo `entertainment_center.py` será definido os valores que serão exibidos no browser.
```
os_smarfs = media.Movie("Os Smurfs",
                        "Gargamel quer capturar os Smurfs para ter eles como amuletos.",
                        "Comédia.",
                        "5 de Agosto de 2011 no Brasil.",
                        "Raja Gosnell.",
                        "https://images.livrariasaraiva.com.br/imagemnet/imagem.aspx/?pro_id=5345846&qld=90&l=430&a=-1",
                        "https://youtu.be/o5TbwxDTn28")
```                        
Ao executar essa linha de codigo o metodo `__init__` sera chamado.
O metodo `__init__` foi definido no arquivo `media.py`

`movies`irá receber todos os valores gerados para cada filme.
`fun.open_movies_page(movies)`irá receber todas as variáveis de `movies`.

## `fun.py`
No Arquivo `fun.py` será gerado html dinamicamnete usando tamplates de htlm para cada filme. 
