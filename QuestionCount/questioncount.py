
import re
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import operator
import matplotlib.pyplot as plt
import numpy as np


questionCounts = {}
totalCounts = {}
for i in range(1,80):
        file = str(i) + '.txt'
        f = open(file)
        content = f.readlines()
        #print(content)
        for line in content:
                if line.count(":") == 1:
                        speakerSpeech=line.split(':')
                        speaker = speakerSpeech[0]
                        speaker = re.sub(r'\<.*\>', '', speaker)
                        speaker = re.sub(r'\<.*\>', '', speaker)
                        speaker = re.sub(r'\[.*\]', '', speaker)
                        speaker = re.sub(r' ', '', speaker)   
                        speaker = re.sub(r'[^A-Z]+', '', speaker)


                        speech = speakerSpeech[1]
                        count = speech.count('?')
                        sentenceCount = count + speech.count('.') + speech.count('!')
                        if speaker in questionCounts.keys():
                                questionCounts[speaker] += count
                                totalCounts[speaker] += sentenceCount
                        else:
                                questionCounts[speaker] = count 
                                totalCounts[speaker] = sentenceCount          
#print(questionCounts)

sorted_Qcounts = sorted(questionCounts.items(), key=operator.itemgetter(1))

print(sorted_Qcounts)
print()
normalized = questionCounts.copy()
for speaker,qCount in questionCounts.items():
        if qCount != 0:
                normalized[speaker] = normalized[speaker]/float(totalCounts[speaker])

sorted_Ncounts = sorted(normalized.items(), key=operator.itemgetter(1))

print(sorted_Ncounts)


objects = ('Kirk','McCoy', 'Spock','Scott', 'Sulu','Uhura','Chekov','Pike','Chapel')
freqs =  [questionCounts[a.upper()] for a in objects] 
normfreqs =  [normalized[a.upper()] for a in objects] 

ypos = np.arange(len(objects))
print(freqs,ypos)
plt.bar(ypos,freqs,align='center',alpha =0.5)
plt.xticks(ypos,objects)
plt.ylabel('Number of Questions Asked by Character')
plt.xlabel('Top Characters')
plt.title('Frequency of Questions per Character in Star Trek')
plt.savefig('absoluteFreqs.png')
plt.show()


#plot normalized question frequencies
plt.bar(ypos,normfreqs,align='center',alpha =0.5)
plt.xticks(ypos,objects)
plt.ylabel('Number of Questions, Divided by Character\'s Total Lines')
plt.xlabel('Top Characters')
plt.title('Normalized Frequency of Questions per Character in Star Trek')

#plt.show()
plt.savefig('normalizedFreqs.png')





