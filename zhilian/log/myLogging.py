import logging
import datetime

def logging_handle(loggername):
    '''
    用于处理日志文件
    :param loggername: 日志名
    :param filename: 日志文件名
    :return: 返回日志对象
    '''
    logger = logging.getLogger(loggername)
    formatter = logging.Formatter('%(name)s %(asctime)s %(lineno)d %(levelname)-8s:%(message)s')
    file_handler = logging.FileHandler('../../log/%s' % datetime.date.today(), encoding='utf8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger