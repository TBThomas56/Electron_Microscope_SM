import subprocess
import sys

from cryoem_monitor import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "cryoem_monitor", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
