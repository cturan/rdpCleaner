# RDP Entry Remover

This script allows you to remove Remote Desktop Protocol (RDP) entries from the registry of a computer running the Windows operating system.

## Usage

To use the script, run the following command:

python rdp_entry_remover.py



The script will display a list of the RDP entries that it finds in the registry. You can then select the entry that you want to remove by entering the corresponding number. The script will then remove the selected entry from the registry.

You can repeat this process to remove multiple entries if desired. To exit the script, enter -1 when prompted to select an entry.

## Requirements

- Python 3
- The `winreg` module (included with the standard library in Python 3)
