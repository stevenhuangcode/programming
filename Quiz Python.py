# Quiz Game

correct = 0
incorrect = 0

# Question 1
if input("What is the name of the famous tower in Paris?").lower() == "eiffel":
    print("Correct")
    correct += 1
else:
    print("Incorrect")
    incorrect += 1

# Question 2
Donnie_Yen = input("How many Ip Man movies are there (ft. Donnie Yen)")
if Donnie_Yen == "4" or Donnie_Yen.lower() == "four":
    print("Correct")
    correct += 1
else:
    print("Incorrect")
    incorrect += 1

# Question 3
if input("Capital of New York / a. NYC b. NCY c. CYN d. Albany").lower() == "d":
    print("Correct")
    correct += 1
else:
    print("Incorrect")
    incorrect += 1

# Question 4
if input("Which country does pineapple pizza come from?").lower() == "canada":
    print("Correct")
    correct += 1
else:
    print("Incorrect")
    incorrect += 1

# Question 5
if input("True or False, there is a Popeye's in Richmond").lower() == "true":
    print("Correct")
    correct += 1
else:
    print("Incorrect")
    incorrect += 1

print(f" You have {correct} correct answers and {incorrect} incorrect answers")
if (correct / (correct + incorrect)) * 100 >= 60:
    print(f" Congrats. You passed with a score of {(correct / (correct + incorrect)) * 100} %")
elif (correct / (correct + incorrect)) * 100 <= 60:
    print(f" Sorry. You failed with a score of {(correct / (correct + incorrect)) * 100} %")