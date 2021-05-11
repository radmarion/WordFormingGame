"""
So this is a game that can be used on encouragement date, hangouts or fun devo:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ RULES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a number of options which contain 5 words each. A team of 2 
or an individual picks a random number from 1 to 'n' where n is the 
last number of the option and they are supposed to form a reasonable
sentence using those 5 words. A correct answer is awarded 2 points

For a team, when it is a member of the team's turn a correct answer is awarded 2 points
else the partner of the member of the team can answer for 1 point if the first teammate can't
answer correctly and vice versa when it is the second teammate's turn

"""


number  = input('what is your number ')
number = int(number)

#The code can be modified to suit the user's benefits
#The words too in the string quotes can be changed depending on the user's choice

if number == 1:
    print(" Go,you,tomorrow,time,try")
elif number == 2:
    print(" fly,try,to,brain,tough")
elif number == 3:
    print(" weigh,height,tower,bricks,mud")
elif number == 4:
    print(" bread,stew,eat,afternoon,black")
elif number == 5:
    print(' dough,flour,eggs,make,farm')
elif number == 6:
    print(' blouse,fashion,tailor,area,days')
elif number == 7:
    print(' play,child,pepper,salt,brine')
elif number == 8:
    print(' please,dock,program,year,ship')
elif number == 9:
    print(' shop,house,enter,kill,true')
elif number == 10:
    print(' friend,trust,church,drive,food')
elif number == 11:
    print(' small,chops,party,event,canopy')
elif number == 12:
    print(' bro,code,fun,chow,yesterday')
else:
    print("This number is not part of the option")

# More numbers can be added in the grouped if/else if statements