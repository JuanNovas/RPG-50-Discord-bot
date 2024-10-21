import asyncio
import pytest
from bot import *

def test_get_token():
    try:
        get_token()
    except RuntimeError as e:
        pytest.fail(f"setup_bot raised an exception: {e}")
        
def test_load():
    assert asyncio.run(load("cogs/test")) == True
    with pytest.raises(FileNotFoundError):
        asyncio.run(load("cogs/example"))

def test_load_extensions():
    assert asyncio.run(load_extensions()) == True
