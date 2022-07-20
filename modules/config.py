import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "15469484"))
API_HASH = getenv("API_HASH", "a4e47ac121ccd896f52fc815a9a10a8e")
BOT_TOKEN = getenv("BOT_TOKEN", "5529236088:AAFHny36b7XhIN7bH6JF92zdPp7TqAdMh78")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQA0nbdwxgI5RE-jkMq_s7jOcuLCofQfJ5653335fW2LdE0-TTrfeauDK1fnSMeIubLYpg3gSBU7aqKoAVCbew4Jk-usrhlrDWNFn579i4FMwKMhQ9rSEWxtKTlrADOVbQPAk3XTQzY2YixlC9-z59xrM548wAlk2XsRw1jPqD6qA7lLqtnxfu4qVEZ-4MXaAcSpy4PHuMeKM4ebnHfrePtCsWYKHJhSmH-A0CbZTozZZQ0U0m2tdzQtnIABjy99dJTLqykM80_5JTtRXOIbE9XAOV37Qzys_izxeWWcByEZsx7rX2jksCPF2O-stvsiHJOtzaeUzURymyI5VVABgm6WAAAAAUlnZNMA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1792725669").split()))
