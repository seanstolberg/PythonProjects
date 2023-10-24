"""Module providing unit test functionality for python"""

import pytest
from pathlib import Path
from testautomationtools.remotescriptmanager import RemoteScriptManager

@pytest.fixture
def rsm():
    """
    Fixture to create a RemoteScriptManager instance for testing.

    Returns:
        RemoteScriptManager: An instance of RemoteScriptManager.
    """
    test_config = str(Path.joinpath(Path(__file__).parent, "test_config.yml"))
    return RemoteScriptManager(test_config)

def test_constructor_default_values(rsm: RemoteScriptManager):
    """
    Test the constructor of the RemoteScriptManager with default values.

    Args:
        rsm (RemoteScriptManager): An instance of RemoteScriptManager.

    Raises:
        AssertionError: If any assertion fails.
    """
    # Define expected values for attributes
    exp_user = "user1"
    exp_target = "myTarget"
    exp_scp_path = "myPath/scp.exe"
    exp_ssh_path = "myPath/ssh.exe"
    exp_scripts_dir = "scripts"
    exp_scripts = ["GetResourceInfo.sh"]
    exp_target_logs_to_save = [
        "/var/log/resourceInfoLog.txt", "/var/log/messages"]
    exp_destination_log_dir = "logs"

    # Perform assertions to check if attributes match expected values
    assert isinstance(rsm, RemoteScriptManager)
    assert rsm.user == exp_user, f"Expected self.user to be {exp_user}, but was {rsm.user}"
    assert rsm.target == exp_target, f"Expected self.target to be {exp_target}, but was {rsm.target}"
    assert rsm.scp_path == exp_scp_path, f"Expected self.scp_path to be {exp_scp_path}, but was {rsm.scp_path}"
    assert rsm.ssh_path == exp_ssh_path, f"Expected self.ssh_path to be {exp_ssh_path}, but was {rsm.ssh_path}"
    assert rsm.scripts_dir == exp_scripts_dir, f"Expected self.scripts_dir to be {exp_scripts_dir}, but was {rsm.scripts_dir}"
    assert_lists_are_equal(exp_scripts, rsm.scripts)
    rsm.target_logs_to_save.sort()
    exp_target_logs_to_save.sort()
    assert_lists_are_equal(exp_target_logs_to_save, rsm.target_logs_to_save)
    assert rsm.destination_log_dir == exp_destination_log_dir, f"Expected self.destination_log_dir to be {exp_destination_log_dir}, but was {rsm.destination_log_dir}"

def test_constructor_null_user():
    """
    Test the constructor of the RemoteScriptManager with a null user configuration.

    Raises:
        ValueError: If RemoteScriptManager is instantiated with a None config.
    """
    with pytest.raises(ValueError):
        RemoteScriptManager(None)

def assert_lists_are_equal(expList, actList):
    """
    Utility function to assert that two lists are equal, disregarding order.

    Args:
        expList (list): The expected list.
        actList (list): The actual list.

    Raises:
        AssertionError: If the lists are not equal.
    """
    actList.sort()
    expList.sort()
    assert actList == expList, f"Expected list to be {expList}, but was {actList}"
