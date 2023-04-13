"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq16o2qv2dcb927060-a.oregon-postgres.render.com",
        database="todo_wedy",
        user="root",
        password="jVoC6ps5hULtbaibIpURuJ4HrrLK0iHO")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
