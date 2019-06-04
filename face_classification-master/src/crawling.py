import random
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

L=[]

def getText() :
    randPageNum = str(random.randrange(1, 3000))
    
    html = urlopen("https://talktalkhealing.tistory.com/"+randPageNum)

    bsObj = BeautifulSoup(html, "html.parser")
           
    list = bsObj.findAll("h3", {"class" : "tit_post"})

    f = open('../emotion_result/write.txt','w')       
    for item in list:
        f.write(item.getText())


    f.close()

'''
def download_img(url):
    name = "img"
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_img("https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F26187936555C4B282A41E9")
'''

def readSentence() :
    file=open('../emotion_result/write.txt','r')

    while (1):
        line=file.readline()

        try:escape=line.index('\n')
        except:escape=len(line)
        
        if line:
            L.append(line[0:escape])
        else:
            break
        
    file.close()

    return L
