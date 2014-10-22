###############################
#                             #
#           Review 2!         #
#                             #
###############################

# Write a program that uses a loop to print out:

#           2
#           4
#           6
#           8
# Who do we appreciate?

# Use a loop to complete this, either a for loop or a while loop.
# Each time through the loop, print out either 2, 4, 6 or 8.
# When the loop is finished, print "Who do we appreciate?"
# Remember how range can be used to create the list [2,4,6,8]
# When complete, commit to github and submit a pull request!

lis = [2,4,6,8]
song = 2


while song > -1:
    print "Who do we appreciate?"
    song = song - 1
    for x in lis:
        print x
    if song == -1:
        print "Mr.edgeley"