from __future__ import print_function
import socket
import time
import sys



def main():
	"""
	usage: python socketStreamer.py 8888 iris.csv 1
	"""
	if len(sys.argv) <= 1:
		print("Please specify the port and file name.")

	s = socket.socket()

	port = sys.argv[1]

	file = sys.argv[2]

	if len(sys.argv) > 3:
		wait = sys.argv[3]
	else:
		wait = 1

	s.bind(('127.0.0.1', int(port)))

	s.listen(3)
	print("Start streaming")

	while True:

		c, addr = s.accept()

		with open(file, 'rb') as f:
			for line in f.readlines():
				c.send(line)
				time.sleep(wait)

		c.send("")

		c.close()


if __name__ == "__main__":
	main()



