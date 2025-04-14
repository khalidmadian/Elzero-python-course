# --------------------------------------------------
# -- Advanced_Lessons => Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger.
# -----------------------------------------------------
# Basic Config
# - level => Level of Severity
# - filename => File Name and Extension
# - mode => Mode Of The File a => Append
# - format => Format For The Log Message
# ------------------------
# getLogger => Return a Logger With the Specified Name

import logging

logging.basicConfig(filename='khalid.log')

logging.critical('this is critical message')
