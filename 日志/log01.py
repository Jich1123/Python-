import logging
LOG_FORMAT = "%(asctime)s============%(levelname)s++++++++++%(message)s"
logging.basicConfig(filename="tuling.log", level=logging.DEBUG, format=LOG_FORMAT)
logging.debug("DEBUG")
logging.info("INFO")
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL")

logging.log(logging.DEBUG,"DEBUG")
logging.log(logging.INFO,"INFO")
logging.log(logging.WARNING,"WARNING")
logging.log(logging.ERROR,"ERROR")
logging.log(logging.CRITICAL,"CRITICAL")