from flask import Flask, request, jsonify, render_template
import pandas as pd
import os



app = Flask(__name__)

@app.route("/")
def index():
	a = 100
	b = 20
	osc1 = pd.read_excel('osc_1_1_1.xls')
	osc2 = pd.read_excel('osc_1_1_2.xls')
	theta1 = pd.read_excel('osc_1_1_1.xls',sheetname='phase')
	theta2 = pd.read_excel('osc_1_1_2.xls',sheetname='phase')

	osc = pd.concat([osc1.Y,osc2.Y],axis=1)#.values.tolist()
	mx = osc.max().max()
	mn = osc.min().min()
	mxx = ((osc - mn)/mx).max().max()
	osc = 2*((osc-mn)/mx)/mxx

	
	phase = pd.concat([theta1.fillna(0).phase % 6.28,theta2.fillna(0).phase % 6.28,],axis=1)


	return render_template('index.html', a=a, b=b, 
		osc=osc.round(3).values.tolist()[:1200], 
		phase=phase.round(3).values.tolist()[:1200])

if __name__ == '__main__':
	port = int(os.environ.get('PORT',8000))
	app.debug = False
	app.run(host = '0.0.0.0',port=port)