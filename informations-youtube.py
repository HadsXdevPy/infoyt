import os
from getpass import getpass
try:
    import pytube
    from pytube import YouTube

except ModuleNotFound:
    os.system('pip install pytube')

try:
    os.system('clear')
    os.system('figlet -f slant info yt')
    print('[+] informations youtube')
    link=input('[+] Link video : ')
    yt=YouTube(link)
    print('[+] Judul : {}'.format(yt.title))
    print('[+] channel : {}'.format(yt.author))
    print('[+] views : {}'.format(yt.views))
    print('[+] durasi : {}'.format(yt.length))
    print('[+] deskripsi : {}'.format(yt.description))
except KeyboardInterrupt:
    print('\n[+] dihentikan')

