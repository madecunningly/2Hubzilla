# -*- coding: utf-8 -*-

from ..activity_pub import getToken
from .. import getConfigInfo

import logging
import pytest

log = logging.getLogger(__name__)


def test_configInfo(configInfo):

    log.info(getConfigInfo(configInfo))
