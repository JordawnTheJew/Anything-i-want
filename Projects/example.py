def make_album(artist_name, album_name, track_number):
    """Returns a dictionary of an Artist"""

    artist_name = artist_name.strip()
    album_name = album_name.strip()
    track_number = track_number.strip()


    full_block = {'artist': artist_name, 'album': album_name, 'track': track_number}
    return full_block

while True:

    artist_name = input("Enter artist_name")
    album_name = input("Enter album_name")
    track_number = input("Enter album_name")

    if artist_name == 'q' or album_name == 'q' or track_number == 'q':
    #If even on of the inputs is q, it will break out of the while loop
        print("You pressed q, quitting..")
        break

    else:

        musician = make_album(artist_name, album_name, track_number)
        print(musician)