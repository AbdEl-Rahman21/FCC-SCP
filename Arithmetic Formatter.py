def arithmetic_arranger(problems, show_answers=False):
    separate_problems = list(map(lambda x: x.split(), problems))
    error = check_errors(separate_problems)
    final_text = []

    if not error is None: return error

    final_text.append(create_first_line(separate_problems))
    final_text.append(create_second_line(separate_problems))
    final_text.append(create_third_line(separate_problems))

    if show_answers: final_text.append(create_forth_line(separate_problems))

    return '\n'.join(final_text)

def check_errors(problems):
    if len(problems) > 5: return 'Error: Too many problems.'
    else:
        for problem in problems:
            if not problem[1] in ['+', '-']:
                return "Error: Operator must be '+' or '-'."
            elif not (problem[0].isdigit() and problem[2].isdigit()):
                return 'Error: Numbers must only contain digits.'
            elif not (len(problem[0]) <= 4 and len(problem[2]) <= 4):
                return 'Error: Numbers cannot be more than four digits.'

def create_first_line(problems):
    first_line = []

    for problem in problems:
        first_line.append('  ')

        if len(problem[0]) > len(problem[2]):
            first_line.append(problem[0] + '    ')
        else:
            for _ in range(len(problem[2]) - len(problem[0])):
                first_line.append(' ')
            
            first_line.append(problem[0] + '    ')

    return ''.join(first_line).rstrip(' ')

def create_second_line(problems):
    second_line = []

    for problem in problems:
        second_line.append(f'{problem[1]} ')

        if len(problem[2]) > len(problem[0]):
            second_line.append(problem[2] + '    ')
        else:
            for _ in range(len(problem[0]) - len(problem[2])):
                second_line.append(' ')
            
            second_line.append(problem[2] + '    ')

    return ''.join(second_line).rstrip(' ')

def create_third_line(problems):
    third_line = []

    for problem in problems:
        third_line.append('--')

        for _ in range(max(len(problem[0]), len(problem[2]))):
            third_line.append('-')

        third_line.append('    ')

    return ''.join(third_line).rstrip(' ')

def create_forth_line(problems):
    forth_line = []

    for problem in problems:
        if problem[1] == '+':
            answer = int(problem[0]) + int(problem[2])
        else:
            answer = int(problem[0]) - int(problem[2])

        for_range = abs(max(len(problem[0]), len(problem[2])) + 2 - len(str(answer)))

        for _ in range(for_range):
            forth_line.append(' ')

        forth_line.append(str(answer) + '    ')

    return ''.join(forth_line).rstrip(' ')

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
