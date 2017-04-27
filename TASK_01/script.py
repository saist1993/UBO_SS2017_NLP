import spacy

nlp = spacy.load('en')

text = unicode(open('input.txt','r').read())
processed_text = nlp(text)

#Merging code
'''
	Logic to merge all
		Nouns
		Verbs
		Adverbs
		Adjectives
'''

output_string_pos = ''

# print ' '.join([x.tag_ for x in processed_text])
merging_map = {'N':'NN','R':'RB','V':'VB','J':'JJ','PR':'NN'}

for i in range(len(processed_text)):
	current_token = processed_text[i]

	if current_token.ent_type == 0:
		#Then nevermind.
		ner = ''
	else:
		#See if there are more tokens and if so, do they have the same NER
		if i >= len(processed_text) - 1:
			#This is the last token and the NER Needs to come in the tag
			ner = '_'+current_token.ent_type_
		else:
			#There are more NERs. See if they too have the same NER tag
			next_token = processed_text[i+1]
			if next_token.ent_type == current_token.ent_type:
				ner = ''
			else:
				#This is the last word with this NER tag
				ner = '_'+current_token.ent_type_


	if current_token.tag_[0] in merging_map.keys():
		current_token.tag_ = merging_map[current_token.tag_[0]]
		output_string_pos += current_token.text+'_'+current_token.tag_+ner+' '
		continue

	if current_token.tag_[:2] in merging_map.keys():
		current_token.tag_ = merging_map[current_token.tag_[:2]]
		output_string_pos += current_token.text+'_'+current_token.tag_+ner+' '
		continue		

	output_string_pos += current_token.text+ner+' '

f = open('output.txt','w+') 
f.write(output_string_pos)
f.close()
print 'Tschuss'



