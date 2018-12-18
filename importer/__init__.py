import pytest
import logging


log = logging.getLogger(__name__)


def getConfigInfo(configInfo):

    log.debug(configInfo)

    configInfo = [configInfo['ZOTBASE'], configInfo[
        'USERNAME'], configInfo['PASSWORD']]

    return configInfo
