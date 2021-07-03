import yaml


def profile_read(p_file_path):
    """
    create a tree of dictionaries as per
    a profile determined
    """

    def parse_profile():
        """Parses a profile in json format"""

        try:
            stream = open(p_file_path)
            d = yaml.safe_load(stream)
            return d['profile']
        except (yaml.YAMLError, KeyError, OSError, IOError) as e:
            _logger.error(e)
            _logger.fatal("malformed profile file in: {0}".format(p_file_path))
            raise
        finally:
            stream.close()

    pt = parse_profile()
    pt['source'] = p_file_path
    return pt
