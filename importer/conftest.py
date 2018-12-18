import pytest
from pathlib import Path
import logging
import configparser

log = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def configInfo(pytestconfig):
    global data
    global reporting

    p = Path.cwd()
    log.info(p.parent)

    configLoc = Path('config.ini')  # pytestconfig.getoption('--CONFIG')

    loc = p.joinpath(configLoc)
    #assert loc.exists() is True
    #assert loc.is_dir() is False

    log.info(configLoc.parent)

    config = configparser.ConfigParser()
    print()
    config.read(configLoc)  # local config file
    # log.info(repr(config.sections()))
    configData = config['AUTH-CONFIG']

    return configData
