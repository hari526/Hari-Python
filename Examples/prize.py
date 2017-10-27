def which_prize():
    points = int(input("enter the points they scored : "))
    if(points <= 50):
        print("Congratulations! You have won a wooden rabbit!")
    elif(points >=51 and points <= 150):
        print("Oh dear, no prize this time.")
    elif(points >=151 and points <= 180):
        print("Congratulations! You have won a wooden waffer_thin mint!")
    elif(points >= 181 and points<=200):
        print("Congratulations! You have won a penguin!")
    else:
        print("nothing")

which_prize()
