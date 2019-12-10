#!/usr/bin/env python3
"""
Server code for memegen rojigan.
"""
import logging

from flask import Flask
from flask import request
from flask import send_from_directory
from flask import redirect
from flask import render_template
from flask import url_for


app = Flask(__name__)


links = None


@app.route('/')
def index():
    images_dir = 'static/images/'
    images_names = [
        '77412709_538950413617199_6818013205168652288_n.jpg',
        '79015809_1261120694078187_8577508787756204032_n.jpg']
    image_paths = [images_dir + images_name for images_name in images_names]
    print(image_paths)
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