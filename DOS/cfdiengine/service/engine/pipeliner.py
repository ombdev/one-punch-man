import os
import json
import sys
from misc.tricks import dump_exception
from engine.error import ErrorCode

class PipeLiner(object):

    @classmethod
    def maneuver_req(cls, pt, req, adapter=None):
        """"""
        def apply_adapter():
            if adapter is not None:
                return adapter()
            # So we assumed request are bytes of a json string
            json_lines = req.decode(encoding='UTF-8')
            return json.loads(json_lines)

        d = apply_adapter()
        try:
            action = d['req']['action']
            args = d['req']['args']

            if not hasattr(cls, action):
                msg = "module {0} has no handler {1}".format(business_mod, action)
                raise RuntimeError(msg)

            handler = getattr(cls, action)
            return handler(logger, pt, args)
        except (RuntimeError) as e:
            _logger.fatal("support module failure {}".format(e))
            return ErrorCode.ACTION_NOT_MANEUVERED.value
        except:
            _logger.error(dump_exception())
            return ErrorCode.ACTION_UNEXPECTED_FAIL.value
