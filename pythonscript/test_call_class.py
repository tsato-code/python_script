import test_class as c


manga_list = []
manga_list.append(c.Manga('Chihayafuru', 'Yuki Suetsugu'))
manga_list.append(c.Manga('Case Closed', 'Gosho Aoyama'))
manga_list.append(c.Manga('Shogi no Watanabe-kun', 'Megumi Ina'))
manga_list.append(c.Manga('Magic Kaito', 'Gosho Aoyama'))
manga_list.append(c.Manga('The Flowers of Evil ', 'Shuzo Oshimi'))
manga_list.append(c.Manga('Chi no Wadachi', 'Shuzo Oshimi'))
manga_list.append(c.Manga('Karakai Jozu no Takagi-san', 'Sōichirō Yamamoto'))
manga_list.append(c.Manga('Kingdom', 'Yasuhisa Hara'))


print('\n* manga list *')
for manga in manga_list:
	manga.print()


"""
$ python test_call_class.py 

* manga list *
Chihayafuru - Yuki Suetsugu
Case Closed - Gosho Aoyama
Shogi no Watanabe-kun - Megumi Ina
Magic Kaito - Gosho Aoyama
The Flowers of Evil  - Shuzo Oshimi
Chi no Wadachi - Shuzo Oshimi
Karakai Jozu no Takagi-san - Sōichirō Yamamoto
Kingdom - Yasuhisa Hara
"""