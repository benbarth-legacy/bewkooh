#!/usr/bin/env python3

import os
import argparse
from flask import Flask

#sys.argv
parser = argparse.ArgumentParser()
parser.add_argument("path", help="The path to execute the command in.")
parser.add_argument("--port", help="The port do listen on. (Default: 8080)")
parser.add_argument("--webhookPath", help="The webhook path. (Default: '/webhook')")
parser.add_argument("--command", help="The command to execute. (Default: 'git pull')")
args = parser.parse_args()

path = args.path

port = 8080
if args.port:
    port = args.port

command = 'git pull'
if args.command:
    command = args.command

webhookPath = '/webhook'
if args.webhookPath:
    webhookPath = args.webhookPath

command = 'cd {0} && {1}'.format(path, command)


app = Flask(__name__)

@app.route(webhookPath, methods=['GET','POST'])
def webhook():
    os.system(command)
    return "OK"

if __name__ == '__main__':
    app.run(port=port)