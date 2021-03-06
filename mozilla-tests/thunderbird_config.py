from copy import deepcopy

from config import BRANCH_UNITTEST_VARS, MOZHARNESS_REBOOT_CMD
from localconfig import SLAVES, TRY_SLAVES, GLOBAL_VARS

import config_common
reload(config_common)
from config_common import delete_slave_platform

import thunderbird_localconfig
reload(thunderbird_localconfig)
import master_common
reload(master_common)
from master_common import setMainCommVersions, items_before, items_at_least
import thunderbird_project_branches
reload(thunderbird_project_branches)
from thunderbird_project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

GLOBAL_VARS = deepcopy(GLOBAL_VARS)
BRANCH_UNITTEST_VARS = deepcopy(BRANCH_UNITTEST_VARS)

GLOBAL_VARS['stage_username'] = 'tbirdbld'
GLOBAL_VARS.update(thunderbird_localconfig.GLOBAL_VARS.copy())

BRANCHES = {
    'comm-central': {
    },
    'comm-beta': {
    },
    'comm-aurora': {
    },
    'comm-esr38': {
        'gecko_version': 38
    },
    'comm-esr45': {
        'gecko_version': 45
    },
    'try-comm-central': {
        'coallesce_jobs': False
    },
}

setMainCommVersions(BRANCHES)

PLATFORMS = {
    'macosx64': {},
    'win32': {},
    'linux': {},
    'linux64': {},
}

builder_prefix = "TB "

PLATFORMS['macosx64']['slave_platforms'] = ['snowleopard', 'yosemite', 'yosemite_r7']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['snowleopard'] = {'name': builder_prefix + "Rev4 MacOSX Snow Leopard 10.6"}
PLATFORMS['macosx64']['yosemite'] = {'name': builder_prefix + "Rev5 MacOSX Yosemite 10.10"}
PLATFORMS['macosx64']['yosemite_r7'] = {'name': builder_prefix + "Rev7 MacOSX Yosemite 10.10.5"}
PLATFORMS['macosx64']['stage_product'] = 'thunderbird'
PLATFORMS['macosx64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
}
PLATFORMS['win32']['slave_platforms'] = ['xp-ix', 'win7-ix']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp-ix'] = {'name': builder_prefix + "Windows XP 32-bit"}
PLATFORMS['win32']['win7-ix'] = {'name': builder_prefix + "Windows 7 32-bit"}
PLATFORMS['win32']['stage_product'] = 'thunderbird'
PLATFORMS['win32']['mozharness_config'] = {
    'mozharness_python': ['c:/mozilla-build/python27/python', '-u'],
    'hg_bin': 'c:\\mozilla-build\\hg\\hg',
    'reboot_command': ['c:/mozilla-build/python27/python', '-u'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '32',
}
PLATFORMS['linux']['slave_platforms'] = ['ubuntu32_vm']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['ubuntu32_vm'] = {'name': 'Ubuntu VM 12.04'}
PLATFORMS['linux']['stage_product'] = 'thunderbird'
PLATFORMS['linux']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '32',
}

PLATFORMS['linux64']['slave_platforms'] = ['ubuntu64_vm']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['ubuntu64_vm'] = {'name': 'Ubuntu VM 12.04 x64'}
PLATFORMS['linux64']['stage_product'] = 'thunderbird'
PLATFORMS['linux64']['mozharness_config'] = {
    'mozharness_python': '/tools/buildbot/bin/python',
    'hg_bin': 'hg',
    'reboot_command': ['/tools/buildbot/bin/python'] + MOZHARNESS_REBOOT_CMD,
    'system_bits': '64',
}

# Lets be explicit instead of magical.
for platform, platform_config in PLATFORMS.iteritems():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform])
        if slave_platform in TRY_SLAVES:
            platform_config[slave_platform]['try_slaves'] = sorted(TRY_SLAVES[slave_platform])
        else:
            platform_config[slave_platform]['try_slaves'] = platform_config[slave_platform]['slaves']

MOBILE_PLATFORMS = []

ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
    PLATFORMS['linux64']['slave_platforms'] + \
    PLATFORMS['win32']['slave_platforms'] + \
    PLATFORMS['macosx64']['slave_platforms']

WIN7_ONLY = ['win7']

