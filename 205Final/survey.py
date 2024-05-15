import random

teams = range(3473,3487)

def odd_func(my_num):
    if int(my_num)%2 == 0:
        return [x for x in teams if x%2 != 0]
    else:
        return [x for x in teams if x%2 == 0]

try:
    team_num = input("Enter your team number: ")
    if int(team_num) not in teams:
        raise ValueError()
except ValueError:
    print(f'\n{"*"*20}\nPlease enter a valid team number.\nThis incident will be recorded.\nGood bye.\n{"*"*20}')
    print(hex(id(team_num)) + '\n')
else:
    possible_teams = [t for t in odd_func(team_num) if t!=int(team_num) ]
    print( random.sample(possible_teams, 4) )