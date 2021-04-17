import psycopg2
import os
from dotenv import load_dotenv

class Database:
    
    def __init__(self):

        load_dotenv(os.path.dirname(os.path.realpath(__file__)))
        self.DATABASE_URL = os.getenv("DATABASE_URL")

        self.connection = psycopg2.connect(self.DATABASE_URL, sslmode = "require")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS discofy")
        self.cursor.execute("USE discofy")

    def create(self, guild_id: str) -> bool:

        try:

            self.cursor.execute("USE discofy")

            query = f"""CREATE TABLE {guild_id}
            (SONG_NAME  VARCHAR(100)    NOT NULL
            SONG_URL    VARCHAR(100)    NOT NULL,
            USERNAME    VARCHAR(30)     NOT NULL);"""

            self.cursor.execute(query)
            self.connection.commit()

            return True

        except:
            return False

    def read(self, guild_id: str):

        try:

            self.cursor.execute("USE discofy")
            query = f"SELECT SONG_URL, USERNAME from {guild_id}"
            self.cursor.execute(query)
            result = self.cursor.fetchall()

            return result

        except:
            return False

    def insert(self, guild_id: str, song_name: str, song_url: str, username: str) -> bool:

        try:

            self.cursor.execute("USE discofy")

            query = f"""INSERT INTO {guild_id} (SONG_NAME, SONG_URL, USERNAME)
            VALUES ('{song_name}', '{song_url}', '{username}')"""

            self.cursor.execute(query)
            self.connection.commit()

            return True

        except:
            return False

    def delete(self, guild_id: str, song_name: str) -> bool:

        try:

            self.cursor.execute("USE discofy")
            query = f"DELETE FROM {guild_id} where SONG_NAME = '{song_name}';"
            self.cursor.execute(query)
            self.connection.commit()
            
            return True

        except:
            return False

    def purge(self, guild_id: str) -> bool:

        try:

            self.cursor.execute("USE discofy")
            query = f"DROP TABLE {guild_id}"
            self.cursor.execute(query)
            self.connection.commit()
            
            return True

        except:
            return False


"""
discofy
"""
