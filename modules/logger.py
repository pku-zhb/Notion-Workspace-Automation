import logging

logger = logging.getLogger('applog')
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler(filename='NotionAutomation.log')
fileHandler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s %(filename)s:%(lineno)s\n%(levelname)s: %(message)s\n")
formatter.datefmt = "%Y-%m-%d %H:%M:%S"
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
