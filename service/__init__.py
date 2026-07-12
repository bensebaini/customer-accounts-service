import os
import logging
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(app)

from service import routes, models
