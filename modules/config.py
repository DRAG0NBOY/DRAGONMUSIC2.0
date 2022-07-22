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
STRING_SESSION = getenv("STRING_SESSION", "BQAoz_gzk70hPh2WdAwiN5yMcSqYmWr2pSssHR4PHtuwr97o3XNNaxd7CNGkr3VhtnRpLEsizeuUhD3b2k6bkvC2Tq9dvt6MVWpKQXZ6pprQgKcckOfeqh6EZc6r5kx414kwgV6q-_NX_uirshDtXso2zXlfyjvMnOJPqGkYHgCTzGYtmFa5B-CTzL8RBVPPQJXyE9zTBFXhw8BmemLx6GWUtjD3IEwizi737N3LpnH0YUyqgf4zwqTkLuDZkUsSV2uBHMM2NDX8KsHWu2G_VKHXeZAikf3f9d8felXjwTWZOpqaFmVBHsF0joO6EX2u-GCmRQAc8SfJwb0SmzGj6x6zAAAAAUlnZNMA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1792725669").split()))
