#!/usr/bin/env python3
"""
Server code for memegen rojigan.
"""
import logging
import os

from flask import Flask
from flask import request
from flask import send_from_directory
from flask import redirect
from flask import render_template
from flask import url_for


app = Flask(__name__)


links = None

def get_image_paths(directory_path='static/images/'):
    image_names = os.listdir(directory_path)
    image_paths = [directory_path + images_name for images_name in image_names]
    return image_paths


@app.route('/')
def index():

    image_paths = get_image_paths()

    return render_template('index.jinja', images=image_paths)


def main(args):

    app.run(
        host='0.0.0.0',
        debug=args.debug,
        port=args.port
    )


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument('-p', '--port',
                        help="Port that the server will run on.",
                        type=int,
                        default=8383)
    parser.add_argument('-d', '--debug',
                        help="Whether or not to run in debug mode.",
                        default=False,
                        action='store_true')
    parser.add_argument('--prod',
                        help="Whether or not to run in prod mode.",
                        default=False,
                        action='store_true')

    parser.add_argument('--no_log',
                        help="Whether to not keep logs.",
                        default=False,
                        action='store_true')

    args = parser.parse_args()
    main(args)