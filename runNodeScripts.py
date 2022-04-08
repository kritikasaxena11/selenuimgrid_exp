from subprocess import Popen
import glob
tests = glob.glob('node*.py')
processes = []
for test in tests:
 processes.append(Popen('python %s' % test, shell=True))
for process in processes:
 process.wait()