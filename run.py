import os
from app import MS3DM

app = MS3DM(__name__)

if __name__ == '__main__': 
    os.environ['FLASK_DEBUG'] = 'development'
    app.run()
