# -*- coding: utf-8 -*-

from ..zot import getToken
from .. import getConfigInfo

import logging
import pytest

log = logging.getLogger(__name__)


def test_configInfo(configInfo):

    log.info(getConfigInfo(configInfo))
