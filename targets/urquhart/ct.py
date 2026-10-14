"""Thomas Urquhart's two encrypted poems, as printed.

Source: Klaus Schmeh, "The Top 50 unsolved encrypted messages: 28. Thomas Urquhart's encrypted poems",
Cipherbrain, 30 June 2017, which takes them from John Wilcock, "Sir Thomas Urquhart of Cromartie,
Knight" (1899).

The distich is 64 numbers in two lines of 32, values 1 to 70. The octastich is eight lines, values
up to 201. Both ranges have the shape of an index into a text rather than of a substitution
alphabet, which is why a book cipher on Urquhart's own printed works is the natural hypothesis.
"""

DISTICH = [
 5,3,27,38,32,14,21,8,66,8,70,39,5,9,12,18,2,3,56,5,1,7,3,2,13,19,3,25,9,3,16,6,
 25,15,13,6,11,20,5,1,2,12,1,20,20,49,20,20,35,33,4,6,8,35,5,38,5,5,18,10,3,11,32,42,
]
# Position 56 is 38 in the 1653 print (NLS H.32.a.39, photographed by David Scheers) and in the
# 1834 Works; Schmeh has 33. Corrected 14 Oct 2026 (sum 1078).

OCTASTICH = [
 [25,11,39,4,4,10,3,54,50,19,1,18,1,5,9,58,15,1,4,17,1,42,32,77,23,75,6,3,18,20,36,8,21],
 [4,10,22,3,5,11,3,162,18,21,44,79,42,2,17,61,32,7,7,107,8,59,28,54,31,113,42],
 [1,6,96,31,87,5,88,1,4,30,10,15,8,47,28,17,139,17,69,5,29,9,9,1,51,6,114,8,34,30,2,18,24,41,33,74,93,8],
 [5,12,58,162,12,44,1,66,9,15,100,42,2,28,16,6,27,4,196,70,53,7,1,69,2,15,89,34,11,13,12,29,15,76,40,22,8,24,75],
 [3,58,15,2,1,4,5,56,5,5,2,4,12,20,19,14,80,37,45,34,3,95,6,38,1,18,11,27,4,13,7,24],
 [5,20,5,87,40,25,9,56,21,29,2,81,50,147,2,6,16,15,14,9,13,27,3,16,14,7,6,10],
 [38,3,3,2,10,34,8,18,9,28,2,4,6,2,201,10,13,6,1,36,1,31,4,17,54,16,5,22,11,5,31],
 [71,96,15,45,19,6,64,10,42,7,83,37,6,3,7,74,4,14,8,91,27,12,11,2,28,50,68,3,2,12,1,5,49,3],
 [7,7,95,66,1,11,33,51,50,6],
]

# The August 2026 claim, for testing. Vals AI reported that the distich is a book cipher on
# Urquhart's Proquiritations, the i-th number indexing a word in the i-th Proquiritation, first
# letters taken. A rebuttal of 1 September 2026 says the rule fails at 10 of 64 positions.
CLAIM = 'OGODUPHOLDKINGCHARLSTHESECONDANDMAKEHIMTHESUPREMERULEROFTHISLAND'

# Transcribed 16 Sept 2026 from the HCPortal scans of the 1983 Jack & Lyall edition, p. 212 and the facing page
# (src/octastich_part1.jpg, src/octastich_part2.jpg): eight stanza-lines each with a run-over, then the Decagram.
# 285 numbers. Schmeh's transcription above lacks the run-over of lines 2 and 6, one "2" in line 6, and has 6 for 16
# in line 3.
OCTASTICH_1983 = [
 [25,11,39,4,4,10,3,54,50,19,1,18,1,5,9,58,15,1,4,17,1,42,32,77,23,75,6, 3,18,20,36,8,21],
 [4,10,22,3,5,11,3,162,18,21,44,79,42,2,17,61,32,7,7,107,8,59,28,54,31,113,42, 31,5,19,32,3,115,3,22],
 [1,16,96,31,87,5,88,1,4,30,10,15,8,47,28,17,139,17,69,5,29,9,9,1,51,6,114,8, 34,30,2,18,24,41,33,74,93,8],
 [5,12,58,162,12,44,1,66,9,15,100,42,2,28,16,6,27,4,196,70,53,7,1,69,2,15,89, 34,11,13,12,29,15,76,40,22,8,24,75],
 [3,58,15,2,1,4,5,56,5,5,2,4,12,20,19,14,80,37,45,34,3,95,6,38,1,18,11,27,4,13, 7,24],
 [5,20,5,87,40,25,9,56,21,29,2,81,50,147,2,6,16,15,14,9,13,27,3,16,14,7,6,2,10, 16,69,1,44],
 [38,3,3,2,10,34,8,18,9,28,2,4,6,2,201,10,13,6,1,36,1,31,4,17,54,16,5,22,11,5, 31],
 [71,96,15,45,19,6,64,10,42,7,83,37,6,3,7,74,4,14,8,91,27,12,11,2,28,50,68,3,2, 12,1,5,49,3],
 [7,7,95,66,1,11,33,51,50,6],
]
