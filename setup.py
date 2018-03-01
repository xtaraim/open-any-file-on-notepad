>>> helloFile = open('c:\\users\\kiit1\\hello.txt')
>>> helloFile.read()
'Hello world!\nHow are you?'
>>> helloFile.close()
>>> helloFile = open('c:\\users\\kiit1\\hello.txt')
>>> content = helloFile.read()
>>> print(content)
Hello world!
How are you?
>>> helloFile.close()
>>> helloFile = open('c:\\users\\kiit1\\hello.txt')
>>> helloFile.readlines()
['Hello world!\n', 'How are you?']
>>> helloFile.close()
>>> helloFile = open('c:\\users\\kiit1\\hello2.txt', 'w')
>>> helloFile.write('Hello!!!!!!!')
12
>>> helloFile.write('Hello!!!!!!!')
12
>>> helloFile.write('Hello!!!!!!!')
12
>>> helloFile.close()
>>> helloFile.write('Hello!!!!!!!!')
