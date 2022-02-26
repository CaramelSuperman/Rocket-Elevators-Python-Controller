# Description


this program creates an column of elevators that can move to the desire floor
 by chosing the most apropriate elevator for each situation
the user just need to push the call button and an elevator will 
come to the user and then transport him to the desire floor.

# Dependencies 

To be able to try the program, you need ..

- to install an Integrated development environment(we used visual code for this one).

- you also need to install the latest version of python(3.10 at this moment).

-you also need to install pytest (use cmd line).

# Usage

-To use the program, you need to type python -m paytest
this should active the test so you can see the program in action.

- you can also initiate a new column with a set of attrivutes set
by you the see the program in execution(column = Column(your inputs).)
## Example

if you initiate a new column like
columnA = Column(id, number of floors, number of elevators )
the program will create a column with the number of floors 
and number of elevators.

if we set this values:
Elevator A is Idle at floor 2 
Elevator B is Idle at floor 6
Someone is on floor 3 and wants to go to the 7th floor. 

the outcome will be :
Elevator A is expected to be sent.
