# -*- coding: utf-8 -*-
import codecs
import unicodedata
import string
import sys
from itertools import groupby
from operator import itemgetter
# from docx import Document


# Auxiliary functions
def is_greek(term):
	return 'GREEK' in unicodedata.name(term.strip()[0])

def is_english(term):
	return 'LATIN' in unicodedata.name(term.strip()[0])

def check_good(char, word_list, index):
	is_eng = is_english(char)
	symbols = "~`!@#$%^&*()_-+={}[]:>;'.</?*-+"
	if char in symbols:
		next_spec = is_english(word_list[min(len(word_list)-1,index+1)]) 
		prev_spec = is_english(word_list[max(0, index-1)])
		return (is_eng or prev_spec or next_spec)
	else:
		return is_eng

def get_item(group): 
	return list(map(itemgetter(1), group))

####################--Main Program--####################

# if ".doc" in sys.argv[1]:
# 	# document = opendocx(sys.argv[1])
# 	# docbody = document.xpath('/w:document/w:body', namespaces=wordnamespaces)[0]
# 	# inFile = getdocumenttext(document)
# else:
inFile = open('./'+sys.argv[1], 'r', encoding='utf-8')

outFile = open('./'+sys.argv[2], 'w', encoding='utf-8')
outFile.seek(0)

for line in inFile:
	words = line.split()
	idxs = [idx for idx, word in enumerate(words) if check_good(word[0], words, idx)]
	# comp_idxs = [idx for i, idx in  enumerate(idxs) if idxs[-]]
	comp_idx = [get_item(g) for k, g in groupby(enumerate(idxs), lambda i: i[0] - i[1])]
	clean_idx = [[lst[0],lst[-1]] for lst in comp_idx]
	out_words = words[:]
	cnt = 0
	for idx in clean_idx:
		out_words.insert(idx[0]+cnt, '\\'+sys.argv[3])
		out_words.insert(idx[-1]+2+cnt, '\\'+sys.argv[4])
		cnt += 2
	out_line = ' '.join(out_words)
	outFile.write(out_line)

outFile.close()
inFile.close()



