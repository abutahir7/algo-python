def calculateLPS(lps, pat, M):
	ln = 0
	i = 1
	lps[0] = 0

	while i < M:
		if pat[i] == pat[ln]:
			lps[i] = ln + 1
			ln +=1
			i +=1
		else:
			if ln != 0:
				ln = lps[ln -1]
			else:
				lps[i] = 0
				i += 1
	print(lps)



def kmp(txt, pat, check_present_only=False, print_match=False, all_occ=False, print_index=False):
	N = len(txt)
	M = len(pat)
	if N == 0 or M == 0:
		return None
	lps = [0] * M
	calculateLPS(lps, pat, M)
	i = 0
	j = 0

	while i < N:

		if txt[i] == pat[j]:
			# case where the char match
			i += 1
			j += 1
		else:
			if j !=0 :
				j = lps[j -1]
			else:
				i +=1

		if j == M:

			if check_present_only:
				return 1
			elif print_index:
				print(i-j, i)

			if print_match:
				print(txt[i-j : i])

			# if you don't want to find all the occurance break here.
			if all_occ:
				j = lps[j -1 ]
			else:
				break
		
	return -1
t ="sadasda"
p = "sda"

print(kmp(t, p, check_present_only= False, print_index=True))