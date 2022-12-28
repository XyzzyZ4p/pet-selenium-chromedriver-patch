"""
patcher
=======
The core module of selenium_chromedriver_patch
"""
import io
from os import PathLike
from random import choices
from string import ascii_lowercase
from re import sub
from tqdm import tqdm
from selenium_chromedriver_patch.settings import SELENIUM_MARKER, CDC_VALUE_LENGTH


__all__ = ('gen_random_cdc', 'is_binary_patched', 'patch')


def gen_random_cdc() -> bytes:
    """Generate random encoded cdc value.

    :return: Random encoded cdc value
    :rtype: str
    """
    while True:
        cdc = choices(ascii_lowercase, k=CDC_VALUE_LENGTH)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        if not "".join(cdc[0:3]).startswith(SELENIUM_MARKER):
            break
    return "".join(cdc).encode()


def is_binary_patched(
        executable_path:
        str | bytes | PathLike[str] | PathLike[bytes] | int) -> bool:
    """Check if executable is patched.

    :param executable_path: The chromedriver location
    :type executable_path: str | bytes | PathLike[str] | PathLike[bytes] | int

    :return: False if not patched, else True
    :rtype: bool
    """
    with io.open(executable_path, "rb") as fh:
        for line in iter(lambda: fh.readline(), b""):
            if b"cdc_" in line:
                return False
        else:
            return True


def patch(
        executable_path:
        str | bytes | PathLike[str] | PathLike[bytes] | int) -> bool:
    """
    Patches the ChromeDriver binary

    :param executable_path: The chromedriver location
    :type executable_path: str | bytes | PathLike[str] | PathLike[bytes] | int

    :return: False on failure, True on success
    :rtype: bool
    """
    replacement = gen_random_cdc()
    changed = False
    with io.open(executable_path, "r+b") as fh:
        for line in tqdm(iter(lambda: fh.readline(), b"")):
            if b"cdc_" in line:
                fh.seek(-len(line), 1)
                newline = sub(b"cdc_.{22}", replacement, line)
                fh.write(newline)
                changed = True
    return changed
