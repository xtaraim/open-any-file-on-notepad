import shelve
>>> shelve.open('mydata')
<shelve.DbfilenameShelf object at 0x05B4EA70>
>>> shelfFile = shelve.open('mydata')
>>> shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
>>> shelfFile.close()
>>> shelfFile = shelve.open('mydata')
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
>>> shelfFile.close()
>>> #copy given path open file on notepad and paste path
>>> shelfFile = shelve.open('mydata')
>>> shelfFile.keys()
KeysView(<shelve.DbfilenameShelf object at 0x05B4EA70>)
>>> list(shelfFile.keys())
