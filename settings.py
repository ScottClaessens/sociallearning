from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.001,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'sociallearning',
        'display_name': "Social Learning (Molleman, van den Berg, & Weissing, 2013)",
        'num_demo_participants': 8,
        'app_sequence': [#'intro',
                         'bestchoice',
                         'sociald',
                         'coord'],
        'choices': 6,
        'sigma': 200,
        'bestchoice_a_payoff': 50,
        'bestchoice_b_payoff': 50,
        'bestchoice_c_payoff': 300,
        'bestchoice_d_payoff': 300,
        'sociald_a_payoff': 300,
        'sociald_b_payoff': -250,
        'sociald_c_payoff': 600,
        'sociald_d_payoff': 0,
        'coord_a_payoff': 175,
        'coord_b_payoff': -75,
        'coord_c_payoff': -75,
        'coord_d_payoff': 675,
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []


# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# sentry
SENTRY_DSN = 'http://d606c64efb5d449d9ac450ef47fef1b0:1f312687dcc6423fa67a65d3b78782dc@sentry.otree.org/143'

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = 'h8c9ed8hdu6e2pd62kah@7$g1wququx-bzx&)fmaqa&x)s3a43'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
