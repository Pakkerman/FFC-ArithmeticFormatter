problems1 = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
problems2 = [
  '98 + 3g5',
  '3801 - 2',
  '45 + 43',
  '123 + 49',
  '98 + 3g5',
  '3801 - 2',
  '45 + 43',
  '123 + 49',
]
problems3 = ['98 + 325', '3801 - 2', '45 + 43', '123 + 49222']
problems4 = ['98 / 325', '3801 - 2', '45 + 43', '123 + 49222']
problems5 = ['32 + 8', '1 - 3801', '9999 + 9999', '523 - 49']



def arithmetic_arranger(problems, calculateSum=False): 
  # print(f'\n -- Arithmetic Formatter -- \n')

  if 5 < len(problems) :
    return 'Error: Too many problems.'
  
  parsedProblems = []
  for problem in problems:
    operant1, operator, operant2 = problem.split()
    valid_operator = validate_operator(operator)
    valid_operant1 = validate_operant(operant1)
    valid_operant2 = validate_operant(operant2)

    if not valid_operator:
      return "Error: Operator must be '+' or '-'."
    if not valid_operant1 or not valid_operant2:
      return "Error: Numbers must only contain digits."
    if 4 < len(operant1) or 4 < len(operant2):
      return 'Error: Numbers cannot be more than four digits.'

    parsedProblems.append({'operant1': operant1, 'operant2': operant2, 'operator': operator})


  # print(problems)
  # print(f'\n -- END -- \n')

  return getOutput(parsedProblems, calculateSum)

def getOutput(parsedProblems, calculateSum):
  out = list([] for _ in range(4))
  indent = '    '

  for item in parsedProblems:
    operant1 = item['operant1']
    operant2 = item['operant2']
    operator = item['operator']
    width = len(operant1) if len(operant2) < len(operant1) else len(operant2)
    out[0].append(operant1.rjust(width + 2))
    out[1].append(operator+' '+operant2.rjust(width))
    out[2].append('-' * (width + 2))
    sum = 0

    if operator == '+':
      sum = int(operant1) + int(operant2)
    if operator == '-':
      sum = int(operant1) - int(operant2)

    out[3].append(str(sum).rjust(width + 2))

  for i in range(len(out)):
    out[i] = indent.join(out[i])


  if calculateSum:
    out = '\n'.join(out)
  else:
    out = '\n'.join(out[:-1])

  return out

def validate_operator(operator):
  if operator == '+' or operator == '-':
    return True
  else:
    return False
  
def validate_operant(operant):
  try:
    if int(operant):
      return True
  except ValueError:
    return False

print('\n\n\n\n\n\n\n\n\n\n------------------------------------------------')
print(arithmetic_arranger(problems1), '\nexpected: invalid digits')
print(arithmetic_arranger(problems2), '\nexpected: too many problems')
print(arithmetic_arranger(problems3), '\nexpected: too many digits')
print(arithmetic_arranger(problems4), '\nexpected: invalid operator')
print(arithmetic_arranger(problems5) )

