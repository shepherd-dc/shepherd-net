from app.app import create_app

app = create_app()

@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)