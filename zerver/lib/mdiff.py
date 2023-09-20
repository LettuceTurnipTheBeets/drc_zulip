import logging
import os
import subprocess


class DiffError(Exception):
    pass


def diff_strings(output: str, expected_output: str) -> str:
<<<<<<< HEAD
    mdiff_path = "frontend_tests/zjsunit/mdiff.js"
=======
    mdiff_path = "web/tests/lib/mdiff.js"
>>>>>>> drc_main
    if not os.path.isfile(mdiff_path):  # nocoverage
        msg = "Cannot find mdiff for Markdown diff rendering"
        logging.error(msg)
        raise DiffError(msg)

    command = ["node", mdiff_path, output, expected_output]
    diff = subprocess.check_output(command, text=True)
    return diff
