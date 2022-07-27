from os.path import dirname, join
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.models import db
from app.models.role import Role
# from app.models.log import Log

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Koqmed-Chivma@localhost:5432/abcs_amm_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# register app and db with migration class
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
    db.create_all()


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

#
# @app.route('/api/v1/logs')
# def get_logs():
#     return Log.find_all()
