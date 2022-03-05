# This is a program making file exe from file py (<100 code sentences).

print('This is a program making file exe from file py.')
print('And it will save a file exe to desktop.')
print("""
......................................................................
                           .   .  ....................................
      .  ............             ....................................
       :PJJJJJJJJJJJJ5Y^          ............                       .
       ^&:.......... ?@@5^        ............                       .
       ^#: ^???????:..~7J#:       ............ .!~~~~~~^........     .
       ^#: ^??????????: ^#:       ....    .... ^?    .^~!!!!!!!77::. .
    .  ^#. ^7777777777: ^#.           .!:    . :?   ^#&&&&&&&&&&@&@? .
     ~GG@GGGGGGGGGGGGGGGG@GG^    .....:#&P?^.  :?  .B@@@@@@@@@@@@@B. .
  .  7@@@@&PGG&G&BB#PGB@@@@@~    ^GGPPG@@@@@5^ :?  5@@@@@@@@@@@@@#:  .
     7@@@@G:YY&G^~&J~Y5@@@@@~    .::::^&@BY!:. ^? J@@@@@@@@@@@@@@!   .
     7@@@@B755#YPYP5?PP@@@@@~         .?~.     .7!BBBBBBBBBBBBBB?    .
     7@@@&@@&&&&@@&@&&&&@@@@~     ....    ..... ...............      .
     .:!&~^^^^^^^^^^^^^^!&~:.     ..............                 .....
       :PJJJJJJJJJJJJJJJJ5.       ....................................
      .  ................         ....................................
  .   .                         . ....................................
......................................................................
""")
path = input('Let type the full path of file py: ')
file = input('Let type the full name of file py: ')

import os
import time

# install file by pyinstaller
cd = 'cd ' + '"' + path + '"'
os.system(cd)
pyinst = 'pyinstaller --onefile ' + '"' + file + '"'
os.system(pyinst)

path0 = ' "' + path + '" '

# copy file py to any where
pathpy = ' "' + os.path.join(path, file) + '" '
pathpycopy = 'copy' + pathpy + r'"C:\Program Files" /y'
os.system(pathpycopy)

# copy file exe to any where
pathexe = ' "' + os.path.join(path, 'dist', file.replace('.py', '.exe')) + '" '
pathexecopy = 'copy' + pathexe + r'"C:\Program Files" /y'
os.system(pathexecopy)

# delete file and subfolder in main folder
pathcd = 'cd' + ' "' + path + '" '
os.system(pathcd)
os.system('rd /s /q . 2>nul')

# make file py in main folder
pathpyy = ' "' + os.path.join(r'C:\Program Files', file) + '" '
pathpyycopy = 'copy' + pathpyy + path0 + '/y'
os.system(pathpyycopy)
pathpyydel = 'del /q' + pathpyy
os.system(pathpyydel)

# make file exe in main folder
pathexee = ' "' + os.path.join(r'C:\Program Files', file.replace('.py', '.exe')) + '" '
pathexeecopy = 'copy' + pathexee + path0 + '/y'
os.system(pathexeecopy)
pathexeedel = 'del /q' + pathexee
os.system(pathexeedel)

print('Your task has been performed successfully!')
time.sleep(3)
