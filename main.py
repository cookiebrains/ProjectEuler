import subprocess
import os.path
from os import path

problem_num = 48
problem_dir = 'Problem' + str(problem_num)
problem_script = 'Problem' + str(problem_num) + '.py'

if __name__ == '__main__':
    if not path.exists(os.path.join(problem_dir, problem_script)):
        print('that don\'t exist yo')
    else:
        subprocess.call(['python', problem_script], cwd=problem_dir)

