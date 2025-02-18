from app.controllers.application import Application
from bottle import request

# Inicialize a aplicação
app = Application()

# Middleware to store the Application instance in the request environment
@app.app.hook('before_request')
def before_request():
    request.environ['application'] = app

# executa a aplicação
if __name__ == '__main__':

    import eventlet
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8080)), app.wsgi_app)
