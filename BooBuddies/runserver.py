<<<<<<< HEAD
"""
This script runs the BooBuddies application using a development server.
"""

from os import environ
from BooBuddies import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
=======
"""
This script runs the BooBuddies application using a development server.
"""

from os import environ
from BooBuddies import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
>>>>>>> 6c8f3592e94cca8166ec075cce554b0c4c225d0f
