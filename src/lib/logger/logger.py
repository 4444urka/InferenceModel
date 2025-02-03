import logging
import os


def get_logger(name, level='local', log_file='log/app.log'):
    logger = logging.getLogger(name)

    # Устанавливаем уровень логирования
    if level == 'local':
        logger.setLevel(logging.DEBUG)
    elif level == 'dev':
        logger.setLevel(logging.DEBUG)
    elif level == 'prod':
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)

    # Проверяем существует ли директрия с логами
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    # ConsoleHandler для консольных логов
    console_formatter = logging.Formatter('%(levelname)s:   %(name)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logger.level)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # FileHandler для файл логов
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logger.level)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger