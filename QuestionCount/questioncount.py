
import re
import operator

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
normalized = questionCounts
for speaker,qCount in questionCounts.items():
        if qCount != 0:
                normalized[speaker] = normalized[speaker]/float(totalCounts[speaker])

sorted_Ncounts = sorted(normalized.items(), key=operator.itemgetter(1))

print(sorted_Ncounts)