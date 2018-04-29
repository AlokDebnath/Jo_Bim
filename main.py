import agg_graph

def GetDTofWord(word):
	print("\n--------------------------------------------------------------------------------------------------------")

	print("Distributional Thesaurus For: {}\n\n".format(word))
	for syn,val in sorted(agg_graph.jos_spliced[word].items(), key=lambda x: x[1], reverse=True):
		if val >= 2:
			print(syn, val)
	print("--------------------------------------------------------------------------------------------------------\n\n\n")

arr = ["no", "n", "N", "No"]

while True:
	input1 = input("Do you want to give a word?\t")
	if input1 in arr:
		break
	else:
		inp = input("Enter word:\t")
		try:
			GetDTofWord(inp)
		except KeyError:
			print("Not available") 
# print(sorted(agg_graph.jos_agg['horse#NN'].items(), key=lambda x: x[1]))