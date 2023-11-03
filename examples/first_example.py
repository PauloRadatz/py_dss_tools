# -*- coding: utf-8 -*-
# @Author  : Paulo Radatz
# @Email   : paulo.radatz@gmail.com
# @File    : first_example.py
# @Software: PyCharm

import os
import pathlib
import py_dss_tools

script_path = os.path.dirname(os.path.abspath(__file__))

dss_file = pathlib.Path(script_path).joinpath("feeders", "13Bus", "IEEE13Nodeckt.dss")

study = py_dss_tools.create_scenario(name="Test", dss_file=str(dss_file))
study.dss_command("New EnergyMeter.M element=Transformer.Sub terminal=1")
# study.create_model_dataframes()
# study.dss_command("new line.test bus1=source bus2=B")
# study.update_model_dataframes()

study.solve_snapshot()

study.allocate_load()
study.solve_snapshot()

voltages = study.results.voltages[0]


study.plot_profile()