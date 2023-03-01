import os
from itertools import chain

import click

from .constants import VALID_CONFIG_DIR_FILE_EXTENSIONS
from .utils import get_config_dir


@click.command(
    name="ls",
    short_help="List configured sessions in :meth:`tmuxp.cli.utils.get_config_dir`.",
)
def command_ls():
    tmuxp_dir = get_config_dir()
    if os.path.exists(tmuxp_dir) and os.path.isdir(tmuxp_dir):
        for f in sorted(
            chain.from_iterable(
                files for _, _, files in os.walk(tmuxp_dir, followlinks=True)
            )
        ):
            stem, ext = os.path.splitext(f)
            if os.path.isdir(f) or ext not in VALID_CONFIG_DIR_FILE_EXTENSIONS:
                continue
            print(stem)
