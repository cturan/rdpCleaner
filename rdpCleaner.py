import winreg


def remove_rdp_entry(server_name: str):
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Default', 0, winreg.KEY_ALL_ACCESS) as default_key:
        winreg.DeleteValue(default_key, server_name)

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Servers', 0, winreg.KEY_ALL_ACCESS) as servers_key:
        try:
            winreg.DeleteKey(servers_key, server_name)
        except OSError:
            pass


def list_rdp_entries():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Default', 0, winreg.KEY_ALL_ACCESS) as default_key:
        try:
            i = 0
            while True:
                server_name, server_ip, _ = winreg.EnumValue(default_key, i)
                print('{}) {} ({})'.format(i, server_name, server_ip))
                i += 1
        except OSError:
            pass


def main():
    while True:
        list_rdp_entries()

        try:
            selection = int(input('Select the RDP entry to remove (or enter -1 to exit): '))
            if selection < 0:
                break

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Terminal Server Client\\Default', 0, winreg.KEY_ALL_ACCESS) as default_key:
                server_name, _, _ = winreg.EnumValue(default_key, selection)

            print('Removing {}...'.format(server_name))
            remove_rdp_entry(server_name)
            print('...done')
        except (ValueError, OSError) as e:
            print('Error:', e)


if __name__ == '__main__':
    main()
