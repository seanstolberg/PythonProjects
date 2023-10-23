import subprocess
import os
from pathlib import Path
import yaml


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

    * RemoteScriptManager using both ssh and scp and thus requires that password-less ssh is already setup between the client
    running this tool and the remote device/machine.

    Scripts used:

    1. GetResourceInfo.sh - Generates a summary (snapshot in time) of the memory and disk usage, 
       along with the CPU load at the time the script was run

        Example output:

        2023-10-21 17:37:03 Memory Usage: 3208/3829MB (83.78%)
        2023-10-21 17:37:03 Disk Usage: 43G/3.8GGB (/)
        2023-10-21 17:37:03 CPU Load: 0.08

    """
    def __init__(self, config: str):
        if (config is None or not isinstance(config, str) or config.strip() == ""):
            raise ValueError(
                "config must be a non-null or empty string value.")

        with open(config, 'r') as f:
            this_config = yaml.safe_load(f)

        self.user = this_config["user_config"]["user"]
        self.target = this_config["target_config"]["target"]
        self.scp_path = this_config["ext_tool_config"]["scp_path"]
        self.ssh_path = this_config["ext_tool_config"]["ssh_path"]
        self.scripts_dir = this_config["script_config"]["scripts_dir"]
        self.scripts = this_config["script_config"]["scripts"]
        self.target_logs_to_save = this_config["log_config"]["target_logs_to_save"]
        self.destination_log_dir = this_config["log_config"]["destination_log_dir"]
        self.ssh_target = f"{self.user}@{self.target}"
        self.base_script_dir_as_posix = Path.joinpath(
             Path(f"/{self.user}"), self.scripts_dir).as_posix()

    def ensure_target_script_dir(self):
        print(
            f"Ensure target script directory {self.base_script_dir_as_posix} is created.")
        subprocess.run(
            [self.ssh_path, self.ssh_target, f"mkdir -p {self.base_script_dir_as_posix}"])

    def copy_scripts_to_target(self):
        for script in self.scripts:            
            destScriptPath = f"{self.ssh_target}:{Path.joinpath(Path(self.base_script_dir_as_posix), script).as_posix()}"
            localScriptPath = Path.joinpath(
                Path(os.getcwd()), self.scripts_dir, script)
            print(f"Copying {localScriptPath} to destination {destScriptPath}")
            subprocess.run([self.scp_path, localScriptPath, destScriptPath])

    def make_scripts_executable(self):
        command = f"find {self.base_script_dir_as_posix} -type f -name \"*.sh\" -exec chmod +x {{}} \;"
        print(
            f"Making all scripts in {self.base_script_dir_as_posix} executable")
        subprocess.run([self.ssh_path, self.ssh_target, command])

    def run_scripts(self):
        for script in self.scripts:
            command = "./scripts/" + script
            print(f"Running command: {command}")
            subprocess.run([self.ssh_path, self.ssh_target, command])

    def pull_logs_from_target(self):
        destinationPath = Path(self.destination_log_dir)
        if not os.path.exists(destinationPath):
            os.makedirs(destinationPath)

        for log in self.target_logs_to_save:
            print(f"Pulling logs from: {log}")
            fileName = log.split("/")[-1]
            
            subprocess.run(
                [self.scp_path, f"{self.ssh_target}:{log}",  Path.joinpath(Path(self.destination_log_dir), fileName)])

    def execute(self):
        self.ensure_target_script_dir()
        self.copy_scripts_to_target()
        self.make_scripts_executable()
        self.run_scripts()
        self.pull_logs_from_target()

this_rsm = RemoteScriptManager(r"C:\Users\seans\Documents\GitHub\PythonProjects\RemoteLinuxTool\Tests\test_config.yml")
this_rsm.execute()