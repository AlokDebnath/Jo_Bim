import thesaurus
import pmi

bim_to_jo = {}
similar_jo = []

# for all bim, look at the jos that belong in that bim
i = 0
for bim in thesaurus.Bim_dict:
	for jo in thesaurus.Jo_dict:
		i+=1
		print(i)
		key = jo+"\t"+bim+"\n"
		if key in pmi.sig_score:
			similar_jo.append(jo)

	bim_to_jo[bim] = similar_jo

# for jo_bim in thesaurus.JoBim_dict:
# 	if jo_bim in pmi.sig_score:
# 		similar_jo.append(jo_bim.split("\n")[0].split("\t")[0])

# 	bim_to_jo[jo_bim.split("\n")[0].split("\t")[1]] = similar_jo

print (count(bim_to_jo))