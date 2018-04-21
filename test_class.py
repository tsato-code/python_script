class Manga(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def print(self):
    	print(self.title, '-', self.artist)


def main():
	manga_list = []
	manga_list.append(Manga('Chihayafuru', 'Yuki Suetsugu'))
	manga_list.append(Manga('Case Closed', 'Gosho Aoyama'))
	manga_list.append(Manga('Shogi no Watanabe-kun', 'Megumi Ina'))
	manga_list.append(Manga('Magic Kaito', 'Gosho Aoyama'))


	print('\n* manga list *')
	for manga in manga_list:
		manga.print()

	print('\n* Gosho Aoyama written *')
	manga_list_filter = filter(lambda manga: manga.artist == 'Gosho Aoyama', manga_list)
	for manga in manga_list_filter:
	    manga.print()


if __name__ == '__main__':
	main()



"""
$ python test_class.py 

* manga list *
Chihayafuru - Yuki Suetsugu
Case Closed - Gosho Aoyama
Shogi no Watanabe-kun - Megumi Ina
Magic Kaito - Gosho Aoyama

* Gosho Aoyama written *
Case Closed - Gosho Aoyama
Magic Kaito - Gosho Aoyama
"""