"""Version utils."""


from functools import lru_cache

from awesomeversion import AwesomeVersion, AwesomeVersionException


@lru_cache(maxsize=1024)
def version_left_higher_then_right(left: str, right: str) -> bool:
    """Return a bool if source is newer than target, will also be true if identical."""
    try:
        return AwesomeVersion(left) > AwesomeVersion(right)
    except (AwesomeVersionException, AttributeError):
        return False


def version_left_higher_or_equal_then_right(left: str, right: str) -> bool:
    """Return a bool if source is newer than target, will also be true if identical."""
    if left == right:
        return True
    try:
        return version_left_higher_then_right(left, right)
    except (AwesomeVersionException, AttributeError):
        return False
