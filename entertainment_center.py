import media
import fresh_tomatoes

#Toy story movie : movie title, storyline, poster image, and movie trailer
toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#Pokemon movie : movie title, storyline, poster image, and movie trailer
pokemon = media.Movie("Pokemon",
	"A story of a boy and his Pocket Monster fighting Mewtwo",
	"https://upload.wikimedia.org/wikipedia/en/c/c9/Pokemon-mewtwo-strikes-back.jpg",
	"https://www.youtube.com/watch?v=dFizEEX1hps")

#Avatar movie : movie title, storyline, poster image, and movie trailer
avatar = media.Movie("Avatar",
	"A marine of alien planet",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=d1_JBMrrYw8")

#Dawn of the Planet of the Apes movie : movie title, storyline, poster image, and movie trailer
dawn_of_the_apes = media.Movie("Dawn Of The Planet Of The Apes",
	"A story about an ape",
	"http://upload.wikimedia.org/wikipedia/en/7/77/Dawn_of_the_Planet_of_the_Apes.jpg",
	"http://www.youtube.com/watch?v=eq1sTNGDXo0")

#Avenger movie title, storyline, poster image, and movie trailer
avenger = media.Movie("The Avenger",
	"Earth's mightiest heroes must come together and learn to fight as a team if they are"
	" to stop the mischievous Loki"
	" and his alien army from enslaving humanity.",
	"https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
	"http://www.youtube.com/watch?v=hIR8Ar-Z4hw")

#Dark Knight movie : movie title, storyline, poster image, and movie trailer
dark_knight = media.Movie("Dark knight rises",
	"The first story of Batman Trilogies",
	"http://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
	"http://www.youtube.com/watch?v=g8evyE9TuYk")

#Gone girl movie : movie title, storyline, poster image, and movie trailer
gone_girl = media.Movie("Gone Girl",
	"A story about psycopath Girlfriend ",
	"http://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
	"http://www.youtube.com/watch?v=Ym3LB0lOJ0o")

#Set movies to be passed on the media file
movies = [ toy_story,
	pokemon,
	avatar,
	dawn_of_the_apes,
	avenger,
	gone_girl,
	avenger,
	dark_knight]

#calling the HTML Builder	
fresh_tomatoes.open_movies_page(movies)
