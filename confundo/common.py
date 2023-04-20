# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-
# Copyright 2019 Alex Afanasyev
#


MTU = 412

MAX_SEQNO = 50000

RETX_TIME = 0.5

FIN_WAIT_TIME = 2.0

SYN_WAIT_TIME = 10.0

INIT_SSTHRESH = 12000

GLOBAL_TIMEOUT = 10.0

"""
This code defines a set of constants that are likely being used in a network communication protocol implementation. 
Here's what each constant represents:

MTU: the Maximum Transmission Unit size, which is the largest size of a packet that can be transmitted over a network 
link.

MAX_SEQNO: the maximum sequence number that can be used in the protocol. This value is used to avoid sequence number 
wrapping around.

RETX_TIME: the retransmission time, which is the amount of time the sender waits before resending a packet that has not 
been acknowledged.

FIN_WAIT_TIME: the time the sender waits for a FIN packet from the receiver before closing the connection.

SYN_WAIT_TIME: the time the sender waits for a SYN-ACK packet from the receiver before retransmitting the SYN packet.

INIT_SSTHRESH: the initial slow start threshold. Slow start is a congestion control algorithm used to gradually increase
the amount of data sent over the network, and this value determines when to switch from slow start to congestion 
avoidance.

GLOBAL_TIMEOUT: the global timeout, which is the maximum amount of time the sender waits for an acknowledgement from the
receiver before assuming the packet was lost and resending it.

"""