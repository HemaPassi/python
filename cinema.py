
films = {
    "Finding Dory": [3,5],
    "Bourne" : [18,5],
    "Tarzan" : [15,1],
    "Ghost Busters" :[12,5]
    }

while True:
    choice = input('Enter movie to watch').strip().title()

    if choice in films:
        yourAge = int(input ('Enter your age').strip())
        if yourAge >= films[choice][0] :
            if(films[choice][1] > 0) :
                films[choice][1] =  films[choice][1] -1
                print("Enjoy the movie")
            else:
                print("you can't watch that movie, seats are not available")
        else:
              print("you can't watch that movie")
    else:
        print(" we don't have that film")


        
   
   
