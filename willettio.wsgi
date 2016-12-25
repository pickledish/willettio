from werkzeug.wsgi import DispatcherMiddleware
from mainPage import app as frontend

application = DispatcherMiddleware(frontend)