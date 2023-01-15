from flask import Flask, redirect, url_for, request,render_template,jsonify,json

app = Flask(__name__)#app is the object of flask class

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
      fname = request.form['firstname']
      lname=request.form['lastname']
      weight=int(round(float(request.form['weight']),1))
      height=round(float(request.form['height']),2)
      phonenumber=int(request.form['pnumber'])
      bmi=int((weight)/(height*height))
      if bmi <= 18.5:  
         return(f"Hello {fname} {lname} \n Oops! You are underweight.")  
      elif bmi <= 24.9:  
        return(f"Hello {fname} {lname} \nAwesome! You are healthy.")  
      elif bmi <= 29.9:  
        return(f"Hello  {fname} {lname} \nEee! You are overweight.")  
      else:  
         return(f"Hello  {fname} {lname} \nSeesh! You are obese.") 
if __name__ == '__main__':
   app.run(debug=True)
