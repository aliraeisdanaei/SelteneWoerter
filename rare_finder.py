from bs4 import BeautifulSoup # to parse htlm
import codecs #to read the files
from nltk import word_tokenize # to separate into words
from nltk import FreqDist #to get frequencu table 
import os #to get fiel directory 
import glob #to get file directories at the same time 
import re #regular expressions
import pandas as pd # to make data frames 

import sys #for the argv use

# if no value is given as a parameter the top 20 rare words are found
top_n_rare = 20 
if len(sys.argv) != 1:
	top_n_rare = int(sys.argv[1])

#it has been assumed that the freqTable is uptodate
# perhaps a script here is needed to  automatically determine if it requires updating
freqTable = pd.read_csv('./frequencyTable.txt') 
freqTable.columns = ['word', 'frequency'] # gives column headers
# print(freqTable)


cwd = os.getcwd() #getting current directory 
files = glob.glob(cwd + '/*transkript.html') #getting all file names with this specified pattern

def determinePodcastNumber(file) -> str:
	# this function assumes this format for the transkript names
	# egp<number>_transkript.html
	return (str(file)).split('egp')[1].split('_')[0]

for file in files: 
	opener = codecs.open(file, "r", "utf-8") #opening all files
	soup = BeautifulSoup(opener, 'html.parser') #parsing the htlm files
	text = soup.get_text() #getting the text
	withoutHeader = text[text.find('www.easygerman.fm'):] #getting read of the header
	withoutPunctiation = re.sub(r'[^\w\s]','',withoutHeader) #cleaning corpus 
	withoutNumbers = re.sub(r'[0-9]','',withoutPunctiation)
	withoutLink = withoutNumbers.replace('wwweasygermanfm', '')
	cleaned = withoutLink.replace('Cari', '')
	cleaned = cleaned.replace('Manuel', '')
	cleaned = cleaned.replace('Janusz', '')
	cleaned = cleaned.replace('Isi', '')
	words = word_tokenize(cleaned) #tokenezing cleaned corpus
	lowerCase = [each_string.lower() for each_string in words]

	currentWords = pd.DataFrame({'word':lowerCase})
	# print(currentWords)
	
	# takes the natural joic of currentWords & freqTable & sorts them based on frequency
	# occuring_words = lowerCase_set & freqTable_words_Desc
	# top_rare_list = list(occuring_words)[:top_n_rare]
	occuring_words = pd.merge(currentWords, freqTable).sort_values(by=['frequency'])
	# print(occuring_words)

	top_rare = occuring_words.head(top_n_rare)
	print("Top " + str(top_n_rare) + " seltene Wörter in egp" + determinePodcastNumber(file) + ":", list(top_rare.iloc[:, 0].values))

	rare_filename = 'egp' + determinePodcastNumber(file) + "_selteneWörter.txt" #setting a file name based on the podcast number
	top_rare.to_csv(rare_filename, header=False, index=False) #saving it 

