
from django.contrib.auth.models import User

from django.db import models

def _(name): return name

fivepoints = (
              ('5', "Excellent"),
              ('4', "Good"),
              ('3', "Average"),
              ('2', "Poor"),
              ('1', "Very Bad"),
              ('0', "No Comment"),
             )

class Survey1(models.Model):
    """A Survey1 represents the answers to that sort of survey form
    """
    user      = models.ForeignKey(User)
    stamp     = models.DateTimeField(auto_now_add=True)
    uses_wifi = models.CharField(max_length=8, choices=(
                                 ('YES'     , "Yes"),
                                 ('NONEED'  , "Don't need it"),
                                 ('CANT'    , "Can't make it work"),
                                 ('COVERAGE', "Can't get a good signal"),
                                ))
    coverage  = models.CharField(max_length=1, choices=fivepoints)
    speed     = models.CharField(max_length=1, choices=fivepoints)
    where     = models.TextField()
    whereelse = models.TextField()
    what      = models.CharField(max_length=8, choices=(
                                 ('LAPTOP', "Laptop"),
                                 ('WINCE' , "Windows PDA"),
                                 ('IPOD'  , "Apple iPOD"),
                                 ('PDA'   , "Other PDA"),
                                 ('IPHONE', "Apple iPHONE"),
                                 ('BERRY' , "Blackberry"),
                                 ('PHONE' , "Other Mobile Phone"),
                                 ('NONE'  , "Not Applicable"),
                                ))
    whos      = models.CharField(max_length=8, choices=(
                                 ('DEPT' , "Department/Institute"),
                                 ('GRANT', "Grant suplied"),
                                 ('WORK' , "Other work supplied"),
                                 ('OWN'  , "My own"),
                                 ('NONE' , "Not Applicable"),
                                ))
    admins    = models.CharField(max_length=8, choices=(
                                 ('ITS'  , "IT Support"),
                                 ('DEPT' , "Department/Institute"),
                                 ('GROUP', "Group IT support"),
                                 ('WORK' , "Other work supplied"),
                                 ('ME'   , "I do it myself"),
                                 ('NONE' , "Not Applicable"),
                                ))
    comments  = models.TextField()

