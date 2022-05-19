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
        auth_provider = PlainTextAuthProvider("jFdztiKenZBkpDuwOaDsJuZA",
                                              "3Zsa4pecJg317.azFByBNMrwziBA9eq6YA1c8fpDpA4I0TKLDYLbHeM04b40SD_sz-LDi_ZF.D0URIW9kyazYmbhg9u-J5X+cdNHzgGY0IS4BvjnjYmCEGD4rpOwYTxi")
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
