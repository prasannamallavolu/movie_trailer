import p_final
import p_movie
banglore=p_movie.p_mv("Banglore Days","Friendship Movie",
                  "https://wallpapers.filmibeat.com/ph-1024x768/2014/04/bangalore-days-wallpaper_139652831720.jpg",
                  "https://youtu.be/uVpHL5g4buY")
perfect=p_movie.p_mv("Mr.Perfect",
                    "Family Entertainment Movie",
                    "http://4.bp.blogspot.com/-7VmnvfmahOs/TYokZmfh3XI/AAAAAAAADCY/FhH3VA4TeqU/s1600/Mr.Perfect%2BWP%2B02.jpg",
                    "https://youtube/k2seict_FEA")
rail=p_movie.p_mv("Rail","Action Comedy Film",
                "http://ilovefree.in/wp-content/uploads/2016/09/Rail-Telugu-Movie-Review-Rating3.755-Public-Talk-Dynamic.jpg",
                "https://youtu.be/-VkZ9e8I8mk")
meesaya=p_movie.p_mv("Meesaya Murukku","Failure Love story of a B.tech Student",
                 "https://i.ytimg.com/vi/aCY4E1ZCrwo/maxresdefault.jpg",
                 "https://youtu.be/Ghizg_3uI3E")
snehithudu=p_movie.p_mv("Snehithudu","FriendShip Movie",
                        "https://media-images.mio.to/various_artists/S/Snehithudu%20%282012%29/Art-350.jpg",
                        "https://youtu.be/eYZ_bP9xGpQ")
zindagi=p_movie.p_mv("Vunnadi Okate Zindagi","Friendship Movie",
                     "https://www.img.myfirstshow.com/uploads/2017/10/Vunnadhi-Okate-Zindagi-Review-e1509096619523.jpg",
                     "https://youtu.be/FaS_dMl72Qc")
p_movies=[banglore,perfect,snehithudu,rail,meesaya,zindagi]
p_final.p_on_mv_page(p_movies)
