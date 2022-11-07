"""
Remove RDP entries from the registry
"""

import winreg


def main():
    while True:
        server_list = []
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Default', 0,
                                 winreg.KEY_ALL_ACCESS)
        serv_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Servers', 0,
                                  winreg.KEY_ALL_ACCESS)

        try:
            i = 0
            while True:
                server = winreg.EnumValue(reg_key, i)
                server_list.append([server[0], server[1]])
                i += 1
        except OSError:
            pass

        print('Found {} RDP entries'.format(len(server_list)))
        print("Please select the RDP entry you want to remove:")
        for i, server in enumerate(server_list):
            print('{}) {}'.format(i, server[1]))

        try:
            selection = int(input('Selection: '))
            if selection < 0 or selection > len(server_list):
                print('Invalid selection')
                continue
            print('Removing {}'.format(server_list[selection][1])),
            winreg.DeleteValue(reg_key, server_list[selection][0])
            try:
                if ":" in server_list[selection][1]:
                    server_name = server_list[selection][1].split(":")[0]
                else:
                    server_name = server_list[selection][1]
                winreg.DeleteKey(serv_key, server_name)
            except OSError:
                pass
            print('...done')
            print('____________________________________________________________')
        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    main()
