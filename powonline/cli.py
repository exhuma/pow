import logging

import click
from powonline.model import DB, Role, User
from powonline.web import make_app

LOG = logging.getLogger(__name__)


@click.command()
@click.argument('login')
def grant_admin(login: str) -> None:
    """
    Grants the "admin" role to the user with login "login"
    """
    app = make_app()  # type: ignore
    with app.app_context():
        query = User.query.filter_by(name=login)
        user = query.one_or_none()
        if not user:
            print('No such user')
        else:
            user.roles.add(Role.get_or_create(DB.session, 'admin'))
        DB.session.commit()


@click.command()
@click.argument('login')
def revoke_admin(login: str) -> None:
    """
    Revokes the "admin" role from the user with login "login"
    """
    app = make_app()  # type: ignore
    with app.app_context():
        query = User.query.filter_by(name=login)
        user = query.one_or_none()
        if not user:
            print('No such user')
        else:
            user.roles.remove(Role.get_or_create(DB.session, 'admin'))
        DB.session.commit()


@click.command()
def list_users() -> None:
    """
    Lists the existing users in the DB
    """
    app = make_app()  # type: ignore
    with app.app_context():
        query = User.query.order_by(User.name)
        for row in query:
            print(row.name)