# pmi (x;y) = log p(x,y) / p(x) p(y)
# pmi (jo;bim) log p(jo-bim) / p(jo) p(bim)

from math import log
import thesaurus

jo_bim_count = thesaurus.total_count

prob_jo= {}
prob_bim = {}
prob_jo_bim = {}
sig_score = {}

for jo, count in thesaurus.Jo_dict.items():
	prob_jo[jo] = count/jo_bim_count

for bim, count in thesaurus.Bim_dict.items():
	prob_bim[bim] = count/jo_bim_count

for jo_bim, count in thesaurus.JoBim_dict.items():
	prob_jo_bim[jo_bim] = count/jo_bim_count
for jo_bim in thesaurus.JoBim_dict:
	spliced = jo_bim.split('\n')[0]
	jo = spliced.split('\t')[0]
	bim = spliced.split('\t')[1]
	sig_score[jo_bim] = log ((prob_jo_bim[jo_bim]) / (prob_jo[jo]) * prob_bim[bim])