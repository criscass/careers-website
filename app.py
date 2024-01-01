from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Python Developer',
        'location': 'New York',
        'salary': '$100,000'
    },
    {
        'id': 2,
        'title': 'Frontend Developer',
        'location': 'San Francisco',
        'salary': '$110,000'
    },
    {
        'id': 3,
        'title': 'Backend Developer',
        'location': 'Los Angeles',
        'salary': '$120,000'
    },{
      'id': 4,
      'title': 'Cloud Engineer',
      'location': 'Pasadina'
  }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)