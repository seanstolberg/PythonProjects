"""Module providing unit test functionality for python"""
import pytest
from RemoteManager.RemoteScriptManager import RemoteScriptManager

@pytest.fixture
def rsm():
    """
    _summary_

    Returns:
        _type_: _description_
    """
    return RemoteScriptManager(r"C:\Users\seans\Documents\GitHub\PythonProjects\RemoteLinuxTool\Tests\test_config.yml")

def test_constructor_default_values():
    """
    _summary_
    """
    this_rsm = RemoteScriptManager(r"C:\Users\seans\Documents\GitHub\PythonProjects\RemoteLinuxTool\Tests\test_config.yml")
    assert isinstance(this_rsm, RemoteScriptManager)
    # assert thisRsm.scp_path == RemoteScriptManager.defaultScpExe
    # assert thisRsm.sshExe == RemoteScriptManager.defaultSshExe
    # assert thisRsm.scriptsDir == RemoteScriptManager.defaultScriptsDir
    # assert thisRsm.getResourceInfoScript == RemoteScriptManager.defaultGetResourceInfoScript
    # assert thisRsm.log_resourceInfo == RemoteScriptManager.defaultLog_resourceInfo
    # assert thisRsm.log_system == RemoteScriptManager.defaultLog_system
    # assert thisRsm.logPullList == RemoteScriptManager.defaultLogPullList
    # assert thisRsm.scp_path == RemoteScriptManager.defaultScpExe
    # assert thisRsm.sshExe == RemoteScriptManager.defaultSshExe
    # assert thisRsm.scriptsDir == RemoteScriptManager.defaultScriptsDir
    # assert thisRsm.getResourceInfoScript == RemoteScriptManager.defaultGetResourceInfoScript
    # assert thisRsm.log_resourceInfo == RemoteScriptManager.defaultLog_resourceInfo
    # assert thisRsm.log_system == RemoteScriptManager.defaultLog_system
    # assert thisRsm.logPullList == RemoteScriptManager.defaultLogPullList    

def test_constructor_null_user():
    """
    _summary_
    """
    with pytest.raises(ValueError):
        RemoteScriptManager(None)
        
def test_execute():
    """
    _summary_
    """
    this_rsm = RemoteScriptManager(r"C:\Users\seans\Documents\GitHub\PythonProjects\RemoteLinuxTool\Tests\test_config.yml")
    this_rsm.execute()