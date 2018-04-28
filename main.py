import agg_graph

def GetDTofWord(word):
	print("\n\n--------------------------------------------------------------------------------------------------------\n")

	print("Distributional Thesaurus For : {}\n\n".format(word))
	for syn,val in sorted(agg_graph.jos_agg[word].items(), key=lambda x: x[1], reverse=True):
		if val >= 2:
			print(syn, val)
	print("--------------------------------------------------------------------------------------------------------\n\n\n\n")

while True:
	inp = input("Enter word:")
	try:
		GetDTofWord(inp)
	except KeyError:
		print("Not available") 
# print(sorted(agg_graph.jos_agg['horse#NN'].items(), key=lambda x: x[1]))