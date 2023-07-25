import binascii
import time
import re

def containsKorean(text):
    pattern = re.compile(r'[\uac00-\ud7af\u1100-\u11ff\u3130-\u318f\ua960-\ua97f\uac00-\ud7af]')
    return bool(pattern.search(text))

method = ['cp949','ASCII', 'utf-8', 'utf-16', 'utf-32', 'Latin-1', 'CP1252', 'EUC-KR', 'Shift_JIS', 'GBK', 'CP437', 'CP949', 'utf-16le', 'utf-16be', 'KOI8-R']
text = []


cmd = 1 
k = open("decode_보안제품개발.txt",'w')
with open('context.enc','rb') as fp:

    while True:
       
        tmp = fp.readline()
    
        if not tmp:
            break
        tmp = tmp[:-1]

        if tmp[0:3] == b'\x00\x00\x00':
            tmp = tmp[3:]
    
        elif tmp[0:1] == b'\x00':
            tmp = tmp[1:]
        for j in method:
            try:
                decoded_tmp = tmp.decode(j)
                k.write(decoded_tmp+'\n')
                print(decoded_tmp)
                break

            except UnicodeDecodeError:
                continue