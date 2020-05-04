# @nobo/4May2020
# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def addMovie():
    title = input("Title")
    for i in range(len(movies)):
        if title in movies[i]['title']:
            return("Duplicate")
    director = input("Director")
    year = input("year")
    movies.append({'title': title, 'director': director, 'year': year})
    return ("Succesfully Added")


# Create other functions for:
#   - listing movies
#   - finding movies
def viewMovie():

    for i in movies:
            print(i)

def findMovieByTitle(t):

    c=0
    for i in movies:
        if t in i['title']:
            c=1
            print("Found!")
            print(i)
    if c==0:
        print("Not Found")

# And another function here for the user menu
def userMenu():
    menuPrompt="a. addNewMovie /nb. seeMovieList /nc. findMovieByTitle /nd. quit"
    selection=input(menuPrompt)
    while selection!='d':
        if selection=='a':
            addMovie()
        elif selection=='b':
            if len(movies) > 0 :
                viewMovie()
            else:
                print("You're Boring!")
        elif selection=='c':
            t=input("Enter title to be searched")
            print(findMovieByTitle(t))
        else:
            print("Invalid Choice")

        selection=input(menuPrompt)
        
# Remember to run the user menu function at the end!    
userMenu()
