illumio-coding-challenge
========================
Please solve these coding exercises using any language (preferably Ruby or Python, but, any other language is OK too). We can discuss your design and solution when you come for the interview. Please make sure the program compiles and solves the problem stated. 

We will be looking for:
  
    a. The data structures  
    b. The algorithm  
    c. Coding style and good software development practices.   

#Question 1:

You have a deck containing X number of cards. While holding the deck, do the following:

    a. Take the top card off the deck and set it on the table  
    b. Take the next card off the top of desk and put it on the bottom of the deck in your hand.  
    c. Continue doing (a) and (b) until all the cards are on the table.  

>**This is a round.** 

Pick up the deck and repeat steps (a), (b), ( c ) until the deck is in the original order. 

Write a program to determine how many rounds it will take to put the deck back in original order. Please make sure the program can take a command line argument for number of cards in deck. We will test the solution with different sizes of decks e.g. 100, 200, 300, 313. 

#Question 2:

You are given a few Lego Mindstorm-like robots and asked to navigate a rectangular plateau, so that the on-board cameras will get a complete view of the terrain. The robots are expensive and should not get damaged in any way. 

The robot's position and location is a combination of (X,Y) coordinates and a letter representing four cardinal compass points.   
The field is divided into a grid. For example, the bottom left of the field is (0,0,N) with the robot pointing North. The square directly North of the current point of (X,Y) is (X, Y+1).   

Commands you can send the robot:  
L, R - spin 90 degrees left or right  
M - move forward one point and maintain the same heading  

You will be given input in text format. The first line is always two numbers indicating the top right coordinates (presume bottom left is (0,0)).  Then a series of two lines of commands for each robot. Presume that the robots move sequentially.   
The first line is the current coordinates and heading in the format "1 2 N" for a robot at point (1,2) heading North  
The second line is a series of character indicating the pattern of movement e.g. "LMLMLMMM".  

The expected output is the final coordinates of each robot and its heading.  

Test Input:

    5 5  
    1 2 N  
    LMLMLMLMM  
    3 3 E  
    MMRMMRMRRM  

Expected output:  

    1 3 N  
    5 1 E  


##Further questions:

    a. Make the robots move simultaneously. Avoid collisions. 

    b. Write the program so that each robot is a remote client. Your server program parses and sends data to each remote client and collects the responses back. 

    c. Presume that each robot has two on-board front cameras pointing 45degrees outwards from the heading of the robot. The cameras each photograph a grid point in front of them, every time the robot moves forward. Two photos are taken for each step moved by the robot. For each test input, the output should indicate the percentage of the field that has been photographed. Duplicate photos are OK. 

 
#Question 3:

You are given a 2G syslog file with each line in the format:

    Month Day hh:mm:ss hostname service[PID]: (userid) command a b c d e f ...

Where Day, PID is an integer and rest of the fields are alpha-numeric strings.

For each service and user, the command string may occur multiple times in the syslog file. We need to find the number of occurrences of a command for each (service, user, command) combination. 

Write a tool that will prepare a table with each line containing:
  
    service userid command number-of-times-the-command-occurs-in-syslog

For example, for input:  
<code>
    Dec 10 07:17:01 ip-10-198-43-75 CRON[19220]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)  
    Dec 10 08:17:01 ip-10-198-43-75 CRON[30306]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)  
    Dec 10 09:17:01 ip-10-198-43-75 CRON[9098]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)  
    Dec 10 10:17:01 ip-10-198-43-75 CRON[20128]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)  
    Dec 10 11:17:01 ip-10-198-43-75 CRON[31240]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)  
    Dec 10 12:17:01 ip-10-198-43-75 CRON[9881]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)  
    Dec 10 13:17:01 ip-10-198-43-75 CRON[20902]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)  
    Dec 10 14:17:01 ip-10-198-43-75 CRON[31972]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)  
</code>

The output would be:
    CRON  root  CMD 8
