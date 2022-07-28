from os.path import join, dirname

from dotenv import load_dotenv
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import app
from app.models import db

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# register app and db with migration class

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


# @manager.option('-e', '--email', dest='email')
# @manager.option('-p', '--password', dest='password')
# @manager.option('-c', '--confirm_password', dest='confirm_password')
# def admin_user(email, password, confirm_password):
#     create_superuser(email, password, confirm_password)


# @manager.command
# def create_roles():
#     create_default_roles()
#
#
# @manager.command
# def create_registries():
#     add_registries()


if __name__ == '__main__':
    manager.run()
