# -*- coding: utf-8 -*-

from ..zot import getToken
from .. import getConfigInfo

import logging
import pytest

log = logging.getLogger(__name__)


def test_authToken(configInfo):

    log.info(getToken(configInfo))
