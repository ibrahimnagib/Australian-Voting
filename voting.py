#!/usr/bin/env python


def read (infile):
	line = infile.readline()
	infile.readline()

	num_elections = int(line)

	return num_elections


class Candidate:
	def __init__ (self, name):
		self.name = name
		self.ballots = []
	
	def __str__ (self):
		return self.name
	
	def add (self, ballot):
		self.ballots.append(ballot)
	
	def get_ballots (self):
		return self.ballots
	
	def num_votes (self):
		num_votes = len(self.ballots)
		return num_votes
	
	def remove (self):
		self.ballots = []

class Ballot:
	def __init__ (self, line):
		self.index = 0
		self.votes = []

		for vote in line.split(" "):
			vote = int(vote)
			self.votes.append(vote)
	
	def __str__ (self):
		return str(self.votes)
	
	def get_vote (self):
		index = self.index
		self.index += 1
		return self.votes[index]


def election(file):
	candidate_list = []
	ballot_list = []
	num_candidates = int(file.readline())
	for i in range(num_candidates):
		 candidate_list.append(Candidate(file.readline()))


	ballot = Ballot(num_candidates, candidate_list)
	for vote in ballot:
		pass
		
	for votes in Ballot.ballot_list:
		
	while file != "":
		ballot.add(file.readline())

	ballot.counter()



#election()