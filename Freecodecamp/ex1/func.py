def arithmetic_arranger(problems):

    firstline = ""
    secondline = ""
    thirdline = ""
    fourthline = ""

    def largest_len(list):
        largest = 0
        for item in list:
            if len(str(item)) > largest:
                largest = len(str(item))
        return largest

        


    if len(problems) > 5:
       arranged_problems = 'Error: Too many problems.'
       return arranged_problems
    else:
        for problem in problems:
            comps = problem.split()
            try:
                first = int(comps[0])
                second = int(comps[2])
            except:
                arranged_problems = 'Error: Numbers must only contain digits.'
                return arranged_problems
            if len(comps[0]) > 4 or len(comps[2]) > 4:
                arranged_problems = 'Error: Numbers cannot be more than four digits.'
                return arranged_problems
            if comps[1] == '+':
                operation = comps[1]
                problemanswer = first + second
            elif comps [1] == '-': 
                operation = comps[1]
                problemanswer = first - second
            else: 
                arranged_problems = 'Error: Operator must be '+' or '-'.'
                return arranged_problems
            comps.append(problemanswer)

            firstex = " " + (str(first))            
            secondex = operation + " " + str(second)
            thirdex = "-" * largest_len([firstex, secondex, problemanswer])
            
            firstline = firstline + (" " * (len(thirdex) - len(firstex))  +   firstex) + "    "
            secondline = secondline + secondex + "    "
            thirdline = thirdline + thirdex + "    "
            fourthline = fourthline + (" " * (len(thirdex) - len(str(problemanswer)))) + str(problemanswer) + "    "


        arranged_problems = (firstline + "\n" + secondline + "\n" + thirdline + "\n" + fourthline)

    return arranged_problems

