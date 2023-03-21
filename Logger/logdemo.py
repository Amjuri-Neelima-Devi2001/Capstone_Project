import logging
logging.basicConfig(filename='hcllog.log',filemode='a',level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
logging.debug("hello from debug")
logging.info("hello from info")
logging.warning("hello from warning")
logging.error("hello from error")
logging.critical("hello from critical")