#!/usr/bin/env python


class Ballot:
	def __init__(self, num_candidates, candidate_list):
		self.ballot_list = []
		self.num_candidates = num_candidates
		self.candidate_list = candidate_list
		self.count = []

	def add(self, line):
		self.votes.append(line.split(" "))

	def counter(self):
		for i in range(len(self.ballot_list)):
			print(int(self.ballot_list[i[0]]))
			#count[int(self.votes[i][0]) += 1

		#print(count[0], count[1], count[2])



class Candidate:
	def __init__(self, name):
		self.name = name
		self.num_votes = 0

	def get_num_votes():
		pass

	def __next__(self):
		pass



def read(file):
	line = file.readline()
	file.readline()
	return line, file

def election(file):
	candidate_list = []
	num_candidates = int(file.readline())
	for i in range(num_candidates):
		 candidate_list.append(Candidate(file.readline()))

	ballot = Ballot(num_candidates, candidate_list)
	for votes in Ballot.ballot_list:
		
	while file != "":
		ballot.add(file.readline())

	ballot.counter()



#election()