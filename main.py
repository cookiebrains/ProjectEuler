from utilz import MyStopwatch
from problems import problem_56 as problem


def get_problem_num():
    problem_num_string = ''
    found = False
    for c in problem.__name__:
        if c.isdigit():
            found = True
            problem_num_string += c
        elif not c.isdigit() and found:
            break
    return problem_num_string


if __name__ == '__main__':
    print(f'Problem number {get_problem_num()}')
    print('-----------------')
    print('')

    sw = MyStopwatch()
    sw.start('total')

    problem.run()

    sw.stop('total')

    print('')
    print('-----------------')

    sw.print_all()
