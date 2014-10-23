class Candidate:
    """
    Candidate class for creating candidate objects, 
    makes it easier to accesss to attributes such as 
    name and number, also holds candidate ballots and 
    modifies and re-assigns ballots
    """

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
    """
    Ballot class for creating ballot objects 
    that can hold lists of ballots as well as 
    index through those lists
    
    """
	def __init__(self, prefs):
		self.index = 0
		self.votes = list(prefs)

def read_data(infile, w):
    """
    infile is the sys.stdin 
    w is a writer
    reads through the elections, returning
    the number of elections, number of candidates
    as well as reading all of the candidate names
    and ballots and creating objects
    
    """
	#infile = open(r,'r')
	num_elections = int(infile.readline())
    	#assert type(num_elections) == int
	infile.readline()
	win_list = []
	c = 0
	while num_elections != 0:
		num_candidates = int(infile.readline())
        	#assert type(num_candidates) == int
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
		if c == 1:
			w.write('\n')
		w.write(winners + '\n')
		c +=1
		num_elections -= 1

	return num_elections, cand_list, ballot_list, num_candidates, total_ballot

def test_winner(vote_dict, total_ballot):
    """
    Looks for winners in the dictionary
    and returns their ballots
    
    """
	haswinner = False
	winner = ''
	for k,v in vote_dict.items():
		if float(float(v)/float(total_ballot)) > float(0.5):
			haswinner = True
			winner = k
	return winner, haswinner

def test_tie(vote_list):
    """
    Determines if all candidates 
    have the same number of votes
    """
	hastie = True
	for x in range(1,len(vote_list)):
		if vote_list[0] != vote_list[x]:
			hastie = False
			break
	return hastie

def loser(vote_list, vote_dict, cand_list):
    """
    Determines the candidate with the least amount 
    of votes, eliminates that candidate, and re-assigns
    their ballot to its next choice candidate
    
    """

	loser_list = []
	loser_vote = min(vote_list)
    	#assert type(loser_vote) == int
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

def solve_election (cand_list, total_ballot):
    """
    Takes in a list of candidate objects as well as 
    total ballots, and constantly checks if a candidate
    has majority, or if there is a tie
    
    """

	while True:
		vote_dict = {}
		vote_list = []
		for n in cand_list:
			vote_dict[n.name] = n.cand_votecount()
			vote_list.append(n.cand_votecount())

		Winner, hasWinner = test_winner(vote_dict, total_ballot)

		if(hasWinner):
			return Winner

		if(test_tie(vote_list)):
			x = ''
			for cand in cand_list:
				x += str(cand.name) + '\n'
			return x

		cand_list = loser(vote_list, vote_dict, cand_list)

def run_voting(r, w):
    """
    r a reader
    w a writer
    
    """
	num_elections, cand_list, ballot_list, num_candidates, total_ballot = read_data(r, w)
