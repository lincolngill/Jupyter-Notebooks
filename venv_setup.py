#!/usr/bin/env python
from venv import create
import os
from subprocess import run
import logging
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.INFO)
    script_path = os.path.dirname(os.path.realpath(__file__))
    venv_path = os.path.join(script_path, '.venv')
    if os.path.exists(venv_path):
        logger.warning("Virtual env {p} already exists. Not recreated.".format(p=venv_path))
    else:
        logger.info("Creating virtual env {p}...".format(p=venv_path))
        create(venv_path, with_pip=True)
    pip_path = os.path.join(venv_path, 'Scripts', 'pip')
    req_path = os.path.join(script_path, 'requirements.txt')
    req_needed = False
    try:
        import jupyterlab
    except ImportError:
        req_needed = True
    if req_needed:
        logger.info("Installing requirements.txt...")
        run([pip_path, "install", "-r", req_path], cwd=script_path)
        run([pip_path, "list"], cwd=script_path)
    else:
        logger.warning("Jupyter Lab already installed. Pip requirements install not run.")
    logger.info('Done')

if __name__ == '__main__':
    main()