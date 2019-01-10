import pytest
import logging
import configparser


log = logging.getLogger(__name__)


def getMastodonConfig():
    config = configparser.ConfigParser()
    log.info(config.sections())

    config.read('../config.ini')

    log.info(config.sections())
