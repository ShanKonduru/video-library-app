from flask import Flask, render_template
from app import app, delete_service, edit_service, view_service

app = Flask(__name__)

# Routes for each microservice
app.register_blueprint(app.bp)
app.register_blueprint(delete_service.bp)
app.register_blueprint(edit_service.bp)
app.register_blueprint(view_service.bp)

if __name__ == '__main__':
    app.run(debug=True)
