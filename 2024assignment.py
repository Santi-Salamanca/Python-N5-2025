import random

durationOfTraining = int(input("enter the length of your training session between 10min and 30min: "))
while durationOfTraining < 10 or durationOfTraining> 30:
    print("eror please enter a valid duration")
    durationOfTraining = int(input("enter the length of your training session between 10min and 30min: "))

durOfTrain = durationOfTraining * 60

songcounter = 0
songs = []
total = 0
while total < durOfTrain:
    durSong = int(input("Please enter the duration of the next song in seconds: "))
    total = total + durSong
    songs.append(durSong)
    if total >= durOfTrain:
        print("you have entered sufficient songs")
    songcounter = songcounter + 1

counter = 1
songcounter = str(songcounter)
print("number of songs played: " +  songcounter)
songcounter = int(songcounter)
foammachine = random.randint(1, songcounter)
for index in songs:
    print(f"{counter} : {songs[counter - 1]}")
    if foammachine == counter:
        print("start foam machine")
    counter = counter + 1
print(f"the total length of the trainign session was: {total} seconds")