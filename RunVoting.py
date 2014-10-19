# RunVoting.py

import sys
from voting import election, read

def main():
	num_elections, file = read(sys.stdin)
	while num_elections > 0:
		election(file)
		num_elections -= 1

main()