import sys
sys.stdin = open ('4881_배열 최소 합.txt', 'r')


def construct_candidates(a, k, a_input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, a_input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1

    return ncandidates


def backtrack(a, k, a_input):
    c = [0] * len(a)

    if k == input:
        for i in range(1, k+1):
            print(arr[i], end=' ')
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, a_input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, a_input)