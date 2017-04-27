- Step 1: Install your compatible program environment for Java or python
- Step 2: set up NLP library (spaCy NLTK Stanford)
- Step 3: Write a program which reads a text file line by line and perform POS tagging and write back the file
- Step 4: Study basic english grammar. What are the parts of Speech. 
- Step 5: make rule to merge certain POS tag of similar nature to produce a chanker style language. For Example: different forms of Verb are still verbs. merge them.
- Step 6: Write a program (extending step 3), which 
  - POS tag a sentence
  - Perform the merge of tokens
  - Identify verbs and Nouns in sentence
  - Write the result in a file.
- Step 7: Write a program to Implement NER 
- Step 8: Merge NER in Step 6.

```
Input: John went to the United States for his school
Output1: John_NOUN went_VERB to the United_NOUN States_NOUN for his_NOUN school_NOUN
Output2: John_NOUN went_VERB to the United_States_NER for his_NOUN school_NOUN
```

**note:**
- 1: you can use any language/annotation style
- 2: PTB POS tags: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

