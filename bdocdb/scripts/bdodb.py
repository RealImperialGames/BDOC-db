# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""TODO: doc module"""


import argparse
import logging
import logging.handlers
import os
import sys
from bdocdb.configs import SETTINGS
from bdoccore.commands import CommandModule


def main(args=None):
    """Script start

    Keyword Arguments:
        args {dict} -- arguments from cmd or dict from another
            code (default: {None})
    """
    if args is None:
        args = sys.argv[1:]
    # Generate parser
    parser = parser_instance()
    args = parser.parse_args()
    # Generate logger
    logger = logger_instance(args)
    # START SCRIPT
    if args.action == 'install':
        command_install(logger, args)
    elif args.action == 'start':
        command_start(logger, args)
    else:
        logger.error(
            str(SETTINGS.MSG_UNKOWN_COMMAND.format(args)))


def parser_instance():
    """TODO: doc method"""
    parser = argparse.ArgumentParser(
        description="Performs BDOC-db operations",
        epilog="----- Imperial Games, module: BDOC-db -------",
        fromfile_prefix_chars='@',)
    # Main args
    parser.add_argument(
        '-v', '--verbose',
        action="count", help="verbose level... repeat up to three times.")
    parser.add_argument(
        '-a', '--action',
        default=None,
        help="Select available action, values are: [install, start]")
    # Optional args
    parser.add_argument(
        '-c', '--config_path',
        default=None,
        help="Use different absolute PATH+FILE_NAME to read JSON config file")
    return parser


def logger_instance(args):
    """Logger instantiation for script

    Arguments:
        args {dict} -- arguments from cmd

    Returns:
        logging.Logger -- Logger instance to be used
    """
    # configuration
    msg_file_formatter = "{} [{}]({}:{}:{}): {}".format(
        "%(asctime)s", "%(levelname)s", "%(name)s",
        "%(funcName)s", "%(lineno)d", "%(message)s"
    )
    msg_console_formatter = '[%(levelname)s](%(name)s): %(message)s'
    logger_name = 'bdodatabase'
    logger_file_name = '{}.log'.format(logger_name)
    logger = logging.getLogger(logger_name)
    logger_output_dir = '../logs'
    logger_output_path = "{}/{}".format(
        logger_output_dir, logger_file_name)
    # creation
    if not os.path.exists(logger_output_dir):
        os.mkdir('../logs')
    # all loggers
    logger.setLevel(logging.DEBUG)
    # file logger handler
    log_file_handler = logging.handlers.TimedRotatingFileHandler(
        logger_output_path, when='M', interval=2)
    log_file_handler.setFormatter(logging.Formatter(msg_file_formatter))
    log_file_handler.setLevel(logging.DEBUG)
    logger.addHandler(log_file_handler)
    # console logger handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(msg_console_formatter))
    logger.addHandler(console_handler)
    set_log_level_from_verbose(console_handler, args, logger)
    return logger


def command_install(logger, args):
    """Command for install BDOC-db

    Arguments:
        logger {logging.Logger} -- class logger to log messages
        args {dict} -- arguments dict from cmd
    """
    args_dict = {"action": args.action}
    command = CommandModule(logger, **args_dict)
    command.install()


def command_start(logger, args):
    """Command for install BDOC-db

    Arguments:
        logger {logging.Logger} -- class logger to log messages
        args {dict} -- arguments dict from cmd
    """
    args_dict = {"action": args.action}
    command = CommandModule(logger, **args_dict)
    command.start()


def set_log_level_from_verbose(console_handler, args, logger):
    """Set logging level handler for script"""
    if not args.verbose:
        console_handler.setLevel("INFO")
    elif args.verbose == 1:
        console_handler.setLevel('WARNING')
    elif args.verbose == 2:
        console_handler.setLevel('INFO')
    elif args.verbose >= 3:
        console_handler.setLevel('DEBUG')
    else:
        logger.critical("LOGGER level doesn't exist")


if __name__ == '__main__':
    main()