from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':'1',
    'title':'Data Scientist',
    'location':'Dhaka,Bangladesh',
    'salary':'TK. 80,000'
  },
  {
    'id':'2',
    'title':'Data Engineer',
    'location':'Banglore,India',
    'salary':'RS. 100,000'
  },
  {
    'id':'3',
    'title':'Frontend Developer',
    'location':'Rajshahi,Bangladesh',
    'salary':'TK. 50,000'
  },
  {
    'id':'4',
    'title':'Backend Developer',
    'location':'remote',
    'salary':'TK. 90,000'
  }
  
]

@app.route("/")
def softtech_world():
  return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def job_lists():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
