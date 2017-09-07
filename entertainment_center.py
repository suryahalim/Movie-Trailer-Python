import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"A marine of alien planet",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=d1_JBMrrYw8")


dawn_of_the_apes = media.Movie("Dawn Of The Planet Of The Apes",
	"A story about an ape",
	"http://upload.wikimedia.org/wikipedia/en/7/77/Dawn_of_the_Planet_of_the_Apes.jpg",
	"http://www.youtube.com/watch?v=eq1sTNGDXo0")

gone_girl = media.Movie("Gone Girl",
	"A sad story",
	"http://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
	"http://www.youtube.com/watch?v=Ym3LB0lOJ0o")

avenger = media.Movie("Avenger",
	"A story about superheroes",
	"http://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
	"http://www.youtube.com/watch?v=hIR8Ar-Z4hw")

dark_knight = media.Movie("Dark knight rises",
	"A story about batman",
	"http://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
	"http://www.youtube.com/watch?v=g8evyE9TuYk")

movies = [toy_story,avatar,dawn,gonegirl,avenger,dark_knight]
fresh_tomatoes.open_movies_page(movies)
