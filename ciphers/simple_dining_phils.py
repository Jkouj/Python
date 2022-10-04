# Dining Philosophers - Simple example with two philosophers and two chopsticks

from multiprocessing import Process, Lock
import random
import time


def think(tTime):
    time.sleep(tTime)

def eat(eTime):
    time.sleep(eTime)


def diningPhil(phil,ch1,ch2):
    # Start the philosopher
    print(phil, " is starting")                          
    # Get random time for Thinking 
    thinkTime = random.randint(0,5)                      
    # Get random time for eating
    eatTime = random.randint(1,5)                        
    print(phil, " is thinking ", thinkTime, " seconds")
    # Think for random amount of time
    think(thinkTime)                                     
    print(phil, " is asking for chopstick")
    # Ask for first chopstick
    ch1.acquire()                                        
    print(phil, " got chopstick")
    print(phil, " is asking for chopstick")   
    # Pause before picking up second chopstick
    think(1)                                       
    # Ask for second chopstick
    ch2.acquire()                                        
    print(phil, " got chopstick")
    print(phil, " is eating ", eatTime, " seconds")
    # Once the philosopher has both chopsticks, eat
    eat(eatTime)                                         
    print(phil, " is releasing chopsticks")
    # When finished eating, release both chopsticks
    ch1.release()                                        
    ch2.release()
    print(phil," is finished")
    
# Main Program

if __name__=='__main__':
    # Create a lock that we call chopstick1
    chopstick1 = Lock()                                  
    # Create another lock that we call chopstick2
    chopstick2 = Lock()
    
    phil1 = "Aristotle"
    phil2 = "Plato"
    # Create process for philosopher Aristotle asking for chopstick1 and then chopstick2
    proc1 = Process(target = diningPhil, args=(phil1,chopstick1,chopstick2))  
    
    # Create process for philosopher Plato asking for chopstick2 and then chopstick1
    proc2 = Process(target = diningPhil, args=(phil2,chopstick2,chopstick1)) 
    
    # Start process 1
    proc1.start()                                         
    # Start process 2
    proc2.start()                                         
    # Join all processes together to end the program
    
    proc1.join()                                          
    proc2.join()
    print("end of program")






