import os
import sys
import logging
import traceback
from datetime import datetime

import click
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def init_logging(context=None, debug=False, log_level=logging.INFO):
    logger = logging.getLogger()

    if context:
        formatter = logging.Formatter('[%(asctime)s] {} %(name)s %(levelname)s %(message)s'.format(context))
    else:
        formatter = logging.Formatter('[%(asctime)s] %(name)s %(levelname)s %(message)s')

    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if debug:
        log_level = logging.DEBUG

    logger.setLevel(log_level)

    def exception_handler(*exc_info):
        text = "".join(traceback.format_exception(*exc_info))
        logger.error("Unhandled exception: %s", text)

    sys.excepthook = exception_handler

@click.group()
def main():
    pass

## TODO: fix help order
## TODO: create sub command group for secrets? for pipelines? for projects/instances?

@main.command('init', help='Initalize a singer-cloud instance')
@click.argument('config-path')
@click.option('--debug', is_flag=True)
def init(config_path, debug):
    pass

@main.command('new-pipeline', help='Create a new pipeline configuration. Prompts the user to select from existing taps and targets, or installing new ones on the fly. Walks through default config values, if possible to do so with click')
@click.argument('pipeline-name')
@click.option('--debug', is_flag=True)
def new_pipeline(pipeline_name, debug):
    pass

@main.command('install-tap', help='Creates configuration for a new tap and installs it')
@click.argument('tap-name')
@click.argument('package-reference')
@click.option('--debug', is_flag=True)
def install_tap(tap_name, package_reference):
    pass

# TODO: commands install-target, uninstall-tap, and uninstall-target


@main.command('push', help='Update a singer-cloud instance from the local configuration')
@click.option('--catalogs', is_flag=True) # add flag to include the catalog in the push
@click.option('--states', is_flag=True) # add flag to include the states in the push
@click.option('--debug', is_flag=True)
def push(catalogs, states, debug):
    from singer_cloud.docker import sync_container_image

    with open(config_path) as file:
        config = load(file, Loader=Loader)

    ## TODO: validate config

    sync_container_image(config)

@main.command('pull', help='Update the local configuration from the singer-cloud instance')
@click.option('--catalogs', is_flag=True) # add flag to include the catalog in the pull
@click.option('--states', is_flag=True) # add flag to include the states in the pull
def pull(catalogs, states, debug):
    pass

@main.command('discover', help='Discover the tap catalog for a Singer pipeline')
@click.argument('pipeline-name')
@click.option('--debug', is_flag=True)
def discover(pipeline_name, debug):
    pass

@main.command('secret-put', help='Create or update a secret')
@click.argument('secret-path')
@click.argument('secret-value')
@click.option('--debug', is_flag=True)
def secret_put(debug):
    pass

@main.command('secret-get', help='Retrieve a secret')
@click.argument('secret-path')
@click.option('--debug', is_flag=True)
def secret_get(debug):
    pass

@main.command('secret-delete', help='Delete a secret')
@click.argument('secret-path')
@click.option('--debug', is_flag=True)
def secret_delete(debug):
    pass

@main.command('run-pipeline', help='Manually trigger a Singer pipeline')
@click.argument('config-path')
@click.argument('pipeline-name')
@click.option('--cloud', is_flag=True) # if specified, run in cloud. Otherwise run locally
@click.option('--debug', is_flag=True)
def run_pipeline(config_path, pipeline_name, cloud, debug):
    pass
