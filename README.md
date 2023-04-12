# RDP Entry Remover

This script allows you to remove Remote Desktop Protocol (RDP) entries from the registry of a computer running the Windows operating system.

## Usage

To use the script, run the following command:

`python rdpCleaner.py`



The script will display a list of the RDP entries that it finds in the registry. You can then select the entry that you want to remove by entering the corresponding number. The script will then remove the selected entry from the registry.

You can repeat this process to remove multiple entries if desired. To exit the script, enter -1 when prompted to select an entry.


## GUI

![screen](https://user-images.githubusercontent.com/388283/231329289-a93997a4-153b-4c3c-bb06-a44c60f89905.png)



## Requirements

- Python 3
- The `winreg` module (included with the standard library in Python 3)
