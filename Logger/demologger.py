import logging
logging.basicConfig(filename='hcllog.log',filemode='a',level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
a=10
b=0
try:
    print(a/b)
except Exception as e:
    logging.exception(e,exc_info=True)