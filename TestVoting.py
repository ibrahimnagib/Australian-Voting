#  TestVoting.py

from io       import StringIO
from unittest import main, TestCase

from Voting import read, test_winner, test_tie, loser, solve_election


# -----------
# TestVoting
# -----------

class TestVoting(TestCase) :
    
    # ----
    # read
    # ----

    def test_read_1(self):
    	a = read()
    	self.assertEqual()

    def test_read_2(self):
    	a = read()
    	self.assertEqual()

    def test_read_3(self):
    	a = read()
    	self.assertEqual()

    # ----
    # test_winner
    # ----

    def test_test_winner_1(self):
        c = test_winner()
        self.assertEqual()

    def test_test_winner_2(self):
        c = test_winner()
        self.assertEqual()

    def test_test_winner_3(self):
        c = test_winner()
        self.assertEqual()


    # ----
    # test_tie
    # ----

    def test_test_tie_1(self):
    	b = test_tie()
    	self.assertEqual()

    def test_test_tie_2(self):
    	b = test_tie()
    	self.assertEqual()

    def test_test_tie_3(self):
    	b = test_tie()
    	self.assertEqual()


    # ----
    # loser
    # ----

    def test_loser_1(self):
    	d = loser()
    	self.assertEqual()

    def test_loser_2(self):
    	d = loser()
    	self.assertEqual()

    def test_loser_3(self):
    	d = loser()
    	self.assertEqual()

    # ----
    # solve_election
    # ----

    def test_solve_election_1(self):
    	e = solve_election()
    	self.assertEqual()

    def test_solve_election_2(self):
    	e = solve_election()
    	self.assertEqual()

    def test_solve_election_3(self):
    	e = solve_election()
    	self.assertEqual()













