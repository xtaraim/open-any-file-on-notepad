baconFile = open('bacon.txt', 'w')
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> import os
>>> os.getcwd()
'C:\\Python36-32'
>>> print(os.getcwd())
C:\Python36-32
\
>>>  #copy given path open file on notepad and paste path
>>> baconFile = open('batch.txt', 'a')
>>> baconFile.write('\n\nBacon is delicious.')
21
>>> baconFile.close()
