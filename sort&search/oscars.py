# Given:  A file containing Academy Awards
# Find:  The awards given in a particular year and write out to an external file

# Function to get data and store it 3 separate lists
# Parameters: None
# Return: 3 lists: year of award, award name, winner
def getLists():
  infile = open('awards.txt','r')
  yearList = []
  awardList = []
  winnerList = []
  line = infile.readline()
  line = line.strip()
  while line != '':
    year, award, winner = line.split(',')
    yearList.append(year)
    awardList.append(award)
    winnerList.append(winner)
    line = infile.readline()
    line = line.strip()
  infile.close()
  return yearList, awardList, winnerList

# Finds all winners in the given year and returns a list of those winners
# Parameters: yearList, winnerList, year to search for
# Return: List of winners in the given year
def getWinners(year, yearList, winnerList):
  yearWinners = []
  for i in range(len(yearList)):
      if year == yearList[i]:
          yearWinners.append(winnerList[i])
  return yearWinners

# Prints the winners from the given year to an external file
# Parameters: year searched for, list of winners in that year
# Return: None
def outputWinners(year, yearWinners):
    outfname = input("Enter name of output file: ")
    outfile = open(outfname,'w')
    outfile.write("The winners in the year " + year + " were: \n")
    for i in range(len(yearWinners)):
        outfile.write(yearWinners[i] + '\n')
    outfile.close()
    return

# Main function
def main():
  yearList, awardList, winnerList = getLists()
  year = input('Enter the year: ')
  yearWinners = getWinners(year, yearList, winnerList)
  outputWinners(year,yearWinners)

