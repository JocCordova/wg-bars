import os
import sys

def main():
	
	os.system(f"set FLASK_APP=webapp.py")
	os.system(f"flask run --host=0.0.0.0")
    	
	return 0

if __name__ == '__main__':
	
	main()
