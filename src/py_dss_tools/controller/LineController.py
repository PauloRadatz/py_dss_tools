# -*- encoding: utf-8 -*-
"""
 Created by Ênio Viana at 08/10/2021 at 20:17:24
 Project: py-dss-tools [out, 2021]
"""
from py_dss_tools.model.pdelement import Line
from py_dss_tools.service.pdelement.LineService import LineService


class LineController:

    @staticmethod
    def save(line: Line):
        return LineService.save(line)


