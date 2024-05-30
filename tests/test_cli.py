import subprocess
import sys

from EM_Monitoring_System import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "EM_Monitoring_System", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
