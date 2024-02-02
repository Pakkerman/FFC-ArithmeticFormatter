const problems1 = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
const problems2 = [
  '98 + 3g5',
  '3801 - 2',
  '45 + 43',
  '123 + 49',
  '98 + 3g5',
  '3801 - 2',
  '45 + 43',
  '123 + 49',
]
const problems3 = ['98 / 325', '3801 - 2', '45 + 43', '123 + 49222']
const problems4 = ['32 + 8', '1 - 3801', '9999 + 9999', '523 - 49']

console.log('\n ---- P1 ---- \n')
console.log(arithmeticFormatter(problems1))
console.log('\n ---- P2 ---- \n')
console.log(arithmeticFormatter(problems2))
console.log('\n ---- P3 ---- \n')
console.log(arithmeticFormatter(problems3))
console.log('\n ---- P4 ---- \n')
console.log(arithmeticFormatter(problems4))

function arithmeticFormatter(problems: string[]): any {
  if (5 < problems.length) {
    return 'Error: Too many problems.'
  }

  const parsedProblems: any = []
  for (const problem of problems) {
    const [operant1, operator, operant2] = problem.split(' ')
    const validOperator = validateOperator(operator)
    const validOperant1 = validateOperant(operant1)
    const validOperant2 = validateOperant(operant2)

    if (!validOperator) {
      return "Error: Operator must be ' + ' or ' - '.'"
    }

    if (!validOperant1 || !validOperant2) {
      return 'Error: Numbers must only contain digits.'
    }

    if (4 < operant1.length || 4 < operant2.length) {
      return 'Error: Numbers cannot be more than four digits.'
    }

    parsedProblems.push({ operant1, operant2, operator })
  }

  return printProblems(parsedProblems)
}

function printProblems(problems) {
  const out: string[][] = Array.from({ length: 4 }, () => [])

  const indent = '    '

  for (const item of problems) {
    const width = Math.max(item.operant1.length, item.operant2.length)
    out[0].push(item.operant1.padStart(width + 2))
    out[1].push(item.operator, item.operant1.padStart(width + 1))
    out[2].push('-'.repeat(width + 2))
    out[3].push(
      eval(`${item.operant1}${item.operator}${item.operant2}`)
        .toString()
        .padStart(width + 2)
    )

    for (const row of out) {
      row.push(indent)
    }
  }

  return out.map((item) => item.join('')).join('\n')
}

function validateOperator(operator: string): boolean {
  if (operator == '+' || operator == '-') return true
  return false
}

function validateOperant(operant: string): boolean {
  if (isNaN(Number(operant))) return false
  return true
}
