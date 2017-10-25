"""
partition low disk space notifier
"""
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-t", "--threshold",
                  dest="threshold",
                  type="int",
                  default=90,
                  help="Set threshold (%)")

parser.add_option("-m", "--mailbox",
                  dest="mailbox",
                  help="Mail report to this mailbox")


(options, args) = parser.parse_args()

