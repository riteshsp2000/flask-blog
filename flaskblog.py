from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
  {
    "title": "Hi",
    "author": "Ritesh",
    "content": "Starting with flask",
    "date_posted": "6/6/20"
  }
]

@app.route("/")
@app.route("/home")
def home(): 
  return render_template('home.html', posts) 

@app.route("/about")
def about(): 
  return render_template('about.html')  

if __name__ == '__main__':
  app.run(debug=True) 