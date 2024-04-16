from kaggle.api.kaggle_api_extended import KaggleApi

import pandas as pd
import numpy


def ingest_data():
    print('Start data ingestion from Kaggle ...')
    api = KaggleApi()
    api.authenticate()

    dataset = 'parisrohan/credit-score-classification'
    destination_path = 'data/bronze/'

    api.dataset_download_files(dataset, destination_path, unzip=True)


def process_data():
    """
        To-do:
        - Reads data from bronze layer;
        - Apply all necessary data treatments;
        - Send data to silver layer.
    """


def publish_data():
    """
        To-do:
        - Reads data from silver layer;
        - Apply all necessary data treatments;
        - Send data to gold layer.
    """


if __name__ == '__main__':
    ingest_data()
    process_data()
    publish_data()
    