#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/25 19:05
# @File  : conftest.py
# __author__ = 'yangyanqin'

import os
import shlex
import signal
import subprocess

import pytest


@pytest.fixture(scope="class", autouse=True)
def record_vedio():
    cmd = "scrcpy -m 1024 --record file.mp4"
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # print(p)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
