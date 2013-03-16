from bottle import run, route, request, template


@route('/')
def index():
    return template('index')


@route('/query')
def query():
    query = request.query.get('q')
    return template('query', query=query)


if __name__ == '__main__':
    run(reloader=True)
