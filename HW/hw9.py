#Joey Koumjian
#Due 4/18
#HW 9

# Program to find all possible alignments of a pair of strings when adding
# gaps to the shorter string

# Given:  Two strings of nucleotides
# Find:  All possible alignments when adding gaps to the shorter string


# Function to create a list of all ways one gap can be inserted into
# a string.  The input is a string, the output is a list of strings
# with a gap inserted into all positions of the input string

def insertOneGap(strng):
    alignments = []
    for i in range(len(strng)):
        newStrng = strng[0:i] + '-' + strng[i:len(strng)]
        alignments = alignments + [newStrng]
    alignments = alignments + [strng + '-']
    return alignments
            
# Function to take a set union of a pair of lists
# This is used to eliminate any duplicates in the list when they are combined
def Union(list1, list2):
    for a in list2:
        if a not in list1:
            list1 = list1 + [a]
    return list1


# Function to create all possible alignments of a string with a certain number
# of gaps inserted
def insertAllGaps(strng, gaps):
    # List of alignments starts with the initial string
    alignments = [strng]

    # Loop to insert one gap at a time
    for i in range(gaps):

        # Initialize list of new alignments with i gaps in the string
        newAlignments = []

        # For every string in the list of alignments
        for st in alignments:
            # Insert one gap in each alignment in the list
            al = insertOneGap(st)

            # Add the new alignment to the list of new alignments being created
            newAlignments = Union(newAlignments,al)

        # The alignments list now becomes the new alignments list to now
        # add another gap to each of the alignments in the new list
        alignments = newAlignments
    return alignments


# Function to compute the score for a pair of alignments
# Gap score = 0, Match score = 1, Mismatch score = -1
def scoreAlignment(seq1, seq2):
    totalScore = 0
    # Fill in the code to compute the score for a pair of sequences
    # using the scoring in the comment above
    for i in range(len(seq1)):
        if seq1[i] == '-' or seq2[i] == '-':
            totalScore = totalScore
        elif seq1[i] == seq2[i]:
            totalScore += 1
        else:
            totalScore -= 1
            
    return totalScore

# Function to compute all alignments with gaps in both sequences
def scoreGapsInBoth(longSeq, shortSeq, longGaps):
    totalAlignments = 0
    high = 0
    highScore = 0
    otherList = []
    highList = []
    a = []
    b = []
    difference = len(longSeq) - len(shortSeq)
    # Fill in the code to compute the total number of alignments when we
    # allow longGaps number of gaps in the long sequence. longGaps is the n
    # and the optimal score with a list of all alignments with that score
    a = insertAllGaps(longSeq, longGaps)
    c = (longGaps + len(longSeq)) - len(shortSeq)
    b = insertAllGaps(shortSeq, c)
    for i in range(len(a)):
        for j in range(len(b)):
            score = scoreAlignment(a[i],b[j])
            if score > highScore:
                highScore = score


    for i in range(len(a)):
        j = 0
        while j < len(b):
            otherList.append(b[j] + '\n' + a[i])
            score = scoreAlignment(a[i],b[j])
            if score == highScore and score >= 2:
                highList.append(a[i] + '\n' + b[j])
            j = j + 1
                
    totalAlignments = len(a)*len(b)

    return totalAlignments, highScore, highList

        
# Function to print all of the alignments along with the score for
# each alignment
def printResults(totalAlignments, highScore, highList):
        print("There are ", totalAlignments, " alignments.")
        print("There are ", len(highList)," optimal alignments with a score of ", highScore, ":")
        for i in range(len(highList)):
            print(highList[i])
            print()
        return

        
# Main function
def main():
    # Get the two strings to align
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    longGaps = int(input("How many total gaps should we allow in the longer sequence? "))

    # Compute alignments adding gaps to the shorter string
    if len(str1) > len(str2):
        longSeq = str1
        shortSeq = str2
    else:
        longSeq = str2
        shortSeq = str1

    totalAlignments, highScore, highList = scoreGapsInBoth(longSeq, shortSeq, longGaps)
    printResults(totalAlignments, highScore, highList)

     
 
    
