# RemoteScriptManager

- **Author**: Sean Stolberg
- **Date**: October 21, 2023

## Description

This Python class, `RemoteScriptManager`, provides a set of methods for managing a workflow on remote Linux devices. It simplifies tasks such as copying and executing scripts on a remote device, and collecting logs. 

The class takes a `.yaml` config file in the constructor, then uses the values to copy any scripts specified to the target test device via `scp`, execute them via `ssh`, then copy any log files specified in the config back to the client machine we're running on. 

## Important Assumptions

- `RemoteScriptManager` relies on SSH and SCP, so it assumes that password-less SSH authentication is already configured between the client running this tool and the remote device.

## Configuration File Example
Here is an example of the `config.yml` file, passed to the constructor of RemoteScriptManager, with all the required fields filled in:

```yaml
user_config:
  user: 'root'
target_config:
  target: 192.168.1.41
ext_tool_config:
  scp_path: 'C:\Windows\System32\OpenSSH\scp.exe'
  ssh_path: 'C:\Windows\System32\OpenSSH\ssh.exe'
script_config:
  scripts_dir: 'scripts'
  scripts:
    - 'GetResourceInfo.sh'
log_config:
  target_logs_to_save:
    - '/var/log/resourceInfoLog.txt'
    - '/var/log/messages'
  destination_log_dir: 'logs'
```

## Example Script

The class works with scripts like `GetResourceInfo.sh`, which generates a summary (snapshot in time) of memory and disk usage, along with the CPU load at the time the script was run. Here's an example output:

```bash
2023-10-21 17:37:03 Memory Usage: 3208/3829MB (83.78%)
2023-10-21 17:37:03 Disk Usage: 43G/3.8GB (/)
2023-10-21 17:37:03 CPU Load: 0.08
```

## Usage
### Installation

1. Clone the repository: git clone https://github.com/seanstolberg/PythonProjects.git
2. Navigate to the project directory: cd RemoteScriptManager

## Usage Example
```python
from RemoteScriptManager import RemoteScriptManager

# Create a RemoteScriptManager instance with a configuration file path
rsm = RemoteScriptManager("config.yaml")

# Execute the workflow
rsm.execute()
```

## Class Methods
- **\_\_init\_\_(self, config: str)**: Initialize the RemoteScriptManager instance with a configuration file
- **ensure_target_script_dir(self)**: Ensure that the target script directory is created on the remote device
- **copy_scripts_to_target(self)**: Copy script files to the remote device.
- **make_scripts_executable(self)**: Make script files in the remote script directory executable.
- **run_scripts(self)**: Execute script files on the remote device.
- **pull_logs_from_target(self)**: Pull log files from the remote device to the local directory.
- **execute(self)**: Execute the complete workflow, including directory setup, copying scripts, making them executable, running scripts, and pulling logs.

