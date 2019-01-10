import json
import pytest
import logging
import requests
from requests import codes


log = logging.getLogger(__name__)


def getToken(configInfo):

    log.info(configInfo)

    hubzillaToken = requests.get(configInfo['ZOTBASE'] + 'authorize/', auth=(configInfo[
        'USERNAME'], configInfo['PASSWORD']))

    log.info(hubzillaToken.request.url)
    log.info(hubzillaToken.status_code)
    # log.info(hubzillaToken.text)

    return hubzillaToken.text
