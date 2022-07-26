"""Configures tasks to run with invoke."""
import glob
import os
import sys
from invoke import task


@task(
    aliases=["flake8", "pep8"],
    help={
        'filename': 'File(s) to lint. Supports globbing.',
        'envdir': 'Specify the python virtual env dir to ignore. Defaults to "venv".',
        'noglob': 'Disable globbing of filenames. Can give issues in virtual environments',
    },
)
def lint(_ctx, filename=None, envdir=['env', 'venv'], noglob=False):
    """Run flake8 python linter.

    :param _ctx: Invoke context
    :param filename: A filename to check.
    :param envdir: python environment dirs. We exclude these
    :param noglob: Disable globbing in the filename.
    """

    excludes = ['.git', 'env', 'venv']

    # If we are running in a virtualenv environment, ignore it.
    virtual_env = os.getenv('VIRTUAL_ENV', None)
    if virtual_env is not None:
        excludes.append(virtual_env)

    if isinstance(envdir, str):
        excludes.append(str)
    else:
        for x in envdir:
            excludes.append(x)

    command = 'flake8 --jobs=1 --exclude ' + ','.join(excludes)

    if filename is not None:
        if noglob:
            templates = [filename]
        else:
            templates = [x for x in glob.glob(filename)]
            if len(templates) == 0:
                print("File `{0}` not found".format(filename))
                exit(1)

        command += ' ' + " ".join(templates)

    print("Running command: '" + command + "'")
    exit_signal = os.system(command)
    if os.name == 'nt':
        exit_status = exit_signal
    else:
        exit_status = os.WEXITSTATUS(exit_signal)
    sys.exit(exit_status)
