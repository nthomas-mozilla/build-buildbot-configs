from copy import deepcopy

from production_config import \
    GLOBAL_VARS, SLAVES, TRY_SLAVES, GRAPH_CONFIG


GLOBAL_VARS = deepcopy(GLOBAL_VARS)

GLOBAL_VARS['tinderbox_tree'] = 'MozillaTest'
GLOBAL_VARS['stage_username'] = 'ffxbld'
GLOBAL_VARS['stage_ssh_key'] = 'ffxbld_rsa'

# Local branch overrides
BRANCHES = {
    'try': {
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'enable_merging': False,
        'slave_key': 'try_slaves',
        'package_url': 'https://archive.mozilla.org/pub/b2g/try-builds',
        'package_dir': '%(who)s-%(got_revision)s/',
        'stage_username': 'trybld',
        'stage_ssh_key': 'trybld_dsa',
    },
}

PLATFORM_VARS = {}

PROJECTS = {}
B2G_PROJECTS = {}
