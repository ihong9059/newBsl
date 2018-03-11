from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)

if __name__ == '__main__':
    app.run(debug=True)

"""
 {% ... %} for Statements
 {{ ... }} for Expressions to print to the template output
 {# ... #} for Comments not included in the template output
 # ... ## for Line Statements

"""
