#Lab 5
#Joey Koumjian and Rafael Mendez
#3/4/22

# World Series Results

# Given a file with the World Series Champions since 1904
# Allow user to ask various questions about the results

def openFile():
    goodFile = False;
    while goodFile == False:
        fname = input("Enter name of data file: ")
        try:
            inFile = open(fname, 'r')
            goodFile = True
        except IOError:
            print("Invalid filename, please try again...")
    return inFile

def getChamps():
    inFile = openFile()
    years = []
    winners = []
    losers = []
    line = inFile.readline()
    line = line.strip()
    while line != '':
        year, winner, loser = line.split(',')
        years.append(year)
        winners.append(winner)
        losers.append(loser)
        line = inFile.readline()
        line = line.strip()
    return years, winners, losers

def findWinnerAndLoser(year, years, winners, losers):
    winner =""
    loser =""
    i = 0
    found = False
    while i < len(years):
        if year == years[i]:
            found = True
            winner = str(winners[i])
            loser = str(losers[i])
        i += 1
            
    return winner, loser
            

def countWins(team, winners):
    numWins = 0
    i = 0
    while i < len(winners):
        if team == winners[i]:
            numWins += 1
        i = i + 1
    return numWins


def teamWinnerFile(team, years, winners, losers):
    i = 0
    if team not in winners:
        print(team,"never won the World Series. No file created. ")
        return
    outfname = team.replace(" ","")
    outfile = open(outfname + ".txt",'w')
    while i < len(losers):
        if winners[i] == team:
            a = years[i] + "," + losers[i]
            outfile.write(a + '\n')
        i += 1
    print("File written successfully: "+ outfname+".txt")
    outfile.close()
    return 
        
def getChoice():
    # This function displays the menu of choices for the user
    # It reads in the user's choice and returns it as an integer
    print("")
    print("Make a selection from the following choices:")
    print("1 - Find the World Series Winner and Loser for a particular year")
    print("2 - Count how many times a team has won the World Series")
    print("3 - Write to an output file all teams that have won the World Series")
    print("4 - Find the team that has won the most World Series Championships")
    print("5 - Find the team that has lost the most World Series Championships")
    print("6 - Quit")
    choice = int(input("Enter your choice --> "))
    print("")
    return choice


def main():    
    # Call the function to get the data from the data file and store the results in three lists
    years, winners, losers = getChamps()
    choice = getChoice()
    while choice != 6:
        if choice == 1:
            year = input("Enter the year to search for: ")
            winner, loser = findWinnerAndLoser(year,years, winners, losers)
            if winner == "":
                print("Invalid year")
            else:
                print("The ", winner, "defeated the ",loser, "in ", year)
            
            choice = getChoice()
        elif choice == 2:
            team = input("Enter the team name: ")
            # Call the function to get the number of wins for the team
            numWins = countWins(team, winners)
            print("The ", team, "won the World Series", numWins, "times")
            choice = getChoice()
        elif choice == 3:
            team = input("Enter the team name: ")
            # Call the function to create output file containing teams defeated by chosen team
            teamWinnerFile(team, years, winners, losers)
            choice = getChoice()
        elif choice == 4:
            # Call the function to find the team that won the most championships
            print("XXX won the World Series the most at XXX times.")
            choice = getChoice()
        elif choice == 5:
            # Call the function to find the team that lost the most championships
            print("XXX lost the World Series the most at XXX times.")
            choice = getChoice()
        else:
            print("Error in your choice")
            choice = getChoice()
    print("Good-bye")
    
    
