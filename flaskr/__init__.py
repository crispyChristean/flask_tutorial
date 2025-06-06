#This file serves to contain
# an application factory and
# tells the flaskr directory should be
# treated like a package


import os 

from flask import Flask

def create_app(test_config=None):
    #Create and configure the app
    app = Flask(__name__, instance_relative_config=True) 
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        #Loadd instance config, of it exist when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Load the test config if passed in
        app.config.from_mapping(test_config)
    #Ensure the instance folder exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Page says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)


    from . import auth
    app.register_blueprint(auth.bp)


    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app