NO_WIN = PLATFORMS['macosx64']['slave_platforms'] + PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms']

NO_MAC = PLATFORMS['linux']['slave_platforms'] + \
    PLATFORMS['linux64']['slave_platforms'] + \
    PLATFORMS['win32']['slave_platforms']

MAC_ONLY = PLATFORMS['macosx64']['slave_platforms']

SUITES = {}

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'linux': {},
        'linux64': {},
        'macosx64': {},
        'win32': {},
    },
}
XPCSHELL = [
    ('xpcshell', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--xpcshell-suite', 'xpcshell',
                       '--cfg', 'unittests/thunderbird_extra.py'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]
XPCSHELL_TWO_CHUNKS = [
    ('xpcshell', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--xpcshell-suite', 'xpcshell',
                       '--cfg', 'unittests/thunderbird_extra.py'],
        'blob_upload': True,
        'script_maxtime': 7200,
        'totalChunks': 2,
    }),
]
MOZMILL = [
    ('mozmill', {
        'use_mozharness': True,
        'script_path': 'scripts/desktop_unittest.py',
        'extra_args': ['--mozmill-suite', 'mozmill',
                       '--cfg', 'unittests/thunderbird_extra.py'],
        'blob_upload': True,
        'script_maxtime': 7200,
    }),
]

# Default set of unit tests
UNITTEST_SUITES = {
    'opt_unittest_suites': MOZMILL + XPCSHELL,
    'debug_unittest_suites': MOZMILL + XPCSHELL,
    'debug_unittest_suites_two_chunks': MOZMILL + XPCSHELL_TWO_CHUNKS,
}
# You must define opt_unittest_suites when enable_opt_unittests is True for a
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
    'linux': {
        'product_name': 'thunderbird',
        'app_name': 'mail',
        'brand_name': 'Daily',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'ubuntu32_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites_two_chunks'][:],
            'suite_config': {
                'xpcshell': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mozmill': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
        },
    },
    'linux64': {
        'product_name': 'thunderbird',
        'app_name': 'mail',
        'brand_name': 'Daily',
        'builds_before_reboot': 1,
        'unittest-env': {'DISPLAY': ':0'},
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'ubuntu64_vm': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites_two_chunks'][:],
            'suite_config': {
                'xpcshell': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
                'mozmill': {
                    'config_files': ["unittests/linux_unittest.py"],
                },
            },
        },
    },
    'win32': {
        'product_name': 'thunderbird',
        'app_name': 'mail',
        'brand_name': 'Daily',
        'builds_before_reboot': 1,
        'mochitest_leak_threshold': 484,
        'crashtest_leak_threshold': 484,
        'env_name': 'win32-perf-unittest',
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'xp-ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozmill': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        },
        'win7-ix': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'xpcshell': {
                    'config_files': ["unittests/win_unittest.py"],
                },
                'mozmill': {
                    'config_files': ["unittests/win_unittest.py"],
                },
            },
        },
    },
    'macosx64': {
        'product_name': 'thunderbird',
        'app_name': 'mail',
        'brand_name': 'Daily',
        'builds_before_reboot': 1,
        'enable_opt_unittests': True,
        'enable_debug_unittests': True,
        'snowleopard': {
            'opt_unittest_suites': XPCSHELL[:],
            'debug_unittest_suites': XPCSHELL[:],
            'suite_config': {
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mozmill': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
        },
        'yosemite': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mozmill': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
        },
        'yosemite_r7': {
            'opt_unittest_suites': UNITTEST_SUITES['opt_unittest_suites'][:],
            'debug_unittest_suites': UNITTEST_SUITES['debug_unittest_suites'][:],
            'suite_config': {
                'xpcshell': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
                'mozmill': {
                    'config_files': ["unittests/mac_unittest.py"],
                },
            },
        },
    },
}

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])

