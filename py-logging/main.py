import argparse
import json
from datetime import datetime
from logging import getLogger, DEBUG, config

import same_hierarchy as same
import lower.sub as sub

ARGS = None


def main():
    with open('../log_config.json', 'r') as f:
        log_conf = json.load(f)

    # ファイル名をタイムスタンプで作成
    log_conf["handlers"]["fileHandler"]["filename"] = \
        '../data/logs/{}.logs'.format(datetime.utcnow().strftime("%Y%m%d%H%M%S"))

    # パラメータが設定されていればレベルをINFOからDEBUGに置換
    if ARGS.verbose:
        log_conf["handlers"]["fileHandler"]["level"] = DEBUG

    # logging設定
    config.dictConfig(log_conf)

    logger = getLogger(__name__)

    logger.info('Process Start!')
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')

    same.called()
    sub.called()

    logger.info('Process End!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='Log level DEBUG for FileHandler'
    )

    ARGS, _ = parser.parse_known_args()
    main()