import click
import datetime
from personal_email.send import *


@click.group()
def cli():
    """This script is aimed to provide email services
    """
    pass


@cli.command()
@click.argument('subject')
@click.argument('body', default='Refer to Subjects')
def send(subject, body):

    """
    provide subject
    provide body msg
    example:
    email send "Hello" "It's a New Day"
    """
    send_email(subject, body)

if __name__ == '__main__':
    cli()