# Copy unittest vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.iteritems():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for key, value in BRANCH_UNITTEST_VARS.iteritems():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_UNITTEST_VARS.iteritems():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.iteritems():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    # Copy in local config
    if branch in thunderbird_localconfig.BRANCHES:
        for key, value in thunderbird_localconfig.BRANCHES[branch].iteritems():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.iteritems():
                    for key, value in platform_config.iteritems():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)

    # Merge in any project branch config for platforms
    if branch in ACTIVE_PROJECT_BRANCHES and 'platforms' in PROJECT_BRANCHES[branch]:
        for platform, platform_config in PROJECT_BRANCHES[branch]['platforms'].iteritems():
            if platform in PLATFORMS:
                for key, value in platform_config.iteritems():
                    value = deepcopy(value)
                    if isinstance(value, str):
                        value = value % locals()
                    BRANCHES[branch]['platforms'][platform][key] = value

    for platform, platform_config in thunderbird_localconfig.PLATFORM_VARS.iteritems():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.iteritems():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

########
# Entries in BRANCHES for tests should be a tuple of:
# - Number of tests to run per build
# - Whether queue merging is on
# - TalosFactory options
# - Which platforms to run on

# Let's load the defaults
for branch in BRANCHES.keys():
    BRANCHES[branch]['repo_path'] = branch
    BRANCHES[branch]['branch_name'] = branch.title()
    BRANCHES[branch]['build_branch'] = branch.title()
    BRANCHES[branch]['enable_unittests'] = True
    BRANCHES[branch]['fetch_symbols'] = True
    BRANCHES[branch]['fetch_release_symbols'] = False
    BRANCHES[branch]['pgo_strategy'] = None
    BRANCHES[branch]['pgo_platforms'] = []

# The following are exceptions to the defaults

######## comm-central
BRANCHES['comm-central']['branch_name'] = "Thunderbird"
BRANCHES['comm-central']['repo_path'] = "comm-central"
BRANCHES['comm-central']['moz_repo_path'] = "mozilla-central"
#BRANCHES['comm-central']['build_branch'] = "1.9.2"
BRANCHES['comm-central']['pgo_strategy'] = None

######## comm-beta
BRANCHES['comm-beta']['pgo_strategy'] = None
BRANCHES['comm-beta']['repo_path'] = "releases/comm-beta"
BRANCHES['comm-beta']['moz_repo_path'] = "releases/mozilla-beta"

######## comm-aurora
BRANCHES['comm-aurora']['pgo_strategy'] = None
BRANCHES['comm-aurora']['repo_path'] = "releases/comm-aurora"
BRANCHES['comm-aurora']['moz_repo_path'] = "releases/mozilla-aurora"

######## comm-esr38
BRANCHES['comm-esr38']['pgo_strategy'] = None
BRANCHES['comm-esr38']['repo_path'] = "releases/comm-esr38"
BRANCHES['comm-esr38']['moz_repo_path'] = "releases/mozilla-esr38"

######## comm-esr45
BRANCHES['comm-esr45']['pgo_strategy'] = None
BRANCHES['comm-esr45']['repo_path'] = "releases/comm-esr45"
BRANCHES['comm-esr45']['moz_repo_path'] = "releases/mozilla-esr45"

######## try
BRANCHES['try-comm-central']['enable_try'] = True
BRANCHES['try-comm-central']['moz_repo_path'] = "mozilla-central"

# Disable Rev3 winxp and win7 machines for all branches
for branch in set(BRANCHES.keys()):
    if 'win32' not in BRANCHES[branch]['platforms']:
        continue
    if 'win7' not in BRANCHES[branch]['platforms']['win32']:
        continue
    del BRANCHES[branch]['platforms']['win32']['win7']
    BRANCHES[branch]['platforms']['win32']['slave_platforms'] = ['xp-ix', 'win7-ix']

for branch in set(BRANCHES.keys()):
    if 'linux' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['linux']['slave_platforms'] = ['ubuntu32_vm']
    if 'linux64' in BRANCHES[branch]['platforms']:
        BRANCHES[branch]['platforms']['linux64']['slave_platforms'] = ['ubuntu64_vm']

