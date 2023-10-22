import RemoteManager


rm = RemoteManager.RemoteManager("root", "192.168.1.41")
rm.copy_scripts_to_target()