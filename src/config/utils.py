def clean_allowed_hosts(str) -> list:
    """
    It get a string like '["host1", "host2"]' end return a list instead a string.'
    
    Args:
        str: str

    Returns:
        allowed_hosts: list
    """
    allowd_hosts = str.replace('[', '').replace(']', '').replace('"', '').replace("'", '')
    allowd_hosts = allowd_hosts.split(', ')
    return allowd_hosts