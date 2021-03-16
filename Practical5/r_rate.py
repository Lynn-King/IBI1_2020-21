n = 84 
rounds = 5
# 1.2 is the index times, which means the model is like infected_individuals = individuals * (1.2)^(n -1)
def infected_individuals = n*1.2^(rounds-1):
    print(infected_individuals)
# rounds can be modified by any number
    print('there are'+''+str(infected_individuals)+''+'being infected by'+''+'str(n)'+''+'people')


