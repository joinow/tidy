import io,os,sys
import json
import re

import profile
import probe

PATH = "e:/temp/toprocess/"
INDEX = 'e:/ffmout/bookout.json'
OUTPUT = 'e:/ffmout/rename.txt'

top = PATH
if len(sys.argv) > 1:
    top = sys.argv[1]
print('clean path:' + top)
compare = ''

fnd = [
    r'[\?？]{1}',r'（((全|共)[^）]*|上(、)*中(、)*下|上(、)*下[^）]*|增补本|校[订定]*本|(新)*典藏版|精装|平装)）',
    r'"',r'[:：]{1}',r'[，]+',r'["“”]{1}',r'[《]+',r'[》]+',
    r'（(上|下)）',r'（第([\d一二三四五六七八九十]*)[册|部|卷]*）',
]

rep = [
    r'',r'',
    r'"',r'.',r',',r"'",r'{',r'}',
    r'#\1',r'#\1',
]

def rename(book):
    tgtname=book
    for i in range(len(fnd)):
        tgtname=re.sub(fnd[i], rep[i], tgtname)
    newline = book+' -> '+tgtname+'\n'
    return newline

for root, dirs, files in os.walk(top, topdown=False):
    # books = list(map(lambda x: x[:x.rindex('.')], files[:100]))
    books = list(map(lambda x: x[:x.rindex('.')], files))
    for book in books:
        compare = compare + rename(book)
    fp = open(OUTPUT, 'w', encoding='utf8')
    fp.write(compare)
    fp.close()
