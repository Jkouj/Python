#lab 9-1
#Joey Koumjian
#Due 4/15

def matchPct(seq1, seq2):
    pct = 0
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
    pct = round(pct,2)
    return pct
