#  TestVoting.py

from io       import StringIO
from unittest import main, TestCase

from Voting import read, test_winner, test_tie, loser, solve_election, Candidate, Ballot


# -----------
# TestVoting
# -----------

class TestVoting(TestCase) :
    
    # ----
    # Candidate
    # ----

    def test_Candidate_1(self):
    	c = Candidate("Messi",5)
    	self.assertEqual(c.name, "Messi")
    	self.assertEqual(c.number, 5)

    def test_Candidate_2(self):
    	c = Candidate("Luca",2)
    	self.assertEqual(c.name, "Luca")
    	self.assertEqual(c.number, 2)

    def test_Candidate_3(self):
    	c = Candidate("Ribery",1)
    	self.assertEqual(c.name, "Ribery")
    	self.assertEqual(c.number, 1)

    def test_Candidate_4(self):
    	c = Candidate("Messi",2)
    	self.assertEqual(c.count, 0)
    	self.assertEqual(c.cand_ballot, [])

    def test_Candidate_5(self):
    	c = Candidate("Lucas",4)
    	self.assertEqual(c.count, 0)
    	self.assertEqual(c.cand_ballot, [])

	def test_Candidate_6(self):
    	c = Candidate("Modric",15)
    	self.assertEqual(c.name, "Modric")
    	self.assertEqual(c.number, 15)

    def test_Candidate_7(self):
    	c = Candidate("Figo",11)
    	self.assertEqual(c.name, "Figo")
    	self.assertEqual(c.number, 11)

    def test_Candidate_8(self):
    	c = Candidate("Zidanne",1)
    	self.assertEqual(c.name, "Zidanne")
    	self.assertEqual(c.number, 1)

    def test_Candidate_9(self):
    	c = Candidate("Bale", 12)
    	self.assertEqual(c.name, "Bale")
    	self.assertEqual(c.count, 0)
    	self.assertEqual(c.number, 12)
    	self.assertEqual(c.cand_ballot, [])

    def test_Candidate_10(self):
    	c = Candidate("Lavezzi", 14)
    	self.assertEqual(c.count, 0)
    	self.assertEqual(c.name, "Lavezzi")
    	self.assertEqual(c.number, 14)
    	self.assertEqual(c.cand_ballot, [])

    # ----
    # test_winner
    # ----

    def test_test_winner_1(self):
        w,h = test_winner({"John":2,"Mark":1},2)
        self.assertEqual(w, "John")
        self.assertEqual(h, True)

    def test_test_winner_2(self):
        w,h = test_winner({"Jane":3,"Mark":4, "Sirhan":1},11)
        self.assertEqual(w,'')
        self.assertEqual(h, False)

    def test_test_winner_3(self):
        w,h = test_winner({"Jane":2,"Mark":1, "Sirhan":3},2)
        self.assertEqual(w, "Sirhan")
        self.assertEqual(h, True)

    def test_test_winner_4(self):
        w,h = test_winner({"Jane":1,"Mark":2, "Sirhan":2},4)
        self.assertEqual(w,'')
        self.assertEqual(h, False)

    def test_test_winner_5(self):
        w,h = test_winner({"Adam":3,"James":1, "Ronaldo":7},3)
        self.assertEqual(w, "Ronaldo")
        self.assertEqual(h, True)

    def test_test_winner_6(self):
        w,h = test_winner({"Lorenzo":3,"Mark":1},2)
        self.assertEqual(w, "Lorenzo")
        self.assertEqual(h, True)

    def test_test_winner_7(self):
        w,h = test_winner({"Marco":3,"Ruth":4, "Lorie":1},11)
        self.assertEqual(w,'')
        self.assertEqual(h, False)

    def test_test_winner_8(self):
        w,h = test_winner({"Anne":2,"Jake":1, "Alice":7},2)
        self.assertEqual(w, "Alice")
        self.assertEqual(h, True)

    def test_test_winner_9(self):
        w,h = test_winner({"Martha":1,"Marry":1, "Joshua":1},3)
        self.assertEqual(w,'')
        self.assertEqual(h, False)

    def test_test_winner_10(self):
        w,h = test_winner({"Morgan":2,"Avery":3, "Casillas":19},7)
        self.assertEqual(w, "Casillas")
        self.assertEqual(h, True)

    # ----
    # test_tie
    # ----

    def test_test_tie_1(self):
    	b = test_tie([1,2,3])
    	self.assertEqual(b, False)

    def test_test_tie_2(self):
    	b = test_tie([2,2,2,2,2])
    	self.assertEqual(b, True)

    def test_test_tie_3(self):
    	b = test_tie([2,3,1,4,5,6])
    	self.assertEqual(b, False)

    def test_test_tie_4(self):
    	b = test_tie([1])
    	self.assertEqual(b, True)

    def test_test_tie_5(self):
    	b = test_tie([1,5,8,3,2])
    	self.assertEqual(b, False)

    def test_test_tie_6(self):
    	b = test_tie([7,7,7])
    	self.assertEqual(b, True)

    def test_test_tie_7(self):
    	b = test_tie([1,2])
    	self.assertEqual(b, False)

        def test_test_tie_8(self):
    	b = test_tie([6,6,6,6)
    	self.assertEqual(b, True)

    def test_test_tie_9(self):
    	b = test_tie([1,1,1,1,1,1,1])
    	self.assertEqual(b, True)

    def test_test_tie_10(self):
    	b = test_tie([1,3,7,4,5,8,9,2,1])
    	self.assertEqual(b, False)

    def test_test_tie_11(self):
    	b = test_tie([8,8,8,8])
    	self.assertEqual(b, True)

    def test_test_tie_12(self):
    	b = test_tie([2,3,42,21])
    	self.assertEqual(b, False)

    # ----
    # Ballot
    # ----

    def test_Ballot_1(self):
    	ballot = Ballot("312")
    	self.assertEqual(ballot, ['3', '1', '2'])

    def test_Ballot_2(self):
    	ballot = Ballot("12345")
    	self.assertEqual(ballot, ['1', '2', '3', '4', '5'])

    def test_Ballot_3(self):
    	ballot = Ballot("54321")
    	self.assertEqual(ballot, ['5', '4', '3', '2', '1'])

    def test_Ballot_4(self):
    	ballot = Ballot("713")
    	self.assertEqual(ballot, ['7', '1', '3'])

    def test_Ballot_5(self):
    	ballot = Ballot("2818")
    	self.assertEqual(ballot, ['2', '8', '1', '8'])

    def test_Ballot_6(self):
    	ballot = Ballot("456")
    	self.assertEqual(ballot, ['4', '5', '6'])

    def test_Ballot_7(self):
    	ballot = Ballot("32849")
    	self.assertEqual(ballot, ['3', '2', '8', '4', '9'])

    def test_Ballot_8(self):
    	ballot = Ballot("1")
    	self.assertEqual(ballot, ['1'])

    def test_Ballot_9(self):
    	ballot = Ballot("98765432")
    	self.assertEqual(ballot, ['9', '8', '7', '6', '5', '4', '3', '2'])

    def test_Ballot_10(self):
    	ballot = Ballot("246")
    	self.assertEqual(ballot, ['2', '4', '6'])










