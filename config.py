# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = "13675555"
    API_HASH = "c0da9c346d2c45dbc7ec49a05da9b2b6"
    BOT_TOKEN = "5555986769:AAG-nNw82PHwBPlPZ5h55d3hnfHxzqc5JeI"
    LOGS_CHANNEL = "-1001615619184"
    BOT_OWNER = "5591954930"
    MONGODB_URL = "mongodb+srv://f2l:f2l@cluster0.fjjge1y.mongodb.net/?retryWrites=true&w=majority"
    GOFILE_TOKEN = "zPq1O5MunNKBxs33nTfpvmAnQRsB6PJF"
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
