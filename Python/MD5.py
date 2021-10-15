# Szyfrowanie MD5

from hashlib import md5
while True:
    txt= input("Text: ")
    txt = txt.encode("utf-8")
    txt = md5(txt)
    print("Szyfr MD5:", txt.hexdigest(), "\n")