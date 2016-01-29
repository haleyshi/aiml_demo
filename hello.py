# -*- coding: utf-8 -*-

import aiml
import os

os.chdir('./res/alice')

alice = aiml.Kernel()

alice.learn('startup.xml')
alice.response('LOAD ALICE')

alice.respond('hello')
