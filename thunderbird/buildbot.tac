from twisted.application import service
from buildbot.master import BuildMaster

basedir = r'/buildbot/default'
configfile = r'master.cfg'

application = service.Application('buildmaster')
BuildMaster('.', configfile).setServiceParent(application)

