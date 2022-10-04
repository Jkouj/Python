#lab 9-1
#Joey Koumjian
#Due 4/15

def matchPtc(seq1, seq2):
    pct = 0
#    seq1 = str(seq1)
#    seq2 = str(seq2)
    if len(seq1) > len(seq2):
        n = seq1
        m = seq2
    else:
        n = seq2
        m = seq1
    for i in range(len(m)):
        if m[i] == n[i]:
            pct = pct + 1
    pct = pct / len(m)
    return pct
