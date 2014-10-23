ballot_list = []
# class Election:


class Candidate:

	def __init__(self,name, candidate_number):
		self.name = name
		self.number = candidate_number 
		self.count = 0
		self.cand_ballot = []					
	
	def cand_number(self):
		return self.number

	def cand_name(self):
		return self.name

	def cand_votecount(self):
		return self.count	
	
	def view_ballot(self):
		return self.cand_ballot	

	def cache_ballot(self, ballot):	
		self.cand_ballot.append(ballot)
		self.count += 1 

	def mod_ballot(self):
		for x in self.cand_ballot:
			del x[0]

	def get_vote(self):
		for x in self.cand_ballot:
			return x[0]		

class Ballot: 
	def __init__(self, prefs):
		self.index = 0
		self.votes = list(prefs)

def read(r):
	infile = open(r,'r')
	num_elections = int(infile.readline())
	assert type(num_elections) == int
	infile.readline()

	while num_elections != 0:
		num_candidates = int(infile.readline())
		assert type(num_candidates) == int
		cand_list = []
		for i in range (num_candidates):
			cand_list.append(Candidate(infile.readline().rstrip(), i+1 ))

		line = infile.readline()
		while line != '' and line != '\n':
			tmp = Ballot(line.rstrip().split(' '))
			ballot_list.append(tmp.votes)
			cand_list[int(tmp.votes[0])-1].cache_ballot(tmp.votes)
			line = infile.readline()
		total_ballot = len(ballot_list)	
		winners = solve_election(cand_list, total_ballot)
		#w.write(winners)
		num_elections -= 1

	return num_elections, cand_list, ballot_list, num_candidates, total_ballot, winners

def test_winner(vote_dict, total_ballot):
	haswinner = False
	winner = ''
	for k,v in vote_dict.items():
		if float(float(v)/float(total_ballot)) > float(0.5):
			haswinner = True
			winner = k
	return winner, haswinner

def test_tie(vote_list):
	hastie = True
	for x in range(1,len(vote_list)):
		if vote_list[0] != vote_list[x]:
			hastie = False
			break
	return hastie 

def loser(vote_list, vote_dict, cand_list):

	loser_list = []
	loser_vote = min(vote_list) 
	for k,v in vote_dict.items():
		if v == loser_vote:
			loser_list.append(k)

	cand_loser = []
	tmp1 = cand_list
	for loser in loser_list:
		for n in tmp1:
			if loser == n.name:
				cand_loser.append(n)
				cand_list.remove(n)

	cand_id_list = []
	for cand in cand_list:
		cand_id_list.append(cand.number)	

	for loser in cand_loser:
		loser.mod_ballot()
		ball = loser.view_ballot()
		for b in ball:
			while int(b[0]) not in cand_id_list:
				b.remove(b[0])
			for cand in cand_list:
				if int(b[0]) == cand.number:
					cand.cache_ballot(b)

	return cand_list			
	
def solve_election (cand_list, total_ballot, w):

	while True:
		vote_dict = {}
		vote_list = []
		for n in cand_list:
			vote_dict[n.name] = n.cand_votecount()
			vote_list.append(n.cand_votecount())

		Winner, hasWinner = test_winner(vote_dict, total_ballot)

		if(hasWinner):
			return (Winner, '\n')
			break

		if(test_tie(vote_list)):
			x = ''
			for cand in cand_list:
				x += str(cand.name) + '\n'
			return (x)
			break
		
		cand_list = loser(vote_list, vote_dict, cand_list)
		
def final_election(r, w):
	num_elections, cand_list, ballot_list, num_candidates, total_ballot, winners = read(r)
	w.write(winners)

