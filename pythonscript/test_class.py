class Manga(object):
    def __init__(self, index, title, artist, volumes, anime, movie):
        self.index = index
        self.title = title
        self.artist = artist
        self.volumes = volumes
        self.anime = anime
        self.movie = movie


    def __repr__(self):
    	return '<Manga({}): {} - {} - {} - {} - {}>'.format(self.index, self.title, self.artist, self.volumes, self.anime, self.movie)


    def add_vol(self):
    	self.volumes += 1


def main():
	manga_list = []
	manga_list.append(Manga(1, 'Chihayafuru', 'Yuki Suetsugu', 38, True, True))
	manga_list.append(Manga(2, 'Case Closed', 'Gosho Aoyama', 94, True, True))
	manga_list.append(Manga(3, 'Shogi no Watanabe-kun', 'Megumi Ina', 3, False, False))
	manga_list.append(Manga(4, 'Magic Kaito', 'Gosho Aoyama', 5, True, False))


	print('\n* manga list *')
	for manga in manga_list:
		print(manga)


	print('\n* Aoyama written *')
	manga_list_filter = filter(lambda manga: 'Aoyama' in manga.artist, manga_list)
	for manga in manga_list_filter:
	    print(manga)

	print('\n* add volume *')
	manga_list[1].add_vol()


	print('\n* check *')
	print(manga_list[1])



if __name__ == '__main__':
	main()



"""
$ python test_class.py 

* manga list *
<Manga(1): Chihayafuru - Yuki Suetsugu - 38 - True - True>
<Manga(2): Case Closed - Gosho Aoyama - 94 - True - True>
<Manga(3): Shogi no Watanabe-kun - Megumi Ina - 3 - False - False>
<Manga(4): Magic Kaito - Gosho Aoyama - 5 - True - False>

* Aoyama written *
<Manga(2): Case Closed - Gosho Aoyama - 94 - True - True>
<Manga(4): Magic Kaito - Gosho Aoyama - 5 - True - False>

* add volume *

* check *
<Manga(2): Case Closed - Gosho Aoyama - 95 - True - True>
"""