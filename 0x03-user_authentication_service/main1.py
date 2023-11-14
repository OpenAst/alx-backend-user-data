#!/usr/bin/env python3
"""Main file
"""

from user import User
from db import DB

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
