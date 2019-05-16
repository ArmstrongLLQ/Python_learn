#! /home/user/anaconda3/bin/python
import os

def main():
	fork_num = input('please input fork_num\n')
	try:
		fork_num = int(fork_num)
	except Exception as e:
		raise e
	for i in range(fork_num):	
		print('Process (%s) start...' % os.getpid())

		pid = os.fork()

		if pid == -1:
			return -1
		elif pid == 0:
		    print('i am child process %s and my parent is %s' % (os.getpid(), os.getppid()))
		else:
		    print('i %s just create a child process %s' % (os.getpid(), pid))

if __name__ == '__main__':
	main()