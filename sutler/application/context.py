import click
import os


class Context(object):
    def __init__(self):
        self.action = None
        self.machine = None
        self.os = None
        self.paths = {}
        self.program = None
        self.user = None

    # Path Functions

    def get_path(self, key: str, default=None):
        return self.paths.get(key, default)

    def set_path(self, key: str, value):
        if not os.path.exists(value):
            raise FileNotFoundError('Path not found.')
        self.paths[key] = value

    def del_path(self, key: str):
        del self.paths[key]

    # Debug functions

    def print(self):
        click.secho("Action", bold=True)
        click.secho(f"  {self.action}")
        click.echo()
        click.secho("Machine", bold=True)
        click.secho(f"  {self.machine}")
        click.echo()
        click.secho("Operating System", bold=True)
        click.secho(f"  {self.os}")
        click.echo()
        click.secho("Program", bold=True)
        click.secho(f"  {self.program}")
        click.echo()
        click.secho("User", bold=True)
        for key, value in vars(self.user).items():
            click.secho(f"{key}", nl=False, fg='cyan')
            click.secho(f": {value}")
        click.echo()
        click.secho("Paths", bold=True)
        for key, value in self.paths.items():
            click.secho(f"{key}", nl=False, fg='cyan')
            click.secho(f": {value}")