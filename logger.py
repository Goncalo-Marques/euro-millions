from datetime import datetime
from enum import Enum
import os
import logging


class LogType(Enum):
    INFO = "info"
    ERROR = "error"


class Logger:
    def __init__(self, folder_path: str, name: str) -> None:
        time_now_str = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        self.folder_path = os.path.join(folder_path, time_now_str)
        self.name = name

        # make sure that the directories for that path exist
        os.makedirs(self.folder_path, exist_ok=True)

    # log writes a new line in the log file for the given type, given message and the current time
    def log(self, message: str, type: LogType) -> None:
        file_name = "{}.log".format(self.name)
        file_path_log = os.path.join(self.folder_path, file_name)

        time_now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print
        message_to_print = "[{}] [{}] [{}] {}".format(
            time_now_str, type.value, self.name, message
        )
        print(message_to_print)

        # write to file
        try:
            with open(file_path_log, "a") as f:
                message_to_write = "[{}] [{}] {}\n".format(
                    time_now_str, type.value, message
                )
                f.write(message_to_write)

        except Exception as e:
            logging.error(
                "failed to write to log file for {}: {}".format(self.name, e.__str__())
            )

    # log_info writes a new informative line in the log file for the given message with the current time
    def log_info(self, message: str) -> None:
        self.log(message, LogType.INFO)

    # log_error writes a new error line in the log file for the given message with the current time
    def log_error(self, message: str) -> None:
        self.log(message, LogType.ERROR)
