''' Change the reader file for changing the input'''
#importing essential libraries
import spacy

#loading the nlp english model (spacy)
nlp = spacy.load('en')

fname="reader.txt"
fname_writer = "writer.txt"

#parsing the file with end line
sentences = open(fname).read().split('\n')
writer = open(fname_writer,"w+")
final_sentences = []


for sent in sentences:
	#converting the sentence into utf-8 encoding and encoding it as spacy object
	writer.write("original sentence is : " + sent + "\n")
	sent = nlp(unicode(sent,"utf-8"))
	pos_tag_seq = [] #prints the pos tag sequence.
	merged_pos_tag_seq = [] #prints the merged pos tag sequence 
	ner = []	#stores the NER sequence.	
	for word in sent.ents:
		ner.append(word)
	for i in xrange(0,len(sent)):
		pos_tag_seq.append(str(sent[i].text) + "_" + sent[i].pos_) #implements POS TAgging
		if sent[i].tag_ == "NN" or sent[i].tag_ == "NNS" or sent[i].tag_ == "NNP" or sent[i].tag_ == "NNPS": #implements Merger TODO:Add other rules
			merged_pos_tag_seq.append(str(sent[i].text) + "_" + "NOUN")
		elif sent[i].tag_ == "JJ" or sent[i].tag_ == "JJR" or sent[i].tag_ == "JJS" : #implements Merger TODO:Add other rules
			merged_pos_tag_seq.append(str(sent[i].text) + "_" + "ADJ")
		elif sent[i].tag_ == "RB" or sent[i].tag_ == "RBR" or sent[i].tag_ == "RBS" : #implements Merger TODO:Add other rules
			merged_pos_tag_seq.append(str(sent[i].text) + "_" + "ADV")
		elif sent[i].tag_ == "VB" or sent[i].tag_ == "VBD" or sent[i].tag_ == "VBG" or sent[i].tag_ == "VBN" or sent[i].tag_ == "VBP" or sent[i].tag_ == "VBZ": #implements Merger TODO:Add other rules
			merged_pos_tag_seq.append(str(sent[i].text) + "_" + "VERB")			
		else:
			merged_pos_tag_seq.append(str(sent[i].text) + "_" + sent[i].pos_)
	#Merging NER tags 		
	ner_seq = []
	for i in xrange(0,len(sent)):
		flag = True
		for word in ner:
			if sent[i] in word:
				ner_seq.append([sent[i].text,"NER"])
				flag = False
		if flag:
			ner_seq.append([sent[i].text,sent[i].pos_])		
	#printing NER mergers with other pos tags 
	merged = []
	skipping = 0
	for i in range(0,len(ner_seq)):
		
		if skipping != 0 :
			skipping = skipping - 1
			continue
		if ner_seq[i][1] == "NER":
			skipping = 0
			temp = []
			temp.append(ner_seq[i][0])
			flag = True
			while(flag):
				if i < len(ner_seq):
					if ner_seq[i+1][1] == "NER":
						temp.append(ner_seq[i+1][0])
						skipping = skipping + 1
						i = i + 1
					else:
						flag = False	
				else:
					flag= False
			merged.append(" ".join(temp) + "_NER")
		else:
			merged.append(" ".join(ner_seq[i]))
	print "POS seq : " + " ".join(pos_tag_seq)
	print "Merged pos seq : " + " ".join(merged_pos_tag_seq)
	print "NER seq : " + " ".join(merged)

	writer.write("POS seq : " + " ".join(pos_tag_seq) + "\n")				
	writer.write("Merged pos seq : " + " ".join(merged_pos_tag_seq) + "\n")
	writer.write("NER seq : " + " ".join(merged) + "\n")
	writer.write("\n")
