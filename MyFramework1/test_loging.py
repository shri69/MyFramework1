import logging
def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    logger.addHandler(fileHandler)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("information")
    logger.warning("Warning")
    logger.error("a major error")
    logger.critical("critical issue")



