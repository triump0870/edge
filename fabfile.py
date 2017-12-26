from fabric.api import local, task, execute, run
import random
import string


@task()
def deploy_to_heroku():
    local('git init')
    local('heroku login')
    local('heroku create')
    set_config()
    local('git add -A')
    local('git commit -m "%s" ' % input("Enter commit message: "))
    local('git push heroku master')


def set_config():
    """Set the heroku config variables"""
    secret_key = generate_key()
    local('heroku config:set SECRET_KEY=%s' % secret_key)
    local('heroku config:set DJANGO_SETTINGS_MODULE=%s' % "{{ project_name }}.settings.production")


def generate_key():
    return "".join([random.SystemRandom().choice(string.digits + string.ascii_letters) for i in range(100)])
