# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
releaseConfig = {}
# HACK ALERT
# TODO: enable updates when 38.0 ships
#####################################

releaseConfig['skip_updates'] = True

#####################################
# END OF HACK ALERT
releaseConfig['disable_tinderbox_mail'] = True
releaseConfig['base_clobber_url'] = 'https://api.pub.build.mozilla.org/clobberer/forceclobber'

# Release Notification
releaseConfig['AllRecipients']       = ['<release-automation-notifications@mozilla.com>', '<thunderbird-drivers@mozilla.org>']
releaseConfig['ImportantRecipients'] = ['<thunderbird-drivers@mozilla.org>',]
releaseConfig['AVVendorsRecipients'] = ['<av-vendor-release-announce@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'thunderbird'
releaseConfig['stage_product']       = 'thunderbird'
releaseConfig['appName']             = 'mail'
releaseConfig['mozilla_dir']         = 'mozilla'
releaseConfig['mozilla_srcdir']      = 'mozilla'
#  Current version info
releaseConfig['version']             = '38.0'
releaseConfig['appVersion']          = '38.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'THUNDERBIRD_38_0'
releaseConfig['partialUpdates']      = {}
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'comm': {
        'name': 'comm-esr38',
        'path': 'releases/comm-esr38',
        'revision': '1234567890',
        'relbranch': None,
        'bumpFiles': {
            'mail/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
        }
    },
    'mozilla': {
        'name': 'mozilla-esr38',
        'path': 'releases/mozilla-esr38',
        'revision': '1234567890',
        'relbranch': None,
        'bumpFiles': {
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'releases/l10n/mozilla-release'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_thunderbird-esr38'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
    'build/mozharness': 'production',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = ()
releaseConfig['xulrunnerPlatforms']  = ()

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests']     = False

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'mail/locales/shipped-locales'
releaseConfig['mergeLocales']        = True
releaseConfig['l10nUsePymake']       = True

# Mercurial account
releaseConfig['hgUsername']          = 'tbirdbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/tbirdbld_dsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus4.mozilla.org'
releaseConfig['ausHost']             = None
releaseConfig['ausUser']             = 'tbirdbld'
releaseConfig['ausSshKey']           = 'tbirdbld_dsa'
releaseConfig['releaseNotesUrl']     = 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%'
releaseConfig['testOlderPartials']   = False
releaseConfig['promptWaitTime']      = None
releaseConfig['updateVerifyChunks']  = 6
releaseConfig['mozconfigs']          = {
    'linux': 'mail/config/mozconfigs/linux32/release',
    'linux64': 'mail/config/mozconfigs/linux64/release',
    'macosx64': 'mail/config/mozconfigs/macosx-universal/release',
    'win32': 'mail/config/mozconfigs/win32/release',
}
releaseConfig['source_mozconfig']      = 'mail/config/mozconfigs/linux64/release'
releaseConfig['releaseChannel']        = 'release'
releaseConfig['updateChannels'] = {
    "release": {
        "versionRegex": r"^.*$",
        "ruleId": 170,
        "patcherConfig": "mozEsr38-thunderbird-branch-patcher2.cfg",
        "localTestChannel": "release-localtest",
        "cdnTestChannel": "release-cdntest",
        "verifyConfigs": {
            "linux":  "mozEsr38-thunderbird-linux.cfg",
            "linux64":  "mozEsr38-thunderbird-linux64.cfg",
            "macosx64": "mozEsr38-thunderbird-mac64.cfg",
            "win32":  "mozEsr38-thunderbird-win32.cfg",
        },
        "testChannels": {
            "release-localtest": {
                "ruleId": 171,
            },
            "release-cdntest": {
                "ruleId": 172,
            },
        },
    },
}

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_thunderbird.py'

# Product details config
releaseConfig["productDetailsRepo"] = "svn+ssh://tbirdbld@svn.mozilla.org/libs/product-details"
releaseConfig["mozillaComRepo"]     = "svn+ssh://tbirdbld@svn.mozilla.org/projects/mozilla.com"
releaseConfig["svnSshKey"]          = "/home/cltbld/.ssh/ffxbld_rsa"

# Misc configuration
releaseConfig['enable_repo_setup'] = False
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
releaseConfig['ftpSymlinkName'] = 'latest'
