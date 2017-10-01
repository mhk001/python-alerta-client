
import click

from alertaclient.auth import get_token


@click.command('token', short_help='display current auth token')
@click.pass_obj
def cli(obj):
    """Display the auth token for logged in user."""
    client = obj['client']
    click.echo(get_token(client.endpoint))
