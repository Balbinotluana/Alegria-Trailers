# encoding: utf-8
import media
import fun

os_smarfs = media.Movie("Os Smurfs",
                        "Gargamel quer capturar os Smurfs para ter eles como amuletos.",
                        "Comédia.",
                        "5 de Agosto de 2011 no Brasil.",
                        "Raja Gosnell.",
                        "https://images.livrariasaraiva.com.br/imagemnet/imagem.aspx/?pro_id=5345846&qld=90&l=430&a=-1",
                        "https://youtu.be/o5TbwxDTn28")
'''
Ao executar essa linha de codigo o metodo " __init__" sera chamado.
O metodo __init__ foi definido no arquivo 'media.py'
'''
ratatouille = media.Movie("Ratatouille",
                          "Remy é um rato que reside em Paris e sonha em ser um chef de cozinha.",
                          "Animação e Comédia.",
                          "6 de Julho de 2007 no Brasil.",
                          "Brad Bird.",
                          "http://www.cafecomfilme.com.br/media/k2/items/cache/95af20a543d0ffa5a101ab798fe1da12_XL.jpg ",
                          "https://youtu.be/iryIGZlE5B4")

rei_leao = media.Movie("O Rei Leão",
                       "Esse desenho mostra as aventuras de um leão e seus amigos Timon e Pumba.",
                       "Animação, Aventura, Drama e Épico.",
                       "8 de julho de 1994 no Brasil.",
                       "Roger Allers, Rob Minkoff.",
                       "https://vignette.wikia.nocookie.net/disney/images/c/c7/Poster-rei-leao-full.jpeg/revision/latest?cb=20160925204728&path-prefix=pt-br",
                       "https://youtu.be/rHiHRhbTv-Q")

frozen = media.Movie("Frozen",
                     "A jovem princesa Anna, parte em uma jornada com seus amigos para encontrar sua irmã, a rainha Elsa.",
                     "Musical, Fantasia e Comédia dramática.",
                     "3 de janeiro de 2014 no Brasil.",
                     "Chris Buck, Jennifer Lee.",
                     "https://images-na.ssl-images-amazon.com/images/I/A1ltEcBQCvL._RI_SX200_.jpg",
                     "https://youtu.be/0qZEa4xeLmU")

up = media.Movie("Up - Altas Aventuras",
                 "Carl é um senhor de 78 anos que vai encarrar uma aventura pela America do Sul com o menino Ruseel de 8 anos.",
                 "Comédia, Animação e Aventura.",
                 "4 de setembro de 2009 no Brasil.",
                 "Pete Docter.",
                 "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-m0flh1_c3f39708.jpeg?region=0,0,300,450",
                 "https://youtu.be/hwxqLjspkDI")

zootopia = media.Movie("Zootopia",
                       "Em uma cidade de animais, uma raposa se torna uma fugitiva ao ser acusada de um crime que não cometeu.",
                       "Fantasia, Aventura e Comédia.",
                       "17 de março de 2016 no Brasil.",
                       "Byron Howard, Rich Moore.",
                       "http://www.biggarcornexchange.org.uk/wp-content/uploads/zootropolis-poster-2.jpg",
                       "https://youtu.be/_McNwvfvu4s")

monstros_sa = media.Movie("Monstros S.A",
                         "A fábrica de monstros conta com James e Mike ambos tem o trabalhos de assustar crianças, até conhecerem a Boo.",
                         "Animação, Fantasia e Comédia.",
                         "14 de novembro de 2001 no Brasil.",
                         "Pete Docter.",
                         "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-cbntla_d945f607.jpeg",
                         "https://youtu.be/iRh2kF-1X2E")

poderoso_chefinho = media.Movie("O Poderoso Chefinho",
                               "Um bebê falante que usa terno e carrega uma maleta irá tentar impedir que acabe o amor no mundo, e para isso contará coma  ajuda de seu irmão.",
                               "Animação e Comédia.",
                               "30 de marco de 2017 no Brasil.",
                               "Tom McGrath.",
                               "http://br.web.img2.acsta.net/pictures/16/10/18/16/29/576071.jpg",
                               "https://youtu.be/QYYsJkUl7TY")

nemo = media.Movie("Procurando Nemo",
                     "Em seu primeiro dia de aula, Nemo é capturado por um mergulhador e acaba no aquário de um dentista.",
                     "Animação, Aventura e Comédia.",
                     "4 de Julho de 2003 no Brasil.",
                     "Andrew Stanton.",
                     "https://i1.wp.com/psicosaber.wordpress.com/files/2009/05/procurando-nemo-poster04.jpg?resize=1400%2C9999",
                     "https://youtu.be/oIb4tghqQD4")


movies = [os_smarfs, ratatouille, rei_leao, frozen, up, zootopia, monstros_sa, poderoso_chefinho, nemo]
fun.open_movies_page(movies)
