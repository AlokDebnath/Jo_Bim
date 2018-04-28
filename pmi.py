# pmi (x;y) = log p(x,y) / p(x) p(y)
# pmi (jo;bim) log p(jo-bim) / p(jo) p(bim)

from math import log
import jobimcount

jo_bim_count = jobimcount.total_count

prob_jo= {}
prob_bim = {}
prob_jo_bim = {}
sig_score = {}

for jo, count in jobimcount.Jo_dict.items():
	prob_jo[jo] = count/jo_bim_count

for bim, count in jobimcount.Bim_dict.items():
	prob_bim[bim] = count/jo_bim_count

for jo_bim, count in jobimcount.JoBim_dict.items():
	prob_jo_bim[jo_bim] = count/jo_bim_count

for jo_bim in jobimcount.JoBim_dict:
	spliced = jo_bim
	jo = spliced.split('\t')[0]
	bim = spliced.split('\t')[1]
	log_score = log(prob_jo_bim[jo_bim]/(prob_jo[jo] * prob_bim[bim]))
	if log_score >= 4.0:
		sig_score[jo_bim] = log_score
	# print(prob_jo[jo], prob_bim[bim], prob_jo_bim[jo_bim])

# print(len(sig_score))
sorted_sig_score = sorted(sig_score.items(), key= lambda x: x[1], reverse=False)
