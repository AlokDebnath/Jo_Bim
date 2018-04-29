# Team: Abheet Sharma(20161091), Alok Debnath(20161122), Tanmai Khanna(20161212)
# How to Run:
1.	Run main.py using python3
2.	Two options will be given: Entire DT will be created and stored in DT.txt ....OR.... A DT will be printed to terminal given input word.
3.	Selecting option 1(by typing in the option number) will create a file called DT.txt which has the DT for all words in the corpus.
4.	Selecting option 2 will then ask you for an input word, upon entering will print the DT for that word.



# Distribution of Work
1.	Abheet: Made the graph and similarity clustering of jo's.
2.	Alok: Did signifance score calculation, pruning and sorting.
3. 	Tanmai: Jo Bim extraction, counting, pruning and sorting.

Basically, Tanmai did the 1st part, Alok the 2nd part and Abheet did the 3rd part(we all helped each other out, so we didn't just strictly do our parts)


# What each file does
1.	jobimcount.py extracts the jo's, bim's, and jobim's with their counts and sorts them.
2.	pmi.py calculates probability for each jo, bim, jobim occuring and provides a significance score to each jobim using PMI and later prunes them.
3.	agg_graph.py aggregates the jo's per bim into a graph where a jo is connected to a bim if it occurs in that bim.
4.	main.py creates the entire DT or prints out a DT for a word on input.
5.	mouse_corpus is the corpus we used.
6.	mouse_corpus-maltparser contains the JoBim pairs extracted from mouse-corpus with each Jo and Bim being POS-tagged and Dependancy parsed.
7.	DT.txt has all the DT's for each word in the corpus. 
