assert 'BRUO:1234'.removeprefix("BRUO:") == "1234"
assert 'BRUO:1234:stuff:stuff'.removesuffix(":stuff") == "BRUO:1234:stuff"  # different to rstrip