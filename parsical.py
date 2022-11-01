#!/usr/local/bin/python3
# **************************************************************************** #
# This file is part of cmdutils: https://github.com/fdch/cmdutils
# Copyright (C) 2022 Fede Camara Halac
# **************************************************************************** #
# -*- coding: utf-8 -*-
""" Parse ical file and spit out a CSV list to console. """

# import pprint
import icalendar
from dateutil.rrule import *
import sys

count=0
cut_at=100000 # ie, nonstop

with open(sys.argv[1], 'rb') as icalfile:
    gcal = icalendar.Calendar.from_ical(icalfile.read())

    print("name, date, video1, chat1, video2, chat2, a1, a2, a3, a4, a6, a7")

    for component in gcal.walk():
        if count > cut_at: 
            break
        if component.name == "VEVENT":
            count += 1
            summary = component.get('summary')
            description = component.get('description')
            location = component.get('location')
            startdt = component.get('dtstart').dt
            enddt = component.get('dtend').dt
            exdate = component.get('exdate')

            # get the attatchments
            attachments = component.get('attach')

            a = summary
            if startdt:
                a += ", " + startdt.strftime("%D")
            if attachments:
                # pprint.pprint(attachments)
                if isinstance(attachments, list):
                    for x in attachments:
                        # if "document" not in x:
                        a += ", " + x
                else:
                    a += ", " + attachments
            print(a)