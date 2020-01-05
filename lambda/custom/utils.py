import os
import csv
import boto3
from typing import Sequence


def read_file_from_s3(bucket_name, file_path):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, file_path)
    body = obj.get()['Body'].read()
    decoded: str = body.decode('utf-8')
    new_lines = decoded.split('\r\n')
    return [row for row in new_lines]


def read_file_from_lambda(file_name: str,
                          full_path: str = '') -> Sequence[Sequence[str]]:
    open_file_path = full_path if full_path \
        else os.path.join(os.getcwd(), file_name)
    with open(open_file_path) as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        return [row for row in spam_reader]


def read_file(target: str = '') -> Sequence[Sequence[str]]:
    file_name = os.getenv('FILE_NAME')
    if target == 's3':
        bucket_name = os.getenv('BUCKET_NAME')
        file_key = os.path.join(
            os.getenv('PROJECT_NAME'), file_name
            )
        return read_file_from_s3(bucket_name, file_key)
    return read_file_from_lambda(file_name)


def get_speech_text(_, text_keys):
    if isinstance(text_keys, str):
        text_keys = [text_keys]
    # text keys list to response text
    speech_texts = [_.get(text_key, text_key)
                    for text_key in text_keys]
    separated_value = _.get('SEPARATED_VALUE', '.')
    return f'{separated_value}'.join(speech_texts)


class Singleton:
    _unique_instance = None

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()
        return cls._unique_instance
