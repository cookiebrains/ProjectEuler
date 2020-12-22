import subprocess
import os.path
from os import path
from utilz import MyStopwatch

problem_num = 11
problem_dir = 'Problem' + str(problem_num)
problem_script = 'Problem' + str(problem_num) + '.py'


if __name__ == '__main__':
    if not path.exists(os.path.join(problem_dir, problem_script)):
        print(f'that problem don\'t exist, yo ({problem_num})')
        exit(-1)
    print(f'Problem number {problem_num}')
    print('-----------------')
    print('')
    sw = MyStopwatch()
    sw.start('total')
    subprocess.call(['python', problem_script], cwd=problem_dir, shell=True)
    sw.stop('total')
    print('')
    print('-----------------')
    sw.print_all()

