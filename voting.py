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
			del x.votes[0]
	#wont we have to reassign the ballot to someone after modifying it ????		

class Ballot: 
	def __init__(self, prefs):
		self.index = 0
		self.votes = list(prefs)

	# def get_ballot(self):
	# 	return self.votes


def read(r):
	infile = open(r,'r')
	num_elections = int(infile.readline())
	infile.readline()
	while num_elections != 0:
		num_candidates = int(infile.readline())
		cand_list = []
		# print (num_candidates)
		for i in range (num_candidates):
			cand_list.append(Candidate(infile.readline().rstrip(), i+1 ))

		line = infile.readline()
		while line != '':
			tmp = Ballot(line.rstrip().split(' '))
			#print(tmp[0])
			ballot_list.append(tmp.votes)
			cand_list[int(tmp.votes[0])-1].cache_ballot(tmp.votes)
			line = infile.readline()
		# print (cand_list[1].view_ballot())
		# print (ballot_list)
		total_ballot = len(ballot_list)	
		winners = solve_election(cand_list, total_ballot)


		# for i in winners:
		# 	print (i.name)
		infile.readline()	
		num_elections -= 1

	return num_elections, cand_list, ballot_list, num_candidates, total_ballot	

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

	loser_ballot =[]
	for n in cand_list:
		for loser in loser_list:		
			if n.name == loser:
				loser_ballot.append(n.view_ballot())
				cand_list.remove(n)	

	loser_ballot = loser_ballot[0]
	for b in loser_ballot:
		del b[0]
		
	# print (loser_ballot)
	cand_id_list = []
	for cand in cand_list:
		cand_id_list.append(cand.number)
	for b in loser_ballot:
		while int(b[0]) not in cand_id_list:
			del b[0]
		for cand in cand_list:
			if int(b[0]) == cand.number:
				cand.cache_ballot(b) 
				loser_ballot.remove(b)
	# print ('test1')
	return cand_list			
	
def solve_election (cand_list, total_ballot): # added total ballot to check for majority 

#creating a vote list of votes collected by each candidate
	while True:
		vote_dict = {}
		vote_list = []
		for n in cand_list:
			vote_dict[n.name] = n.cand_votecount()
			vote_list.append(n.cand_votecount())

		Winner, hasWinner = test_winner(vote_dict, total_ballot)
		# print hasWinner
		if(hasWinner == True):
			print ('winner')
			# print (Winner)
			return [Winner]

		if(test_tie(vote_list)):
			print ('tie')
			return cand_list


		cand_list = loser(vote_list, vote_dict, cand_list)
		



def main():
	num_elections, cand_list, ballot_list, num_candidates, total_ballot = read('read.txt')


main()	
