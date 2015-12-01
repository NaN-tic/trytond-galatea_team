# This file is part of the galatea_team module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class GalateaTeamTestCase(ModuleTestCase):
    'Test Galatea Team module'
    module = 'galatea_team'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        GalateaTeamTestCase))
    return suite