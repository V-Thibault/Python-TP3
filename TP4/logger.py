import logging
class Logger():
    def __init__(self):
        super().__init__()
    def Print_log(msg):
        logging.basicConfig(filename='log.txt', encoding='utf-8',format='%(asctime)s %(message)s')
        logging.warning(msg)


