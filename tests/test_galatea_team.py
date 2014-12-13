#!/usr/bin/env python
# This file is part galatea_team module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class GalateaTeamTestCase(unittest.TestCase):
    'Test Galatea Team module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('galatea_team')

    def test0005views(self):
        'Test views'
        test_view('galatea_team')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        GalateaTeamTestCase))
    return suite
