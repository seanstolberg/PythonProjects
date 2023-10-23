from pathlib import Path
"""Module providing unit test functionality for python"""
import pytest
from testautomationtools.remotescriptmanager import RemoteScriptManager

@pytest.fixture
def rsm():
    """
    _summary_

    Returns:
        _type_: _description_
    """
    test_config = str(Path.joinpath(Path(__file__).parent, "test_config.yml"))
    return RemoteScriptManager(test_config)

def test_constructor_default_values(rsm):
    """
    _summary_
    """
    exp_user = "user1"
    exp_target = "myTarget"
    exp_scp_path = "myPath/scp.exe"
    exp_ssh_path = "myPath/ssh.exe"
    exp_scripts_dir ="scripts"
    exp_scripts = ["GetResourceInfo.sh"]
    exp_target_logs_to_save = ["/var/log/resourceInfoLog.txt", "/var/log/messages"]
    exp_destination_log_dir = "logs"
    
    assert isinstance(rsm, RemoteScriptManager)
    assert rsm.user == exp_user, f"Expected self.user to be {exp_user}, but was {rsm.user}"

def test_constructor_null_user():
    """
    _summary_
    """
    with pytest.raises(ValueError):
        RemoteScriptManager(None)