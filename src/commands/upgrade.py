'''
  apkg
  ~~~~

  The Agda Package Manager.

'''

# ----------------------------------------------------------------------------

import click

from git       import *
from pony.orm  import *

from .init     import init
from ..config  import REPO

# ----------------------------------------------------------------------------

@click.group()
def upgrade(): pass

@upgrade.command()
@click.pass_context
def upgrade(ctx):
  """Update the list of available packages."""
  try:
    origin = REPO.remotes["origin"]
    click.echo("Updating Agda-Pkg from " + [url for url in REPO.remote().urls][0])
    for pull_info in origin.pull():
      click.echo("%s to %s" % (pull_info.ref, pull_info.commit))
    ctx.invoke(init, drop_tables=False)
  except Exception as e:
    logger.error(e)
  


