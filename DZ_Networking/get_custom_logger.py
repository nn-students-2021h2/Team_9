import logging
import os
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

def get_logger(name : str) -> logging.Logger:
    logger = logging.getLogger(name)

    ch = logging.FileHandler(f"{name}.log", mode='a')
    ch.setLevel(logging.DEBUG)

    formater=logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    ch.setFormatter(formater)

    logger.addHandler(ch)
    return logger 
