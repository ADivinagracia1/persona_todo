# Task object for P5 todo app
# Note: "models" are tanginle objects in the program

from typing import Optional
from dataclasses import dataclass
from datetime import date, datetime
from models.Category import Category # Category file, Category class

@dataclass
class Task:
# Data Class    

    # Class Fields 
    #   - not needed to initialize because of @dateclass
    #   - no need for __init__ since Task is a data class
    title:          str
    description:    str
    category:       Category
    date_created:   date
    date_due:       Optional[date]
    reoccuring:     bool = False
    completed:      bool = False
    
    # Note: want to be able to edit already created tasks
    # - get/set are boiler plate code 
    #   - used for interfacig, necesary but not actual functions
