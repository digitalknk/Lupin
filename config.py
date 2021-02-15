import configparser
import os

config = configparser.RawConfigParser()
config.optionxform = str #not to convert config to lowercase
config.read('config.ini')

__vMajor__     = '3'
__vMinor__     = '0'
__vPatch__     = '0'
__vRel__       = 'e'
__version__    = __vMajor__ + '.' + __vMinor__ + '.' + __vPatch__ + __vRel__

BotToken = config.get('Bot','BotToken')
BotName = config.get('Bot','BotName')
GitHubToken = config.get('GitHub','GitHubToken')
GitHubBranch = config.get('GitHub','GitHubBranch')
GitHubUser = config.get('GitHub','GitHubUser')
GitHubRepo = config.get('GitHub','GitHubRepo')
GitHubAuthor = config.get('GitHub','GitHubAuthor')
GitHubEmail  = config.get('GitHub','GitHubEmail')
hour24 = (config.get('Misc','hour24')).lower()
defaultIndentLevel = (config.get('Misc','defaultIndentLevel'))
journalsFilesFormat = (config.get('Misc','journalsFilesFormat'))
journalsFilesExtension = (config.get('Misc','journalsFilesExtension'))
journalsFolder = (config.get('Misc','journalsFolder'))
journalsPrefix = (config.get('Misc','journalsPrefix'))
TODOCommand = (config.get('Misc','TODOCommand'))
BookmarkTag = (config.get('Misc','BookmarkTag'))
assetsFolder = (config.get('Misc','assetsFolder'))
hypothesisToken = (config.get('hypothesis','hypothesisToken'))
hypothesisUsername = (config.get('hypothesis','hypothesisUsername'))
manageHypothesisUpdates = (config.get('hypothesis','manageHypothesisUpdates')).lower()
embedHypothesisAnnotations = (config.get('hypothesis','embedHypothesisAnnotations')).lower()
hypothesisTagSpaceHandler = (config.get('hypothesis','hypothesisTagSpaceHandler'))

def isBotAuthorized(chat_id):
    isBotAuthorizedID = False
    for BotAuthorizedId in getBotAuthorizedIDs():
        if str(chat_id) == str(BotAuthorizedId):
            isBotAuthorizedID = True
    return isBotAuthorizedID

def isNewer():
    try:
        LastVersionRun = config.get('Bot', 'LastVersionRun')
        if(__version__ != LastVersionRun):
            config.set('Bot', 'LastVersionRun', __version__)
            with open('config.ini', 'w') as configfile: 
                config.write(configfile)
            return True
        else:
            return False
    except:
        config.set('Bot', 'LastVersionRun', __version__)
        with open('config.ini', 'w') as configfile: 
            config.write(configfile)
        return True

def getBotVersion():
    return __version__

def getBotAuthorizedIDs():
    return config.get('Bot','BotAuthorizedIDs').split(',')

def isManageHypothesis():
    if manageHypothesisUpdates == 'true':
        return True
    else:
        return False

def isHypothesisEmbedded():
    if embedHypothesisAnnotations == 'true':
        return True
    else:
        return False

def getHypothesisTagSpaceHandler():
    return hypothesisTagSpaceHandler

def getAssetsFolder():
    return assetsFolder

def getAssetsDestination():
    return config.get('Bot','assetsDestination').lower()

def getFirebaseBucketName():
    return config.get('Firebase','BucketName')

def getflashcardDailyGoal():
    return int(config.get('TimeSpacedRepetion', 'flashcardDailyGoal'))

def getflashcardsTag():
    return config.get('TimeSpacedRepetion', 'flashcardTag') 

def getlastNewsDisplayed():
    try:
        lastNewsDisplayed = config.get('Bot', 'lastNewsDisplayed') 
    except:
        lastNewsDisplayed = 0
        config.set('Bot', 'lastNewsDisplayed', lastNewsDisplayed)
        with open('config.ini', 'w') as configfile: 
            config.write(configfile)   
    return lastNewsDisplayed

def setlastNewsDisplayed(newsid):
    config.set('Bot', 'lastNewsDisplayed', newsid)
    with open('config.ini', 'w') as configfile: 
        config.write(configfile)   