class Manga(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def print_title(self):
    	print(self.title)

    def print_artist(self):
    	print(self.artist)


m1 = Manga('Chihayafuru',
           'Yuki Suetsugu')
m2 = Manga('Case Closed', 
           'Gosho Aoyama')
m3 = Manga('Shogi no Watanabe-kun', 
           'Megumi Ina')

for manga in [m1, m2, m3]:
	manga.print_title()
	manga.print_artist()


"""
$ python test_class.py 
Chihayafuru
Yuki Suetsugu
Case Closed
Gosho Aoyama
Shogi no Watanabe-kun
Megumi Ina
"""