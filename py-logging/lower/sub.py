from logging import getLogger


def called():
    logger = getLogger(__name__)
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
