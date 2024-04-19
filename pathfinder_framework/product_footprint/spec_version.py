class SpecVersion:
    def __init__(self, version):
        if not isinstance(version, int):
            raise ValueError("Version must be an integer")
        if version < 0 or version > 2**31 - 1:
            raise ValueError("Version must be in the range of 0 to 2^31-1")
        self.version = version

    def __eq__(self, other):
        return self.version == other.version

    def __repr__(self):
        return f"SpecVersion({self.version})"
