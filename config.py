import os
import telegram
import time
import stripe
from flask import Flask, request
import telebot
from telebot import types
from models import *
from dotenv import load_dotenv
load_dotenv()


# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )

TOKEN = os.getenv('TOKEN')

DEBUG = False

SERVER_URL = os.getenv("SERVER_URL")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

import importdir
importdir.do("main", globals())