import json
import pytest
import logging
import requests
from requests import codes


log = logging.getLogger(__name__)


def getToken(configInfo):

    log.info(configInfo)

    hubzillaToken = [configInfo['ZOTBASE'], configInfo[
        'USERNAME'], configInfo['PASSWORD']]

    # hubzillaToken = requests.get(configInfo['ZOTBASE'], username=configInfo[
    #                            'USERNAME'], password = configInfo['PASSWORD'])

    # log.info(hubzillaToken.request.url)

    return hubzillaToken
