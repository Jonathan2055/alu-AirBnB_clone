#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone project
"""

import cmd
import shlex
import ast
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

