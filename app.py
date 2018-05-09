from flask import Flask , render_template 

app = Flask (__name__)

@app.route('/upcode')
def upcode () :
	return render_template ("upcode.html")

if __name__ == '__main__' :
	app.run(debug = True)

