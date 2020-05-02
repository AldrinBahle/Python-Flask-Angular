from config import app, mysql

def create_app(config_filename):
    app.config.from_object(config_filename)

    from location import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    from btysrvc import api_btysrvc
    app.register_blueprint(api_btysrvc, url_prefix='/api/v2')

    return app

@app.route("/")
def home():
    return ("Uzuri Africa")

if __name__ == '__main__':
    app = create_app("config")
    app.run(debug=True)