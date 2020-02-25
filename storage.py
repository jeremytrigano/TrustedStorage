#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import sqlite3
import datetime


class DatetimeEventStore:
    def store_event(self, at, data):
        connection = self.__con_db()
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO storage (tsevent, dataevent) VALUES (?, ?)""",
            (at, data),
        )
        connection.commit()
        self.__discon_db(connection)
        return at, data

    def get_events(self, start, end):
        if isinstance(start, datetime.datetime) and isinstance(
            end, datetime.datetime
        ):
            connection = self.__con_db()
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT * FROM 'storage' WHERE tsevent > '{start}' AND tsevent < '{end}'",
            )
            records = cursor.fetchall()
            self.__discon_db(connection)
        return records

    def __con_db(self):
        return sqlite3.connect("events.db")

    def __discon_db(self, dbname):
        dbname.close()
