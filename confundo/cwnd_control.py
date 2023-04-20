# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
# Copyright 2019 Alex Afanasyev
#

from common import *


class CwndControl:
    '''Interface for the congestio control actions'''

    def __init__(self):
        self.cwnd = 1.0 * MTU
        self.ssthresh = INIT_SSTHRESH

    def on_ack(self, ackedDataLen):
        if self.cwnd < self.ssthresh:
            # Slow start
            self.cwnd += MTU
        elif self.cwnd >= self.ssthresh:
            # Congestion avoidance
            self.cwnd += (MTU * MTU) / self.cwnd

    def on_timeout(self):
        self.ssthresh = self.cwnd/2
        self.cwnd = MTU

    def __str__(self):
        return f"cwnd:{self.cwnd} ssthreash:{self.ssthresh}"
