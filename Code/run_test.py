from tools import Tools
from select_reading import SelectReading


class Run:
    def __init__(self):
        Tools.run_all_folder_files(self, "source\World_English_Bible")


Run()
