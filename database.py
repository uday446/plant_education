import uuid
from datetime import datetime
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
from datetime import date


def dataBaseConnection():
    try:
        cloud_config = {
            'secure_connect_bundle': 'secure-connect-plant-recognition.zip'
        }
        auth_provider = PlainTextAuthProvider(os.environ.get("dbstr1"), os.environ.get("dbstr2"))
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect('log')
    except ConnectionError:
        raise ConnectionError
    return session


def insertIntoTable(Log):
    try:
        conn = dataBaseConnection()
        today = date.today()
        now = datetime.now()
        now = now.strftime("%H/%M/%S")
        today = today.strftime("%d/%m/%Y")
        log = str(Log)
        print(log)
        query = 'INSERT INTO log.logs (id, date, description) values(uuid(),{0},{1})'.format(today, log)
        conn.execute("""INSERT INTO log.logs (id, date, description) values (%s, %s, %s)""", (uuid.uuid1(), today, log))
    except Exception as e:
        raise e
