def number_counter():
    """(float,float)->float
        repeatedly input a number
        after each number is inputted, function should display
        1)how many number entered
        2)sum of all numbers
        when  sum>256, return.
        
        >>>number_counter()
        Enter a number: 1
        Total number entered is 1
        Sum of number entered is 1
        Enter a number: 500
        Total number entered is 2
        Sum of number entered is 501
        ----------Start another round----------
        Enter a number: 900
        Total number entered is 1
        Sum of number entered is 900

    """
    total = 0
    count = 0
    while True:
        num = input ("Enter a number: ")
        total += float (num)
        count += 1
        print("Total number entered is {}".format (str (count)))
        print ("Sum of number entered is {}".format (str (total)))
        if total> 256 :
            total=0
            count=0
            print ("----------Start another round----------")
            continue






def rps_round():
    """(string, string)->string
        run one round Rock, Paper,Scissors
        reutrns win or lose
        If there is a tie, the round continues. Use recursion
        and call the round again
        >>>rps_round()
        rock, paper, scissors? rock
        rock, paper, scissors? paper
        rock, paper, scissors? rock
        'You Win!'
    """
    import random
    a = ["rock", "paper","scissors"]
    answer =  random.choice(a)
    player = input ("rock, paper, scissors? ")
    if player == answer:
        return rps_round()
    elif player == "rock":
        if answer == "scissors":
            return "You Win!"
        else:
            return "You Lose."
    elif player == "paper":
        if answer == "scissors":
            return "You Lose."
        else:
            return "You Win!"
    elif player == "scissors":
        if answer == "rock":
            return "You Lose."
        else:
            return "You Win!"
    else:
        return "invalid input"







def rps_best_of_five():
    """string, string)->string
        run a series of 5 rounds of rps_round()
        until the user or the computer wins "best three out of five"
        After each round, print the number of wins and losses.
        
        >>> rps_best_of_five()
        rock, paper, scissors? paper
        Win 1, Lose 0
        rock, paper, scissors? rock
        Win 2, Lose 0
        rock, paper, scissors? paper
        Win 3, Lose 0
        rock, paper, scissors? paper
        rock, paper, scissors? rock
        Win 3, Lose 1
        rock, paper, scissors? rock
        Win 3, Lose 2
        You Win Best Three Out Of Five (*￣▽￣)/‧

        
    """
    while True:
        count_win = 0
        count_lose = 0
        count_total = 0
        while count_total <5:
            result = rps_round()
            count_total += 1
            if result == "You Win!":
                count_win +=1
                print ("Win {}, Lose {}".format(count_win,count_lose))
            elif result == "You Lose.":
                count_lose +=1
                print ("Win {}, Lose {}".format(count_win,count_lose))
            else:
                count_total -=1
                print ("Invalid input")
                continue
        else:
            if count_win==3 :
                print("You Win Best Three Out Of Five (*￣▽￣)/‧")
                break
            elif count_lose == 3:
                print ("Computer Win Best Three Out Of Five (´・ω・`)")
                break
            else:
                print ("---------------No one win Best Three Out Of Five-----------")
                continue

    
        
