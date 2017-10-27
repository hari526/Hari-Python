def which_prize(points):
    if points>0 and points<50:
        print("Congratulations! You have won a wooden rabbit!")
    elif points>51 and points<150:
        print("Oh dear, no prize this time.")
    elif points>151 and points<180:
        print("Congratulations! You have won a wafer-thin mint!")
    elif points>181 and points<200:
        print("Congratulations! You have won a penguin!")
    
test1=which_prize(2)
print(test1)
