from flask import Flask, render_template, g
import database_helper as db

app = Flask(__name__)

@app.route('/')
def home():
	db.main()
	return render_template("index.html")

def main():
	app.run()
	

    
if __name__ == '__main__':
   main()

