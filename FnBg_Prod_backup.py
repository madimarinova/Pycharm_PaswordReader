import  re

def get_file_list(file: str) -> list:
    """
    Opens the file indicated by the file argument, reads it and split the text into list.

    Args:
        file: <class 'str'> which represents teh file that we will aim to open

    Returns:
        <class 'list'> which gives the names and the configs of the systems as list
    """
    with open(file) as f:
        text = f.read()
        systems = text.split('############################\n')
    return systems


def sys_names(source: list) -> list:
    return re.findall(r"\b[A-Z][A-Z]+\b", str(source))
    #return [sys.replace('# ', '').replace('\n', '') for sys in source[1::2]]


def sys_confs(source: list) -> list:
    system_configs = [conf.replace('# ', '').replace('\n\n', '').replace('\n', ';') for conf in source[::2][1:]]
    system_configs[-1] = system_configs[-1][:-1]
    return system_configs


def config_dict(config: str) -> dict:
    sys_conf = dict()
    for conf in config.split(';'):
        (k, v) = conf.split(': ')
        sys_conf[k] = v
    return sys_conf


def sys_list(sys_names: list, sys_configs: list) -> list:
    system_dict = {}
    for  name, config in zip(sys_names, sys_configs):
        system = dict()
        system[name] = config_dict(config)

        for i,j in system.items():
            system_dict[i] = j

    #print(system_dict['BPM']["BPM_url"])
    return system_dict


def main(system, value) -> None:
    t = get_file_list('passwords_backup.py')
    s_names = sys_names(t)
    s_confs = sys_confs(t)
    all_systems = sys_list(s_names, s_confs)
    return all_systems[system][value]


if __name__ == '__main__':
    print(main("BPM","BPM_url"))

# import FnBg_Prod
# print(Fnbg_backup.main("BPM","BPM_url"))