# script to add Google Analytics tags to all html pages.
# Just give it the root html folder and it will crawl through, find all htmls and add it.

import os
import fnmatch
from bs4 import BeautifulSoup
from pathlib import Path
from clint.textui import colored

def insert_g_tag(root_path):
    # log_func = log.info  # push all messages at info level

    for directory, subdir_list, file_list in os.walk(root_path):
        if len(fnmatch.filter(file_list, "*.html")) > 0:
            print(colored.yellow(directory))  # print dir only if you find html files in it (skips printing temp dir)

        # loop through all .html files
        for curr_file in fnmatch.filter(file_list, "*.html"):

            print("  " + curr_file, end=" ")
            # read html file
            with open(os.path.join(directory, curr_file), 'r') as read_handle:
                soup = BeautifulSoup(read_handle, 'html.parser')

            try:
                # try to get the head.
                hit_head = soup.find('head')

                # find if google analytics is already injected
                skip_file = False
                for line in hit_head.contents:
                    if 'Google Analytics' in line:
                        print(colored.cyan('| already tagged - skipping file \n'))
                        skip_file = True
                        break

                if not skip_file:
                    # continuing with project
                    with open(os.path.join(directory, curr_file), 'w') as write_handle:
                        hit_head.insert(0, _get_ga_html())
                        print('| made GA script', end=" ")
                        write_handle.write(str(soup))
                    print("| wrote to disk.\n")

            except Exception as e:
                print(colored.red(" | exception - skipping file"))
                print(str(e))
                continue


def _get_ga_html():
    return_str = '<!-- Global site tag (gtag.js) - Google Analytics -->' +\
                 '<script async src="https://www.googletagmanager.com/gtag/js?id=UA-113202945-1"></script>'+ \
                 '<script> window.dataLayer = window.dataLayer || [];' \
                 'function gtag(){dataLayer.push(arguments);}' \
                 'gtag("js", new Date());' \
                 'gtag("config", "UA-113202945-1");</script>'
    return return_str

if __name__ == "__main__":
    # print(str(os.path.abspath(__file__)))
    current_path = Path(os.path.abspath(__file__))
    one_level_up = current_path.parent.parent
    print('Starting from : ' + str(one_level_up))
    insert_g_tag(str(one_level_up))
