
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","Story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar","Marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)

#avatar.show_trailer()
spiderman = media.Movie("Spider-Man","Thrilled by his experience with the Avengers, young Peter Parker returns home to live with his Aunt May. Under the watchful eye of mentor Tony Stark, Parker starts to embrace his newfound identity as Spider-Man.","https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg","https://www.youtube.com/watch?v=BGHGZjDguqw")

A_Gentleman = media.Movie("A Gentleman","Gaurav dreams of settling down with Kavya, the woman of his dreams, but she prefers a man who's more adventurous and willing to take risks. He soon stands to lose everything when a case of mistaken identity rocks his once-happy life.","https://upload.wikimedia.org/wikipedia/en/c/c6/A_Gentleman.jpg","https://www.youtube.com/watch?v=IMXifj-peiQ")

Thor = media.Movie("Thor: Ragnarok","Imprisoned on the other side of the universe, the mighty Thor finds himself in a deadly gladiatorial contest that pits him against the Hulk, his former ally and fellow Avenger.","https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg","https://www.youtube.com/watch?v=ue80QwXMRHg")

emoji_movie = media.Movie("The Emoji Movie","Hidden inside a smartphone, the bustling city of Textopolis is home to all emojis. Each emoji has only one facial expression, except for Gene, an exuberant emoji with multiple expressions., and thereby profit warlords and diamond companies across the world.","https://upload.wikimedia.org/wikipedia/en/6/63/The_Emoji_Movie_film_poster.jpg","https://www.youtube.com/watch?v=r8pJt4dK_s4")

movies = [toy_story,avatar,spiderman,A_Gentleman,Thor,emoji_movie]
fresh_tomatoes.open_movies_page(movies)
