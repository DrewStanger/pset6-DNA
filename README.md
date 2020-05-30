This is a python application which identifies a person based on their DNA.
https://cs50.harvard.edu/x/2020/psets/6/dna/

This was produced as a part of CS50 - Introduction to Computer Science. Uploading of my solution to Github is considered to be reasonable regarding the academic honesty policy. (https://www.reddit.com/r/cs50/comments/63235w/is_this_reasonable/)

How it works

- There are two main datasets compated within in this program, firstly databases and the DNA sequences, the databases which lists of peoples names compared with the number of sequential nucleotides which occur within a sequence of their DNA. 

- dna.py is used to compare the sequences against the databases.

- To do this dna.py iterates through the DNA sequences and counts how many occurances of each DNA nucleotide occur.

- the values are saved to an array and are then compared to the databases, if all of the values match a person, it can be concluded that the DNA sequence belongs to them. 
