# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True
releaseConfig['base_clobber_url'] = 'http://clobberer.pvt.build.mozilla.org/always_clobber.php'

# Release Notification
releaseConfig['AllRecipients']       = ['<release@mozilla.com>']
releaseConfig['ImportantRecipients'] = ['<thunderbird-drivers@mozilla.org>',]
releaseConfig['AVVendorsRecipients'] = ['<av-vendor-release-announce@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'thunderbird'
releaseConfig['appName']             = 'mail'
releaseConfig['mozilla_dir']         = 'mozilla'
#  Current version info
releaseConfig['version']             = '24.7.0'
releaseConfig['appVersion']          = '24.7.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 2
releaseConfig['baseTag']             = 'THUNDERBIRD_24_7_0'
releaseConfig['partialUpdates']      = {}  # No more supported
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'comm': {
        'name': 'comm-esr24',
        'path': 'releases/comm-esr24',
        'revision': '41aefb13384e',
        'relbranch': None,
        'bumpFiles': {
            'mail/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
        }
    },
    'mozilla': {
        # XXX remove js/src/config/milestone.txt when setting up ESR31
        'name': 'mozilla-esr24',
        'path': 'releases/mozilla-esr24',
        'revision': 'efbda06cb0fa',
        'relbranch': None,
        'bumpFiles': {
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
            'js/src/config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'releases/l10n/mozilla-release'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_thunderbird-esr24'
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
releaseConfig['enableUnittests']     = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'mail/locales/shipped-locales'
releaseConfig['mergeLocales']        = True
releaseConfig['l10nUsePymake']       = False

# Mercurial account
releaseConfig['hgUsername']          = 'tbirdbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/tbirdbld_dsa'

# Update-specific configuration
releaseConfig['patcherConfig']       = None
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus3.mozilla.org'
releaseConfig['ausHost']             = 'aus3-staging.mozilla.org'
releaseConfig['ausUser']             = 'tbirdbld'
releaseConfig['ausSshKey']           = 'tbirdbld_dsa'
releaseConfig['releaseNotesUrl']     = 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%'
releaseConfig['testOlderPartials']   = False
releaseConfig['promptWaitTime']      = None
releaseConfig['updateVerifyChunks']  = 6
releaseConfig['verifyConfigs']       = {}
releaseConfig['skip_updates']        = True
releaseConfig['mozconfigs']          = {
    'linux': 'mail/config/mozconfigs/linux32/release',
    'linux64': 'mail/config/mozconfigs/linux64/release',
    'macosx64': 'mail/config/mozconfigs/macosx-universal/release',
    'win32': 'mail/config/mozconfigs/win32/release',
}
releaseConfig['releaseChannel']      = 'release'
releaseConfig['testChannels']        = []
releaseConfig['testChannelRuleIds']  = []

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_thunderbird.py'

# Misc configuration
releaseConfig['enable_repo_setup'] = False
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
releaseConfig['ftpSymlinkName'] = 'latest-24.0esr'