import operator
file1 = open('./mouse_corpus-maltparser','r')
lines = file1.readlines()
Jo_dict = {}
Bim_dict = {}
JoBim_dict = {}
total_count = 0
for line1 in lines:
	line = line1.strip()
	jobim = line.strip().split('\t')
	if 'punct' in jobim[1]:
		continue
	total_count += 1
	
	if line in JoBim_dict:
		JoBim_dict[line] += 1
	else:
		JoBim_dict[line] = 1
	
	if jobim[0] in Jo_dict:
		Jo_dict[jobim[0]] += 1
	else:
		Jo_dict[jobim[0]] = 1
	# print(jobim[1].split('\n')[0])
	if jobim[1] in Bim_dict:
		Bim_dict[jobim[1]] += 1
	else:
		Bim_dict[jobim[1]] = 1
# print(Bim_dict["-pobj(with#IN)"])
sorted_Jo_dict = sorted(Jo_dict.items(), key=operator.itemgetter(1), reverse=True)
sorted_Bim_dict = sorted(Bim_dict.items(), key=operator.itemgetter(1), reverse=True)
sorted_JoBim_dict = sorted(JoBim_dict.items(), key=operator.itemgetter(1), reverse=True)
Jo_count =len(sorted_Jo_dict)
Bim_count =len(sorted_Bim_dict)
JoBim_count =len(sorted_JoBim_dict)

