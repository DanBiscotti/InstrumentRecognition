from pydub import AudioSegment
from os import listdir
from random import randint

instruments = ['altosax','bassoon','cello','clarinet','doublebass','flute','guitar', \
               'horn','oboe','trombone','trumpet','tuba','violin']
count=1
while (count<=5000):
    instrument1 = instruments[randint(0,len(instruments))-1]
    instrument2 = instruments[randint(0,len(instruments))-1]
    while(instrument1==instrument2):
        instrument2 = instruments[randint(0,len(instruments))-1]
    directory = "/home/dan/university/project/datasets/monophonic/"
    path1 = directory+instrument1+"/"
    path2 = directory+instrument2+"/"
    dataset1 = listdir(path1)
    path1 = path1 + dataset1[randint(0,len(dataset1))-1] + "/"
    dataset2 = listdir(path2)
    path2 = path2 + dataset2[randint(0,len(dataset2))-1] + "/"
    sample1 = listdir(path1)
    path1 = path1 + sample1[randint(0,len(sample1))-1]
    sample2 = listdir(path2)
    path2 = path2 + sample2[randint(0,len(sample2))-1]
    audio1, audio2 = None, None
    if "wav" in path1:
        audio1 = AudioSegment.from_wav(path1)
    else:
        audio1 = AudioSegment.from_mp3(path1)
    if "wav" in path2:
        audio2 = AudioSegment.from_wav(path2)
    else:
        audio2 = AudioSegment.from_mp3(path2)
    if (len(audio1)>500 and len(audio2)>500):
        combined = audio1.overlay(audio2)
        smallest = len(audio1)
        if(len(audio1)>len(audio2)):
            smallest=len(audio2)
        combined_shortened = combined[:smallest]
        combined_shortened.export("/home/dan/university/project/datasets/polyphonic/combined_2/"+\
                                  instrument1+"_"+instrument2+"_"+str(count)+".wav",format='wav')
        count=count+1




