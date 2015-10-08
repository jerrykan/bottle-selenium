from bottle import Bottle, run, request, template

app = Bottle()


@app.route('/')
def index():
    return template('index')


@app.route('/query')
def query():
    query = request.query.get('q')
    return template('query', query=query)


if __name__ == '__main__':
    run(reloader=True)
