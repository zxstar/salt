# -*- coding: utf-8 -*-

# Import python libs
from __future__ import absolute_import, print_function, unicode_literals

import pytest

# Import Salt Testing libs
from tests.support.case import ModuleCase
from tests.support.helpers import requires_salt_modules


@pytest.mark.skip_if_not_root
@requires_salt_modules("rabbitmq")
class RabbitModuleTest(ModuleCase):
    """
    Validates the rabbitmqctl functions.
    To run these tests, you will need to be able to access the rabbitmqctl
    commands.
    """

    def test_user_exists(self):
        """
        Find out whether a user exists.
        """
        ret = self.run_function("rabbitmq.user_exists", ["null_user"])
        self.assertEqual(ret, False)
