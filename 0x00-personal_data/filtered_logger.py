#!/usr/env/python3
'''Logging messages'''

import re
from typing import List


def filter_datum(fields: List[str], redaction:str, message:str, seperator:str) -> str:
    '''Obfuscates message received
    
    Args: 
        fileds (list[str]): List of fields to be filtered.
        redaction (str): String to replace filtered fields.
        message (str): Message to be filtered.
        seperator (str): Separator between fields.
    '''
    for field in fields:
        match = f'{field}=[^{seperator}]*'
        message = re.sub(match, f'{field}={redaction}', message)
    return message
