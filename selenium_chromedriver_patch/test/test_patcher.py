from re import sub
from unittest.mock import mock_open, patch as mock_patch
from ..settings import (
    SELENIUM_MARKER, CDC_VALUE_LENGTH)
from ..patcher import (
    gen_random_cdc, is_binary_patched, patch)


def test_gen_random_cdc_proper_length():
    cdc = gen_random_cdc()
    assert len(cdc) == CDC_VALUE_LENGTH


def test_gen_random_cdc_not_contain_marker():
    cdc = gen_random_cdc()
    assert not cdc.decode().startswith(SELENIUM_MARKER)


def test_is_binary_patched_with_not_patched_string(mocker):
    cdc = gen_random_cdc()
    cdc = sub(r'\w{3}(.*)', r'cdc\g<1>', cdc.decode()).encode()
    with mock_patch('io.open', mock_open(read_data=cdc)):
        result = is_binary_patched(cdc)
        assert result is False


def test_is_binary_patched_with_patched_string(mocker):
    cdc = gen_random_cdc()
    with mock_patch('io.open', mock_open(read_data=cdc)):
        result = is_binary_patched(cdc)
        assert result is True


def test_patch_with_unpatched_file():
    cdc = gen_random_cdc()
    cdc = sub(r'\w{3}(.*)', r'cdc\g<1>', cdc.decode()).encode()
    with mock_patch('io.open', mock_open(read_data=cdc)):
        result = patch(cdc)
        assert result is True


def test_patch_with_patched_file():
    cdc = gen_random_cdc()
    with mock_patch('io.open', mock_open(read_data=cdc)):
        result = patch(cdc)
        assert result is False
