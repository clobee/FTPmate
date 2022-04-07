#!/usr/bin/python3

import argparse,socket
from os import path, system, name
from ftplib import FTP

args = []


def banner():
    data = """
============================================================
                                                             
,------.,--------.,------.                     ,--.          
|  .---''--.  .--'|  .--. ',--,--,--. ,--,--.,-'  '-. ,---.  
|  `--,    |  |   |  '--' ||        |' ,-.  |'-.  .-'| .-. : 
|  |`      |  |   |  | --' |  |  |  |\ '-'  |  |  |  \   --. 
`--'       `--'   `--'     `--`--`--' `--`--'  `--'   `----' 
                                                             
============================================================ 
"""

    data += """
FTPmate tests FTP enabled servers by uploading test executable files,
and then (optionally) uploading files which allow for 
command execution or other actions directly on the target.
"""

    print(data)

def args_collects():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "ftpip",
        help='Provide destination FTP ip',
        type=str
    )

    parser.add_argument(
        "-fp","--ftpport",
        default=21,
        required=False, 
        help='Provide destination FTP port',
        type=int
    )

    parser.add_argument(
        "-u","--url",
        help='Url of the web location.',
        type=str
    )

    parser.add_argument(
        "--user",
        default='anonymous:anonymous',
        help='<user:password> Server user and password', 
        type=str
    )

    parser.add_argument(
        "-r", "--random",
        help="Use this string instead of a random string for filenames",
        default=False,
        type=bool
    )

    parser.add_argument(
        "-v", "--verbose",
        help="Make the operation more talkative",
        default=False
    )

    # parser.add_argument(
    #     "-l", "--log",
    #     help="Log request/responses to this file",
    #     default=False
    # )

    # parser.add_argument(
    #     "-t", "--threads",
    #     help="Number of threads",
    #     default=10
    # )

    args = parser.parse_args()


def is_file_uploadable():
    print("is_file_uploadable")

def is_file_executable():
    print("is_file_executable")

def retrieve_tests_files():
    print("retrieve_tests_files")

def retrieve_backdoor_files():
    print("retrieve_backdoor_files")

def ftp_upload():
    try:
        print("FTP connection...")
        print("Creating directory...")  

        # Prepeare files
        retrieve_tests_files()
        retrieve_backdoor_files()

        # Loop over files
        is_file_uploadable()
        is_file_executable()


        # Loop over backdoors
        is_file_uploadable()
        is_file_executable()

        upload_backdoors()

    except Exception as err:
        pass
   
def main():
    try:
        args_collects()
        ftp_upload()

    except KeyboardInterrupt:
        # print "\nUser Cancelled Attack, stopping remaining threads....."
        # wait(threads) # Wait for threads to complete
        sys.exit(0) # Kill app
    # wait(args.threads) # Wait for threads to complete

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

# Method wait for threads to complete
# def wait():
#     for thread in threads: thread.join()


# clear()
banner()
main()



