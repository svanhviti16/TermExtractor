# this class, given a corpus object and a file path will handle the brat format creation
class brat():

	def __init__(self, corpus, file_path):

		#TODO: do we need a warning if overwriting excisting files.

		try:
			self.txt_file = open(file_path + ".txt", mode = "w")
			self.ann_file = open(file_path + ".ann", mode = "w")
		
		except OSError:

			print("Unable to open files for brat export")
			exit(-1)

		self.class_dict = {
			"PER": "Person", 
			"LOC": "Location", 
			"ORG": "Organization", 
			"MIS": "Miscellaneous", 
			"UCAT": "Uncategorized"
		}
		
		# the char index for start of sentence
		char_index = 0
		# the line index in the brat annotation file
		ann_num = 1		 


		for sentence in corpus.sentences:

			# write untokenized sencence to txt file
			self.txt_file.write(str(sentence))

			# start with the first NE-token in current sencence
			ne_token_index = 0

			while ne_token_index < len(sentence.all_ne_tokens):

				# get class of current NE token
				tok_class = sentence.get_class(ne_token_index, False)		

				start_index = char_index + sentence.get_ne_token_start_char_index(ne_token_index)

				# when a NE is made from only a single token we know that its class designation has less than 5 chars 
				if len(tok_class) < 5:
					# we have to get the original form of the token from the corpus... not the lemma stored in NE list
					ne = sentence.corpus_tuples[sentence.all_ne_tokens_indexes[ne_token_index]][0]
					
					# base case: a single token NE, increment NE index by 1 only
					ne_token_index_increment = 1

				# a class designation of 5 characters tells us the NE is made up of more than one token
				# we have to take care of merging them for the brat format				
				elif len(tok_class) == 5:

					# counter keeping track of NE ending token offset from the start token
					merged_ne_token_offset = 1

					# token class to be expected for the following class
					expected_tok_class = "I" + tok_class[1:]

					# while staying within the NE list and the following token class is a I- version of the first one, increment offset to check one further token
					while (ne_token_index + merged_ne_token_offset) < len(sentence.all_ne_tokens) and expected_tok_class == sentence.get_class(ne_token_index + merged_ne_token_offset, False):
						merged_ne_token_offset += 1

					ne = sentence.get_merged_tokens(ne_token_index, merged_ne_token_offset)

					ne_token_index_increment = merged_ne_token_offset 

					# slice I- from the beginning of tok_class so the dict lookup will work
					tok_class = tok_class[2:]

				else:
					#If we get unexpected length of class designation we want to know --> terminate with an appropriate message
					print("Brat export recieved a token class designation of more than 5 chars :/")
					exit(-1)

				end_index = start_index + len(ne)
		 
				ann_string = "T" + str(ann_num) + "\t" + self.class_dict[tok_class] + " " + str(start_index) + " " + str(end_index) + "\t" + ne + "\n"
				self.ann_file.write(ann_string)

				# increment annotation number
				ann_num += 1

				# increment acc. to number of ne tokens covered so far
				ne_token_index += ne_token_index_increment

			# update character index to be beginning of next sentence. The additional on accounts for a included newline
			char_index += sentence.get_char_count() + 1

		# cleaning up!
		self.txt_file.close()
		self.ann_file.close()
 

