import os
import json
import sys
from misc.tricks import dump_exception
from engine.error import ErrorCode


class PipeLiner(object):

    @staticmethod
    def factura(pt, req):
        pass

    @staticmethod
    def pago(pt, req):
        pass

    @staticmethod
    def nota_cred(pt, req):
        pass

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
            motive = d['req']['motive']
            content = d['req']['content']

            if not hasattr(cls, motive):
                msg = "The {0} has no motive {1}".format(cls.__name__, motive)
                raise RuntimeError(msg)

            return getattr(cls, motive)(pt, content)
        except (RuntimeError) as e:
            _logger.fatal("support module failure {}".format(e))
            return ErrorCode.MOTIVE_NOT_MANEUVERED.value
        except:
            _logger.error(dump_exception())
            return ErrorCode.MOTIVE_UNEXPECTED_FAIL.value
