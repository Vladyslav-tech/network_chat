import os
import subprocess
import time
import signal
import os


PROCESS = []
PATH_TO_SCRIPT_SERVER = os.path.join(os.path.dirname(__file__), "server.py")
PATH_TO_SCRIPT_CLIENTS = os.path.join(os.path.dirname(__file__), "client.py")

while True:
    user_input = input("Нажмите:\n"
                   "s- для запуска сервера и клиентов\n"
                   "c- для запуска клиентов\n"
                   "q- для выхода\n"
                   "Поле для ввода :")

    if user_input == 'q':
        break
    # запуск сервера
    if user_input == 's':
        PROCESS.append(subprocess.Popen(
            f'osascript -e \'tell application "Terminal" to do'
            f' script "python3 {PATH_TO_SCRIPT_SERVER}"\'', shell=True))

    # запуск клиентов
    elif user_input == 'c':
        PROCESS.append(subprocess.Popen(
            f'osascript -e \'tell application "Terminal" to do'
            f' script "python3 {PATH_TO_SCRIPT_CLIENTS} -n test1"\'',
            shell=True))
        time.sleep(3)
        PROCESS.append(subprocess.Popen(
            f'osascript -e \'tell application "Terminal" to do'
            f' script "python3 {PATH_TO_SCRIPT_CLIENTS} -n test2"\'',
            shell=True))
        time.sleep(3)
        # PROCESS.append(subprocess.Popen(
        #     f'osascript -e \'tell application "Terminal" to do'
        #     f' script "python3 {PATH_TO_SCRIPT_CLIENTS} -n test3"\'',
        #     shell=True))
    elif user_input == 'stop':
        for proc in PROCESS:
            os.kill(proc.pid, signal.SIGTERM)


