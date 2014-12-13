# This file is part galatea_team module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .team import *

def register():
    Pool.register(
        GalateaTeam,
        GalateaTeamWebSite,
        module='galatea_team', type_='model')
