"""Test the misc module.
"""
import subprocess as sp
sp.run("sudo apt-get update", shell=True, check=True)


def test_nomachine():
    """Test installing and configuring NoMachine.
    """
    cmd = "xinstall nomachine"
    sp.run(cmd, shell=True, check=True)


def test_version():
    """Test the version command.
    """
    cmd = "xinstall version"
    sp.run(cmd, shell=True, check=True)
