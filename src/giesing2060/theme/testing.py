from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class Giesing2060Theme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import giesing2060.theme
        xmlconfig.file('configure.zcml',
                       giesing2060.theme,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'giesing2060.theme:default')

GIESING2060_THEME_FIXTURE = Giesing2060Theme()
GIESING2060_THEME_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(GIESING2060_THEME_FIXTURE, ),
                       name="Giesing2060Theme:Integration")