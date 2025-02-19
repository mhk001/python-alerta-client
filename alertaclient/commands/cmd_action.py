import click

from alertaclient.utils import action_progressbar, build_query


@click.command('action', short_help='Action alerts')
@click.option('--action', '-a', metavar='ACTION', help='Custom action (user-defined)')
@click.option('--ids', '-i', metavar='ID', multiple=True, help='List of alert IDs (can use short 8-char id)')
@click.option('--query', '-q', 'query', metavar='QUERY', help='severity:"warning" AND resource:web')
@click.option('--filter', '-f', 'filters', metavar='FILTER', multiple=True, help='KEY=VALUE eg. serverity=warning resource=web')
@click.option('--text', help='Message associated with action')
@click.pass_obj
def cli(obj, action, ids, query, filters, text):
    """Take action on alert'."""
    client = obj['client']
    if ids:
        total = len(ids)
    else:
        if query:
            query = [('q', query)]
        else:
            query = build_query(filters)
        total, _, _ = client.get_count(query)
        ids = [a.id for a in client.get_alerts(query)]

    label = 'Action ({}) {} alerts'.format(action, total)
    action_progressbar(client, action=action, ids=ids, label=label, text=text)
