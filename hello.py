# -*- coding: utf-8 -*-

import aiml
import os

os.chdir('./res/alice')

alice = aiml.Kernel()

alice.learn('startup.xml')
alice.respond('LOAD ALICE')

while True:
    question = raw_input('SGH >>> ')
    if question == 'exit':
        print 'Bye-bye!'
        break

    print 'ALICE >>>', alice.respond(question)
