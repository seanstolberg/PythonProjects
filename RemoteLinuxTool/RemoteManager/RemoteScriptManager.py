
# Build a script that
# Copies a script over to a remote Linux machine,
# runs it,
# then collects /var/messages log from the machine as well as the output from the script.
# The script should take process measurements around memory, disk, and cpu usage.
import subprocess
import os
from pathlib import Path
import configparser


class RemoteScriptManager:
    """
    Author: Sean Stolberg
    Date: 10/21/2023
    
    Description:
    This class implements methods to support a basic workflow where 1 to many remote Linux devices exist
    and the user needs to iterate on the following workflow.
    
    1. Copy one or more test scripts to the remote Linux device
    2. Execute the test scripts on the remote Linux device
    3. When the test scripts are done executing, collect the logs created by the scripts and
       the system log from /var/log/messages
    4. Create a summary of any error messages encountered
    
    Important Assumptions:
    
    * RemoteScriptManager using both ssh and scp and thus requires that passwordless ssh is already setup between the client
    running this tool and the remote device/machine.
    
    Scripts used:
    
    1. GetResourceInfo.sh - Generates a summary (snapshot in time) of the memory and disk usage, 
       along with the CPU load at the time the script was run
       
        Example output:
       
        2023-10-21 17:37:03 Memory Usage: 3208/3829MB (83.78%)
        2023-10-21 17:37:03 Disk Usage: 43G/3.8GGB (/)
        2023-10-21 17:37:03 CPU Load: 0.08

    """    

    # Class Variables
    defaultScpExe = "C:\Windows\System32\OpenSSH\scp.exe"
    sshExe = "C:\Windows\System32\OpenSSH\ssh.exe"
    scriptsDir = "scripts"
    getResourceInfoScript = "GetResourceInfo.sh"
    log_resourceInfo = "/var/log/resourceInfoLog.txt"
    log_system = "/var/log/messages"
    logPullList = [log_resourceInfo, log_system]

    def __init__(self, user: str, target: str, config: str = None):
    
        self.validateInputs(user, target)
        self.validateConfig(config)
        self.user = user
        self.target = target
        self.sshTarget = f"{self.user}@{self.target}"
        self.baseScriptDir_as_posix = Path.joinpath(Path(f"/{self.user}"), self.scriptsDir).as_posix()

    def validateInputs(self, user, target):
        if user is None or not isinstance(user, str) or user.strip() == "":
            raise ValueError("Initialization variable 'user' must be a non-null or empty string value.")
        if target is None or not isinstance(target, str) or target.strip() == "":
            raise ValueError("Initialization variable 'target' must be a non-null or empty string value.")
        
    def validateConfig(self, config):
        if  config is not None and isinstance(config, str) and config.strip() != "" and os.path.exists(config):
            myConfig = configparser.ConfigParser()
            myConfig.read(config)
            
            scpExe = myConfig.get('ToolConfigs', 'scpExe')
            if(scpExe):
                self.defaultScpExe = scpExe if scpExe else self.defaultScpExe

    def ensure_target_script_dir(self):
        print(f"Ensure target script directory {self.baseScriptDir_as_posix} is created.")
        subprocess.run(
            [self.sshExe, self.sshTarget, f"mkdir -p {self.baseScriptDir_as_posix}"])

    def copy_scripts_to_target(self):
        destScriptPath = f"{self.sshTarget}:{Path.joinpath(Path(self.baseScriptDir_as_posix), self.getResourceInfoScript).as_posix()}"
        localScriptPath = Path.joinpath(
            Path(os.getcwd()), "RemoteLinuxTool", self.scriptsDir, self.getResourceInfoScript)
        print(f"Copying {localScriptPath} to destination {destScriptPath}")
        subprocess.run([self.defaultScpExe, localScriptPath, destScriptPath])

    def make_scripts_executable(self):
        command = f"find {self.baseScriptDir_as_posix} -type f -name \"*.sh\" -exec chmod +x {{}} \;"
        print(f"Making all scripts in {self.baseScriptDir_as_posix} executable")
        subprocess.run([self.sshExe, self.sshTarget, command])

    def run_script(self):
        command = "./scripts/GetResourceInfo.sh"
        print(f"Running command: {command}")
        subprocess.run([self.sshExe, self.sshTarget, command])

    def pull_logs_from_target(self):
        # newpath = r'C:\Program Files\arbitrary'
        # if not os.path.exists(newpath):
        #     os.makedirs(newpath)

        for log in self.logPullList:
            print(f"Pulling logs from: {log}")
            fileName = log.split("/")[-1]
            subprocess.run([self.defaultScpExe, f"{self.sshTarget}:{log}", fileName])


    def execute(self):
        self.ensure_target_script_dir()
        self.copy_scripts_to_target()
        self.make_scripts_executable()
        self.run_script()
        self.pull_logs_from_target()
        
rm = RemoteScriptManager("root", "192.168.1.41", r"C:\Users\seans\OneDrive\VSCodeProjects\RemoteLinuxTool\config.ini")
rm.execute()

