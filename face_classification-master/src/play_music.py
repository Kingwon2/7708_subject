import pygame
import random
import result
import crawling

def getEmotion(emotion):
    now_emotion = emotion

    randMusicNum = str(random.randrange(1, 7))

    freq = 44100    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
    bitsize = -16   # signed 16 bit. support 8,-8,16,-16
    channels = 1    # 1 is mono, 2 is stereo
    buffer = 2048   # number of samples (experiment to get right sound)

    # default : pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.load("../emotion_result/"+now_emotion+"/"+randMusicNum+".mp3")
    pygame.mixer.music.play()

    crawling.getText()
    L = str(crawling.readSentence())
    result.bitOperation(10, 10, L)

    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(30)
    pygame.mixer.quit() 
