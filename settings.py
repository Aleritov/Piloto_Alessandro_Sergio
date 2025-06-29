from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    session_name='test_session',
    survey_link='https://forms.gle/oX36R6uzS16Q1xBS7',
    timeseries_filepath='_static/ZTS/timeseries_files/',
    timeseries_filename='["demo_1.csv", "demo_2.csv"]',
    refresh_rate_ms='[250, 250]',
    initial_cash='[100, 1000]',
    initial_shares='[0, 0]',
    trading_button_values='[[1, 3, 5], [1, 3, 5]]',
    random_round_payoff=True,
    training_round=True,
    graph_buffer=0.05,
    real_world_currency_per_point=1,
    participation_fee=1.00,
    doc='',
)

SESSION_CONFIGS = [
    dict(
        name='Piloto_Alessandro_Sergio',
        num_demo_participants=10,
        app_sequence=['ZTS', 'Survey']
    ),
]

SESSION_FIELDS = ['num_rounds']
PARTICIPANT_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='ZTS_test_room',
        display_name='ZTS Test Room',
        participant_label_file='_rooms/zts_test.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
<b>Zurich Trading Simulator (ZTS)</b>
<p>A web-based behaviour experiment 
in the form of a trading game, designed by the Chair of Cognitive Science - ETH Zurich.</p>
"""

# Change this default secret key to a fully random one after forking.
SECRET_KEY = '1sjjosef4a7#)%cb3_us8%aa*l_d476lp&*hatrb6al*u*dude^'