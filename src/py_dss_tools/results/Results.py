# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : Results.py
# @Software: PyCharm


from py_dss_tools.results.SnapShot.SnapShotPowerFlowResults import SnapShotPowerFlowResults
from py_dss_tools.results.TimeSeries.TimeSeriesPowerFlowResults import TimeSeriesPowerFlowResults
from py_dss_tools.results.ShortCircuit.FaultResults import FaultResults
from py_dss_interface import DSS


class Results(SnapShotPowerFlowResults, TimeSeriesPowerFlowResults, FaultResults):

    def __init__(self, dss: DSS):
        self._dss = dss
        SnapShotPowerFlowResults.__init__(self, self._dss)
        TimeSeriesPowerFlowResults.__init__(self, self._dss)
        FaultResults.__init__(self, self._dss)
