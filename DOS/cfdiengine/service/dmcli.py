import argparse
import logging
import os
import sys
from engine.error import FatalError
from custom.profconf import profile_read


_logger = logging.getLogger(__name__)


def _dmcli(args):

    def env_property(prop):
        """Read env variables for microservice's sake"""
        val = os.environ.get(prop)
        if val:
            return val
        raise FatalError("Enviroment variable {} has not been set !!".format(prop))

    def read_settings(s_file):
        _logger.debug("looking for config profile file in:\n{0}".format(
            os.path.abspath(s_file)))
        if os.path.isfile(s_file):
            return profile_read(s_file)
        raise Exception("unable to locate the config profile file")

    RESOURCES_DIR = os.path.join(env_property('BASE_DIR'), 'resources')

    if not os.path.isdir(RESOURCES_DIR):
        msg = 'We can not go ahead without a resource directory'
        sys.exit(msg)

    PROFILES_DIR = os.path.join(RESOURCES_DIR, 'profiles')

    if not os.path.isdir(PROFILES_DIR):
        msg = 'We can not go ahead without a profile directory'
        sys.exit(msg)

    PROFILE_PATH = '{}.yaml'.format(os.path.join(PROFILES_DIR, args.config))

    if not os.path.exists(PROFILE_PATH):
        msg = 'We can not go ahead without a profile'
        sys.exit(msg)

    pt = read_settings(PROFILE_PATH)

    if not args.dm_output:
        raise Exception("not defined output file")

    if args.dm_builder:
        if not args.dm_input:
            raise Exception("not defined input variables")

        kwargs = dict([])
        try:
            if args.dm_input.find(';') == -1:
                raise Exception("input variables bad conformed")
            else:
                for opt in args.dm_input.split(';'):
                    if opt.find('=') == -1:
                        continue
                    (k , v) = opt.split('=')
                    kwargs[k] = v
        except ValueError:
            raise Exception("input variables bad conformed")

        try:
            builder(RESOURCES_DIR, pt['res']['dirs'],
                    args.dm_builder, args.dm_output, **kwargs)
        except:
            raise Exception("problems in document builder")
    else:
        raise Exception("builder module not define")


def _set_cmdargs_up():
    """parses the cmd line arguments at the call"""

    psr_desc='Document maker command line control interface'
    psr_epi='The config profile is used to specify defaults'

    psr = argparse.ArgumentParser(description=psr_desc, epilog=psr_epi)

    psr.add_argument('-d', '--debug', action='store_true',
                     dest='dm_debug', help='print debug information')
    psr.add_argument('-c', '--config', action='store', default='basic',
                     dest='config', help='load an specific config profile')
    psr.add_argument('-b', '--builder',
                     dest='dm_builder', help='specify the builder to use')
    psr.add_argument('-i', '--input', dest='dm_input',
                     help='specify the input variables with \'var=val;var2=val2;var2=valN\'..')
    psr.add_argument('-o', '--output', dest='dm_output', help='specify the output file')

    return psr.parse_args()


if __name__ == "__main__":

    args = _set_cmdargs_up()

    try:
        logging.basicConfig(level=logging.DEBUG if args.dm_debug else logging.INFO)
        _logger.debug(args)
        _dmcli(args)
        _logger.info('successful builder execution')
    except:
        if args.dm_debug:
            traceback.print_exc()
        sys.exit(1)

    sys.exit(0)
