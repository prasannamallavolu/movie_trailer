import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial_scale=1">
    <title>Movie Trailers!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 75px;
            background-color:#E8F8F5;
            background-image:url("https://www.aacounty.org/sebin/l/a/page-background-default.jpg")
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 639px;
            height: 479px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        p_trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color:#85C1E9;
            cursor: pointer;
            border-radius:5%;
        }
        .p_scale_media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .p_scale_media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: black;
        }
        img{
          border-radius:12%;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'p_trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
p_main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="p_scale_media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{p_trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2 style="font-family:serif;color:red;">{p_mv_title}</h2>
    <p style="color:violet;">{p_mv_line}</p>
</div>
'''


def create_movie_tiles_content(p_movies):
    # The HTML content for this section of the page
    p_content = ''
    for p_movie in p_movies:
        # Extract the youtube ID from the url
        youtube_match = re.search(
            r'(?<=v=)[^&#]+', p_movie.pmv_trailer)
        youtube_match = youtube_match or re.search(
            r'(?<=be/)[^&#]+', p_movie.pmv_trailer)
        p_trailer_utube_id = (youtube_match.group(0) if youtube_match
                              else None)

        # Append the tile for the movie with its content filled in
        p_content += movie_tile_content.format(
            p_mv_title=p_movie.pmv_name,
            p_mv_line=p_movie.pmv_line,
            poster_image_url=p_movie.pmv_poster,
            p_trailer_youtube_id=p_trailer_utube_id
        )
    return p_content


def p_on_mv_page(p_movies):
    # Create or overwrite the output file
    p_op_fl = open('p_final.html', 'w')

    # Replace the movie tiles placeholder generated content
    p_rendered_content = p_main_page_content.format(
        movie_tiles=create_movie_tiles_content(p_movies))

    # Output the file
    p_op_fl.write(main_page_head + p_rendered_content)
    p_op_fl.close()

    # open the output file in the browser (in a new tab, if possible)
    p_url = os.path.abspath(p_op_fl.name)
    webbrowser.open('file://' + p_url, new=2)
