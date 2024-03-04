from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def myFunc():
    name = input()
    print(f"Hello, {name}!")
    return render_template('index.html')

if __name__ == '__main__':
    print("Hello Vedant!! It worked.")
    app.run(host='0.0.0.0', port=5000)

    
