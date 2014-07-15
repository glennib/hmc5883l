from hmc5883l import hmc5883l
import time

compass = hmc5883l()

while True:
	print chr(27) + "[2J"
	print "%.2F" % compass.heading()
	time.sleep(0.2)
