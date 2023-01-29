#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("APP_ID", 7275264)
    API_HASH = config("API_HASH", "6a5b202320d2e67f19fb43fb294f17a3")
    BOT_TOKEN = config("BOT_TOKEN", "5833971496:AAFYCcEAI5c53X66XNvzD1CAWiThbpbC97M")
    DEV = 1008174601
    OWNER = config("OWNER", "1008174601")
    LOG = config("LOG_CHANNEL", -1001529761844)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
