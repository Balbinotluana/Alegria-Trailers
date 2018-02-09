# encoding: utf-8
import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Alegria</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro" rel="stylesheet">
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            font-family: 'Source Sans Pro', sans-serif;
        }
        .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        .trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 90%;
            left: 32;
            top: 12;
            background-color: white;
        }
        .cabecalho {
            background-color: #0038a8;
        }
        .navbar-brand {
            font-size: 25px;
            height: 40px;
            color: white;
        }
        .text-personal {
        color: #0038a8;
        }
        .espacamento {
        padding-bottom: 40px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });

          // comentar do truque
          $('.modal').on('hidden.bs.modal', function() {
              var $this = $(this).find('iframe');
              var src = $this.attr('src');
              $this.attr('src', "");
              $this.attr('src', src);
          });
        });
        </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-fixed-top cabecalho" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Alegria Trailers!!!</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
        <div class="row">
          {movie_tiles}
        </div>
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="modal" id="{trailer_youtube_id}">
  <div class="modal-dialog">
    <div class="modal-content">
      <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
      </a>
      <div class = "modal-body">
          <div class = "row">
            <div class = "cl-md-12">
                <div class = "scale-media">
                <iframe type="text-html" src="http://www.youtube.com/embed/{trailer_youtube_id}" frameborder="0">
                </iframe>
                </div>
              </div>
           </div>
            <div class = "row">
              <div class = "cl-md-12">
                <br>
                <h4 class="text-capitalize text-center text-personal"><b>{movie_title}</b></h4>
              </div>
           </div>
          <div class = "row">
            <div class = "cl-md-12">
              <h5 class="text-capitalize text-left"><b>{storyline}</b></h5>
            </div>
          </div>
          <div class = "row">
            <div class = "cl-md-12">
              <strong>Genero</strong>: {genre}
            </div>
          </div>
          <div class = "row">
            <div class = "cl-md-12">
              <strong>Data de Lançamento</strong>: {release_date}
            </div>
          </div>
          <div class = "row">
            <div class = "cl-md-12">
              <strong>Diretor</strong>: {director}
            </div>
          </div>
      </div>
    </div>
  </div>
</div>
<div class="col-md-4 text-center espacamento" data-toggle="modal" data-target="#{trailer_youtube_id}">
    <img src="{poster_image_url}" width="220" height="342">
    <h3 class="text-center text-personal"><b>{movie_title}</b></h3>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            storyline = movie.storyline,
            genre = movie.genre,
            release_date = movie.release_date,
            director = movie.director,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fun.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
