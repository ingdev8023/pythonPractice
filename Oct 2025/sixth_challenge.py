# Favorite Songs
# Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

# Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

# Each object will have a "title" property (string), and a "plays" property (integer).

def favorite_songs(playlist):
    plays = []
    title = []
    most_played_songs = []
    for song in playlist:
        plays.append(song['plays'])
        title.append(song['title'])
    
    while len(most_played_songs) < 2:
        index = plays.index(max(plays))
        most_played_songs.append(title[index])
        plays.pop(index)
        title.pop(index)
               
    return most_played_songs

favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ])
favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ])
favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ])


