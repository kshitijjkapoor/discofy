import logging
import os
import pathlib
import re
import urllib.request
import urllib.parse

class Logs:

    def __init__(self, guild: str, username: str):

        self.guild = guild
        self.username = username
        self.dir = pathlib.Path(__file__).parents[0]

        logging.basicConfig(
            filename = f"{self.dir}/servers/{self.guild}-{self.username}.log",
            format = "%(message)s",
            filemode = "w"
        )

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def song_url(self, song_name: str):

        try:
            content = urllib.parse.quote(song_name)
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + content)
            videos = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = "https://www.youtube.com/watch?v=" + videos[0]

            return url

        except:
            return False

    def add(self, song_name: str) -> bool:

        try:
            song_url = Logs(self.guild, self.username).song_url(song_name)

            if song_url:
                self.logger.info(f"{song_name} -> {song_url}")
                return True

            else:
                return False

        except:
            return False

    def remove(self, song_name: str):

        try:

            if os.path.isfile(f"{self.dir}/servers/{self.guild}-{self.username}.log"):
                
                file = open(f"{self.dir}/servers/{self.guild}-{self.username}.log")
                new_file = open(f"{self.dir}/servers/{self.guild}-{self.username}-swap.log", "w")
                content = file.read().splitlines()

                for song in content:
                    name = song.split(" -> ")

                    if name[0] != song_name:
                        new_file.write(song + "\n")

                file.close()
                new_file.close()
                
                os.remove(f"{self.dir}/servers/{self.guild}-{self.username}.log")
                os.rename(f"{self.dir}/servers/{self.guild}-{self.username}-swap.log", f"{self.dir}/servers/{self.guild}-{self.username}.log")

                return True

            else:
                return False

        except:
            return False

    def purge(self):

        try:

            if os.path.isfile(f"{self.dir}/servers/{self.guild}-{self.username}.log"):

                os.remove(f"{self.dir}/servers/{self.guild}-{self.username}.log")
                return True

            else:
                return False

        except:
            return False

