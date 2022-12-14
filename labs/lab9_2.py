# Program to compute and print a dot plot of two nucleotide sequences

# Function to find how many matches there are in two strings of equal length
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

# Function to initialize a dot plot of a certain size
def initDotPlot(rows, cols):
    # Initialize the dot_plot matrix
    empty_dot_plot = []
    # For each row in the matrix
    for i in range(rows):
        # Initialize the row
        row = []
        # For each col in the matrix
        for j in range(cols):
            # Insert a blank in the row
            row.append("-")
        empty_dot_plot.append(row)
    return empty_dot_plot          
            
# Function to compute the dot plot of two sequences using a sliding window of size winsize
def computeDotPlot(str1, str2, winsize, threshold, dot_plot):
    # Loop through all of the rows (characters in the side sequence)
    for i in range(len(str2)):
        # Loop through all of the columns (characters in the top sequence)
        for j in range(len(str1)):
            try:
                if matchPct(str1,str2) > threshold and str1[i] == str2[j]:
                    dot_plot[i][j] = "*"
            except IndexError:
                    u = 'cute'
            # Fill in the code to determine if we should insert
            # a "*" to the position in the dot plot

    return dot_plot


# Function to print the dot plot of two sequences
def printDotPlot(str1, str2, dot_plot):
    row = ""
    for ch in str1:
        row = row + " " + ch + " "
    print(" ", row)
    row = ""
    for i in range(len(dot_plot)):
        row = row + str2[i] + " "
        for j in range(len(dot_plot[i])):
            row = row + " " + dot_plot[i][j] + " "
        print(row)
        row = ""

# Main function
def main():
    str1 = input("Enter top string: ")
    str2 = input("Enter side string: ")
    winsize = int(input("Enter size of window: "))
    threshold = float(input("Enter expected threshold: "))
    empty_dot_plot = initDotPlot(len(str2), len(str1))
    dot_plot = computeDotPlot(str1,str2, winsize, threshold, empty_dot_plot)
    printDotPlot(str1, str2, dot_plot)

    
