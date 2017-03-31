import pandas as pd
import numpy as np
from feature_extraction import extract_mfccs
from machine_learning import knn
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Reading features into Dataframes
# Violin
philharmonia_violin = extract_mfccs("violin","single_notes","philharmonia",13)
university_of_iowa_violin = extract_mfccs("violin","single_notes","university_of_iowa",13)
vsco2_violin = extract_mfccs("violin","single_notes","vsco2",13)
freesound_mtg_violin = extract_mfccs("violin","single_notes","freesound_mtg",13)
freesound_ldk1609_violin = extract_mfccs("violin","single_notes","freesound_ldk1609",13)

# Flute
philharmonia_flute = extract_mfccs("flute","single_notes","philharmonia",13)
university_of_iowa_flute = extract_mfccs("flute","single_notes","university_of_iowa",13)
freesound_mtg_flute = extract_mfccs("flute","single_notes","freesound_mtg",13)
vsco2_flute = extract_mfccs("flute","single_notes","vsco2",13)
freesound_carlos_vaquero_flute = extract_mfccs("flute","single_notes","freesound_carlos_vaquero",13)


# Train a knn on philharmonia dataset and test on university_of_iowa dataset
train = pd.concat([philharmonia_violin,philharmonia_flute,vsco2_violin,vsco2_flute,freesound_mtg_flute,freesound_carlos_vaquero_flute,freesound_mtg_violin,freesound_ldk1609_violin])
test = pd.concat([university_of_iowa_violin,university_of_iowa_flute])
xtrain = np.array(train.ix[:, 2:train.shape[1]-1])
ytrain = np.array(train['classification'])
xtest = np.array(test.ix[:, 2:test.shape[1]-1])
ytest = np.array(test['classification'])
xtrain_scaled = normalize(xtrain)
xtest_scaled = normalize(xtest)
#logreg = linear_model.LogisticRegression()
#logreg.fit(xtrain_scaled,ytrain)
#pred = logreg.predict(xtest_scaled)
gnb = SVC()
gnb.fit(xtrain_scaled,ytrain)
pred = gnb.predict(xtest_scaled)
print(accuracy_score(ytest,pred))
# for k in range(1,100):
#     if(k%2==1):
#         knn1 = knn(xtrain_scaled,ytrain,k,'euclidean','knn1.pkl')
#         pred = knn1.predict(xtest_scaled)
#         with open('/home/dan/university/project/results/cross_dataset_testing/results3.csv','a') as myfile:
#             print(str(k)+","+str(accuracy_score(ytest,pred)),file=myfile)
