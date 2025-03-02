#Exercice 1
#Print the total duration of the playlist
playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}


total_duration = 0
for i in range(len(playlist["songs"])):
    total_duration += playlist["songs"][i]["duration"]

print("La durée totale de la playlist est :", total_duration, "minutes")

#Exercice 2:
# create a new list that only contains the uppercased words
words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
words_upper = [word for word in words if word.isupper() ]
print(words_upper)


# FUNCTIONS
# Exercice 1 
#Create a function average_length_of_words which takes a string as 
# an argument and returns the average length of the words in the 
# string. You can assume that there is a single space between each
#  word and that the input does not have punctuation. The result
#  should be rounded to one decimal place (hint: see round).
#average_length_of_words('only four lett erwo rdss') == 4 (modifié) 

def average_length_of_words(string):
    words = string.split("")
    average = sum(len(word) for word in words) / len(words)
    return average