# xpcshell-on-mozharness should ride the trains
# Replace old trains with non-mozharness code.
# MERGE DAY (remove this code once Thunderbird no longer services Gecko 32 and lower)
for platform in PLATFORMS.keys():
    XPCSHELL_OLD = ('xpcshell', ['xpcshell'])
    for name, branch in items_before(BRANCHES, 'gecko_version', 33):
        if platform not in branch['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in branch['platforms'][platform]:
                continue

            for suite_type in ['opt_unittest_suites', 'debug_unittest_suites']:
                for xpcshell in XPCSHELL:
                    try:
                        branch['platforms'][platform][slave_platform][suite_type].remove(xpcshell)
                        if XPCSHELL_OLD not in branch['platforms'][platform][slave_platform][suite_type]:
                            branch['platforms'][platform][slave_platform][suite_type].append(XPCSHELL_OLD)
                    except ValueError:
                        # wasn't in the list anyways
                        pass

# Mac OSX signing changes in gecko 34 - bug 1117637, bug 1047584
for name, branch in items_before(BRANCHES, 'gecko_version', 34):
  if 'macosx64' in BRANCHES[name]['platforms']:
    BRANCHES[name]['platforms']['macosx64']['mac_res_subdir'] = 'MacOS'

# mozmill-on-mozharness should ride the trains
# Replace old trains with non-mozharness code.
# MERGE DAY (remove this code once Thunderbird no longer services Gecko 37 and lower)
for platform in PLATFORMS.keys():
    MOZMILL_OLD = ('mozmill', ['mozmill'])
    for name, branch in items_before(BRANCHES, 'gecko_version', 38):
        if platform not in branch['platforms']:
            continue
        for slave_platform in PLATFORMS[platform]['slave_platforms']:
            if slave_platform not in branch['platforms'][platform]:
                continue

            for suite_type in ['opt_unittest_suites', 'debug_unittest_suites']:
                for mozmill in MOZMILL:
                    try:
                        branch['platforms'][platform][slave_platform][suite_type].remove(mozmill)
                        if MOZMILL_OLD not in branch['platforms'][platform][slave_platform][suite_type]:
                            branch['platforms'][platform][slave_platform][suite_type].append(MOZMILL_OLD)
                    except ValueError:
                        # wasn't in the list anyways
                        pass

# Bug 1230763 - enable r7 on trunk and disable r5 on non-trunk
ride_trains_branches = []
for name, branch in items_at_least(BRANCHES, 'gecko_version', 46):
    ride_trains_branches.append(name)

not_ride_trains_branches = []
for name, branch in items_before(BRANCHES, 'gecko_version', 46):
    not_ride_trains_branches.append(name)

delete_slave_platform(BRANCHES, PLATFORMS, {'macosx64': 'yosemite_r7'}, branch_exclusions=ride_trains_branches)
delete_slave_platform(BRANCHES, PLATFORMS, {'macosx64': 'yosemite'}, branch_exclusions=not_ride_trains_branches)

# Enable mozharness pinning
for _, branch in items_at_least(BRANCHES, 'gecko_version', 30):
    branch['script_repo_manifest'] = \
        "https://hg.mozilla.org/%(moz_repo_path)s/raw-file/default/" + \
        "testing/mozharness/mozharness.json"
    # mozharness_archiver_repo_path tells the factory to use a copy of mozharness from within the
    #  gecko tree and also allows us to overwrite which gecko repo to use. Useful for platforms
    # like Thunderbird
    branch['mozharness_archiver_repo_path'] = '%(moz_repo_path)s'
    branch['mozharness_archiver_rev'] = 'default'

# Cypress is the m-c in c-c repo, so set some specifics
BRANCHES['cypress']['mozharness_archiver_repo_path'] = '%(repo_path)s'
if 'mozharness_archiver_rev' in BRANCHES['cypress']:
    # Without this retriggers wouldn't use the repo rev for mozharness.
    del BRANCHES['cypress']['mozharness_archiver_rev']
BRANCHES['cypress']['script_repo_manifest'] = \
    "https://hg.mozilla.org/%(repo_path)s/raw-file/%(revision)s/" + \
    "testing/mozharness/mozharness.json"
BRANCHES['cypress']['pgo_strategy'] = None


if __name__ == "__main__":
    import sys
    import pprint

    args = sys.argv[1:]

    if len(args) > 0:
        items = dict([(b, BRANCHES[b]) for b in args])
    else:
        items = dict(BRANCHES.iteritems())

    for k, v in sorted(items.iteritems()):
        out = pprint.pformat(v)
        for l in out.splitlines():
            print '%s: %s' % (k, l)

    for suite in sorted(SUITES):
        out = pprint.pformat(SUITES[suite])
        for l in out.splitlines():
            print '%s: %s' % (suite, l)
