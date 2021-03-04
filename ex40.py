class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

bday_lyrics = ["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there",
                   "One more line of lyrics"]

happy_bday = Song(bday_lyrics)

bulls_on_parade = Song(["They rally around that family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()