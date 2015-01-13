# This file is part galatea_team module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.config import config
from trytond.cache import Cache
from .tools import slugify
from datetime import datetime
from mimetypes import guess_type
import os
import hashlib

__all__ = ['GalateaTeam', 'GalateaTeamWebSite']
IMAGE_TYPES = ['image/jpeg', 'image/png',  'image/gif']


class GalateaTeam(ModelSQL, ModelView):
    "Galatea Team"
    __name__ = 'galatea.team'
    name = fields.Char('Name', required=True, on_change=['name', 'slug'])
    slug = fields.Char('slug', required=True, translate=True,
        help='Cannonical uri.')
    avatar = fields.Function(fields.Binary('Avatar', filename='file_name'), 'get_image',
        setter='set_image')
    avatar_path = fields.Function(fields.Char('Avatar Path'), 'get_avatarpath')
    file_name = fields.Char('File Name', required=True)
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

    @staticmethod
    def _create_team_dir():
        db_name = Transaction().cursor.dbname
        directory = os.path.join(config.get('database', 'path'), db_name)
        if not os.path.isdir(directory):
            os.makedirs(directory, 0770)
        directory = os.path.join(directory, 'team')
        if not os.path.isdir(directory):
            os.makedirs(directory, 0770)

    @classmethod
    def __setup__(cls):
        super(GalateaTeam, cls).__setup__()
        cls._order.insert(0, ('name', 'ASC'))
        cls._error_messages.update({
            'delete_teams': ('You can not delete teams because you will get error ' \
                '404 NOT Found. Dissable active field.'),
            'not_file_mime': ('Not know file mime "%(file_name)s"'),
            'not_file_mime_image': ('"%(file_name)s" file mime is not an image ' \
                '(jpg, png or gif)'),
            })
        cls._create_team_dir()

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

    def get_image(self, name):
        db_name = Transaction().cursor.dbname
        filename = self.file_name
        if not filename:
            return None
        filename = os.path.join(config.get('database', 'path'), db_name,
            'team', filename[0:2], filename[2:4], self.file_name)

        value = None
        try:
            with open(filename, 'rb') as file_p:
                value = buffer(file_p.read())
        except IOError:
            pass
        return value

    def get_avatarpath(self, name):
        filename = self.file_name
        if not filename:
            return None
        return '%s/%s/%s' % (filename[:2], filename[2:4], filename)

    @classmethod
    def set_image(cls, teams, name, value):
        if value is None:
            return

        db_name = Transaction().cursor.dbname
        teamdir = os.path.join(
            config.get('database', 'path'), db_name, 'team')

        for team in teams:
            file_name = team['file_name']
            
            file_mime, _ = guess_type(file_name)
            if not file_mime:
                cls.raise_user_error('not_file_mime', {
                        'file_name': file_name,
                        })
            if file_mime not in IMAGE_TYPES:
                cls.raise_user_error('not_file_mime_image', {
                        'file_name': file_name,
                        })
    
            _, ext = file_mime.split('/')
            digest = '%s.%s' % (hashlib.md5(value).hexdigest(), ext)
            subdir1 = digest[0:2]
            subdir2 = digest[2:4]
            directory = os.path.join(teamdir, subdir1, subdir2)
            filename = os.path.join(directory, digest)

            if not os.path.isdir(directory):
                os.makedirs(directory, 0770)
            with open(filename, 'wb') as file_p:
                file_p.write(value)

            cls.write([team], {
                'file_name': digest,
                })


class GalateaTeamWebSite(ModelSQL):
    'Galatea Team - Website'
    __name__ = 'galatea.team-galatea.website'
    _table = 'galatea_team_galatea_website'
    team = fields.Many2One('galatea.team', 'Team', ondelete='CASCADE',
            select=True, required=True)
    website = fields.Many2One('galatea.website', 'Website', ondelete='RESTRICT',
            select=True, required=True)
