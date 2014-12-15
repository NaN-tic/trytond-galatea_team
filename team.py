# This file is part galatea_team module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.cache import Cache
from .tools import slugify
from datetime import datetime

__all__ = ['GalateaTeam', 'GalateaTeamWebSite']


class GalateaTeam(ModelSQL, ModelView):
    "Galatea Team"
    __name__ = 'galatea.team'
    name = fields.Char('Name', required=True, on_change=['name', 'slug'])
    slug = fields.Char('slug', required=True, translate=True,
        help='Cannonical uri.')
    avatar = fields.Binary('Avatar')
    description = fields.Text('Description', required=True, translate=True,
        help='You could write wiki markup to create html content. Formats text following '
        'the MediaWiki (http://meta.wikimedia.org/wiki/Help:Editing) syntax.')
    long_description = fields.Text('Long Description', translate=True,
        help='You could write wiki markup to create html content. Formats text following '
        'the MediaWiki (http://meta.wikimedia.org/wiki/Help:Editing) syntax.')
    metadescription = fields.Char('Meta Description', translate=True, 
        help='Almost all search engines recommend it to be shorter ' \
        'than 155 characters of plain text')
    metakeywords = fields.Char('Meta Keywords',  translate=True,
        help='Separated by comma')
    metatitle = fields.Char('Meta Title',  translate=True)
    active = fields.Boolean('Active',
        help='Dissable to not show content team.')
    websites = fields.Many2Many('galatea.team-galatea.website', 
        'team', 'website', 'Websites',
        help='Team will be available in those websites')

    @staticmethod
    def default_active():
        return True

    @staticmethod
    def default_websites():
        Website = Pool().get('galatea.website')
        return [p.id for p in Website.search([('registration','=',True)])]

    @classmethod
    def __setup__(cls):
        super(GalateaTeam, cls).__setup__()
        cls._order.insert(0, ('name', 'ASC'))
        cls._error_messages.update({
            'delete_teams': ('You can not delete '
                'teams because you will get error 404 NOT Found. '
                'Dissable active field.'),
            })

    def on_change_name(self):
        res = {}
        if self.name and not self.slug:
            res['slug'] = slugify(self.name)
        return res

    @classmethod
    def copy(cls, teams, default=None):
        new_teams = []
        for team in teams:
            default['slug'] = '%s-copy' % team.slug
            new_team, = super(GalateaTeam, cls).copy([team], default=default)
            teams.append(new_team)
        return new_teams

    @classmethod
    def delete(cls, teams):
        cls.raise_user_error('delete_teams')


class GalateaTeamWebSite(ModelSQL):
    'Galatea Team - Website'
    __name__ = 'galatea.team-galatea.website'
    _table = 'galatea_team_galatea_website'
    team = fields.Many2One('galatea.team', 'Team', ondelete='CASCADE',
            select=True, required=True)
    website = fields.Many2One('galatea.website', 'Website', ondelete='RESTRICT',
            select=True, required=True)
