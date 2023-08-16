def arithmetic_arranger(problems, showanswers = False):

    firstline = ""
    secondline = ""
    thirdline = ""
    fourthline = ""
    if len(problems) > 5:
       arranged_problems = 'Error: Too many problems.'
       return arranged_problems
    else:
        counter = len(problems)
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
                arranged_problems = "Error: Operator must be '+' or '-'."
                return arranged_problems
            comps.append(problemanswer)
         


            if len(str(first)) > len(str(second)):
                firstex = "  " + str(first)
                secondex = operation + " " + (" " * (len(str(first)) - len(str(second)))) + str(second)
                thirdex = "-" * len(firstex)
            else:
                firstex = "  " + (" " * (len(str(second)) - len(str(first)))) + str(first)
                secondex = operation + " " + str(second)
                thirdex = "-" * len(secondex)
            if counter > 1:
                firstline = firstline + firstex + "    "
                secondline = secondline +  secondex + "    "
                thirdline = thirdline + thirdex + "    "
                fourthline = fourthline + (" " * (len(thirdex) - len(str(problemanswer)))) + str(problemanswer) + "    "
            else:
                firstline = firstline + firstex 
                secondline = secondline +  secondex
                thirdline = thirdline + thirdex
                fourthline = fourthline + (" " * (len(thirdex) - len(str(problemanswer)))) + str(problemanswer)
            counter -= 1
            if showanswers:
                arranged_problems = firstline + '\n' + secondline + '\n' + thirdline + '\n' + fourthline
            else:
                arranged_problems = firstline + '\n' + secondline + '\n' + thirdline


    return arranged_problems

