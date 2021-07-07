"""
A one cli for all the anime.
"""

import click

from core.cli.commands import download, stream, continuation, grab, schedule, test
from core.cli.helpers.player import supported_streamers

commands = {
    'download': download.animdl_download,
    'continue': continuation.animdl_continue,
    'grab': grab.animdl_grab,
    'schedule': schedule.animdl_schedule,
    'test': test.animdl_test
}

executable = [*supported_streamers()]

if executable:
    commands.update({'stream': stream.animdl_stream})
	
@click.group(commands=commands)
def __animdl_cli__():
    pass

if __name__  == '__main__':
    __animdl_cli__()