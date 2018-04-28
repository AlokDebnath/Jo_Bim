import operator
file1 = open('./JoBims/mouse_corpus-maltparser','r')
lines = file1.readlines()
Jo_dict = {}
Bim_dict = {}
JoBim_dict = {}
total_count = 0
for line in lines:

	jobim = line.split('\t')
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

	y = ""
	for c in jobim[1]:
		y += c
		if(c=='('):
			y += '@_'
	if y in Bim_dict:
		Bim_dict[y] += 1
	else:
		Bim_dict[y] = 1


sorted_Jo_dict = sorted(Jo_dict.items(), key=operator.itemgetter(1), reverse=True)
sorted_Bim_dict = sorted(Bim_dict.items(), key=operator.itemgetter(1), reverse=True)
sorted_JoBim_dict = sorted(JoBim_dict.items(), key=operator.itemgetter(1), reverse=True)

Jo_count =len(sorted_Jo_dict)
Bim_count =len(sorted_Bim_dict)
JoBim_count =len(sorted_JoBim_dict)