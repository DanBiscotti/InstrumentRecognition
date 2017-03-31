# This module is used to extract features from datasets for use in as training and testing data

# Libraries
from os.path import exists # Checks if given path exists
from os import listdir # Used to list all filenames in a directory
from librosa import load # Loads an audio file
from librosa.feature import mfcc # Extracts mfcc features
import pandas as pd # Library for reading and writing csv files

def extract_mfccs(instrument,sample_type,dataset,n_mfccs):
    "Function that will extract mfccs from all the files in a given directory"
    mfcc_list=[]
    directory="/home/dan/university/project/datasets/"+instrument+"/"+dataset+"/"
    outputfile="/home/dan/university/project/source/data/"+instrument+"_"+sample_type+"_"+dataset+"_"+n_mfccs+".csv"
    if exists(outputfile):
        return pd.read_csv(outputfile)
    if exists(directory):
        samples = listdir(directory)
        for sample in samples:
            try:
                y, sr = load(directory+sample)
                res = mfcc(y, sr, n_mfcc=n_mfccs)
                for x in range(0,res.shape[1]):
                    sum=0
                    for x2 in range(1,n_mfccs):
                        sum+=res[x2,x]
                    if(sum>0.1):
                        l = []
                        for x3 in range(0,n_mfccs):
                            l.append(res[x3,x])
                        l.append(instrument)
                        mfcc_list.append(tuple(l))
            except:
                print("error for " + directory + sample)
        if not mfcc_list:
            return
        column_headers=[]
        for x in range(1,n_mfccs+1):
            column_headers.append('mfcc'+str(x))
        column_headers.append('classification')
        df = pd.DataFrame(mfcc_list,columns=column_headers)
        df.to_csv(outputfile)
        return df
    else:
        print(directory+" does not exist")

                            
