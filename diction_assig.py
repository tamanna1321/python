movies =[
    {"name" : "forrest gump" ,"year" : 1994 , "duration":142,"genres":
     ["drama","romance"]},{"name":"Avengers:Endgame","year":2019,"duration":181,
                           "genres":["action","adventure","drama"]},
                           {"name":"back to the future","year":1985,
                            "duration":114,"genres":["adventure","comedy","sci-fi"]}
                            ]

def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value :
            return value
        print("input cannot be empty.please try again")
def input_int(prompt) :
    while True:
        try:
           return int(input(prompt).strip())  
        except ValueError:
         print("Invalid input.please enter an integer")     
def add_movie(movies):
    name = input_something("Enter the movie name:")
    year = input_int("Enter the release year:")
    duration = input_int("Enter the duration in minutes:")
    while True:
        genres_input = input ("Enter genres(comma-separated):").strip()
        if genres_input:
            genres = genres_input.split(", ")
            break
        print("you must enter atleast one genre.Please try again.")  
    movie = {"name":name,"year":year,"duration":duration,"genres":genres}  
    movies.append(movie)  
    print(f"movie'{name}' added successfully.") 
def list_movies(movies):
    if not movies:
        print("No movies saved.")
    else:
        for i , movie in enumerate(movies,start=1):
            print(f"{i}){movie['name']}({movie['year']})")   
def search_movies(movies):
    if not movies:
        print("no movies saved.")  
    else:
        term =input_something("Enter a search term:").lower()  
        results = [movie for movie in movies if term in movie["name"].lower()]   
        if results :
            for i , movie in enumerate(results,start=1):      
             print(f"{i}){movie['name']}({movie['year']})")
        else:
            print("no movies found.")  
def view_movie(movies) :
    if not movies:
        print("No movies saved.")   
    else:
        index = input_int("Enter the movie index to view:")-1
        if 0 <= index < len(movies):
            movie = movies[index]
            print(f"name:{movie['name']}")
            print(f"year:{movie['year']}")
            print(f"duration:{movie['duration']} minutes") 
            print(f"genres:{','.join(movie['genres'])}")
        else:
            print("invalid index.")  
def delete_movie(movies):
    if not movies:
        print("No movies saved")
    else:
        index = input_int("Enter the movie index to delete:")-1
        if 0 <= index <len (movies):
            removed_movie = movies.pap(index) 
            print(f"Movie '{removed_movie['name']}'deleted successfully.")  
        else:
            print("invalid index.")
print("Welcome to the movie CLI program!")   
while True:
    print("\nChoose[a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")   
    choice = input ("Enter your choice:") .strip() .lower() 
    if choice == 'a':
        add_movie(movies)  
    elif choice == 'l':
        list_movies(movies)
    elif choice == 's':
        search_movies(movies) 
    elif choice =='v':
        view_movie(movies)  
    elif choice =='d':
        delete_movie(movies) 
    elif choice =='q':
        print("Exiting the program.Goodbye!") 
        break
    else:
        print("invalid choice. Please try again.")        
             