#!/usr/bin/env python
"""Jupyter Notebook python virtual env setup
Creates a python virtual environment ".venv" in this scripts directory.
Uses pip to install Jupyter Lab and other required packages specified in requirements.txt (located in this scripts directory).

Won't create the virtual environment if the directory for it already exists.
Won't install requirements.txt packages if jupyterlab is already installed.
"""
from venv import create
import os
from subprocess import run
import logging
logger = logging.getLogger(__name__)

script_path = os.path.dirname(os.path.realpath(__file__))
venv_path = os.path.join(script_path, '.venv')

def create_venv():
    if os.path.exists(venv_path):
        logger.warning("Virtual env {p} already exists. Not recreated.".format(p=venv_path))
    else:
        logger.info("Creating virtual env {p}...".format(p=venv_path))
        create(venv_path, with_pip=True)

def install_pkgs():
    venv_bin_dir = 'bin'
    if os.name == 'nt':
        # Windows has executables in "Scripts" directory rather than "bin"
        venv_bin_dir = 'Scripts'
    pip_path = os.path.join(venv_path, venv_bin_dir, 'pip')
    req_path = os.path.join(script_path, 'requirements.txt')
    if run([pip_path, "-q", "--require-virtualenv", "show", "jupyterlab"], cwd=script_path).returncode == 0:
        logger.warning("Jupyter Lab already installed. Pip requirements install not run.")
    else:
        logger.info("Installing requirements.txt...")
        run([pip_path, "install", "-r", req_path], cwd=script_path)
        run([pip_path, "list"], cwd=script_path)

def main():
    logging.basicConfig(level=logging.INFO)
    create_venv()
    install_pkgs()
    logger.info('Done')

if __name__ == '__main__':
    main()