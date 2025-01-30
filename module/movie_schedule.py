# Current movie schedule
current_movies = {
    "The Grinch": "11:00am",
    "Rudolph": "1:00pm",
    "Frosty the Snowman": "3:00pm",
    "Christmas Vacation": "5:00pm",
}

print("🎥 We're showing the following movies:\n")

# Display movie options with a numbered list
for idx, (movie, time) in enumerate(current_movies.items(), start=1):
    print(f"{idx}. {movie} - {time}")

for key in current_movies:
    print("key in a simple way:")
    print(key)

# Prompt the user to select a movie
while True:
    movie = input("\nWhat movie would you like the showtime for?\n").strip()

    # Check if the movie exists in the schedule
    if movie in current_movies:
        print(f"\n🎬 '{movie}' is showing at {current_movies[movie]}. Enjoy the movie!")
        break
    else:
        print(f"🚫 Sorry, we don't have '{movie}' in the schedule. Please choose again.")

# Thank the user
print("\n🍿 Thank you for using the Movie Schedule Program!")
