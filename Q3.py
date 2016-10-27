
# IsValid(S, D, i) returns True if the first i characters of S (i.e. S[0:i+1])
# is a corrupted text of valid words.


def IsValid(S, D, i):

	if S[0:i+1] in D: # if S[0:i+1] is a valid word, then obviously the output is True
		return True

# The rest of the code goes here.
# Hints:
# 1. If S[0:i+1] is a corrupted text of valid words, then S[0:i+1] = uv,
# where u is a corrupted text of valid words and v is in D.
# 2. Consider all possibilities.

	for j in range(i,-1,-1):
		if S[j:i+1] in D and IsValid(S,D,j-1):
			return True

	return False


D = {
	'it':True,
	'was':True,
	'the':True,
	'best':True,
	'of':True,
	'time':True,
	'times':True,
}

S = 'itwasthebestoftimes'

ans = IsValid(S,D,len(S)-1)
print(ans)