from distutils.log import debug
from app import create_app
from flask_script import Manager,Server
import unittest

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run(debug=True)