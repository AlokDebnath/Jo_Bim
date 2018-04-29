import agg_graph
import sys
def GetDTofWord(word):
	sorted_vals = sorted(agg_graph.jos_spliced[word].items(), key=lambda x: x[1], reverse=True)
	if sorted_vals == []:
		return True

	print("\n--------------------------------------------------------------------------------------------------------")

	print("Distributional Thesaurus For: {}\n\n".format(word))

	val_first = sorted_vals[0][1]
	flag = 0
	if val_first == 1:
		flag = 1
	count = 0
	for syn,val in sorted_vals:
		if flag == 1 and count < 10:
			print(syn, val)
			count += 1
			continue
		if val >= 2:
			print(syn, val)
	print("--------------------------------------------------------------------------------------------------------\n\n\n")


arr = ["no", "n", "N", "No"]

inp1 = input("Select option (Enter number)\n1.Create an entire DT for each word?\n2.Display DT for a word on input?\n\nEnter option:\t")
if inp1 == '1':
	sys.stdout=open("DT.txt","w")
	for jo in agg_graph.jos_spliced:
		GetDTofWord(jo)
	sys.stdout.close()

elif inp1 == '2':
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