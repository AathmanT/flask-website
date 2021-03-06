"""
Provides classes for describing :mod:`.corpus` or :mod:`.social` models.

.. autosummary::

   corpus
   social

The purpose of this module is to provide a common way to describe models
generated by various modeling algorithms and their sundry implementations.

To generate models from a :class:`.Corpus` and/or :class:`.GraphCollection`\,
use one of the model :mod:`.managers`\.
"""

from corpus import *
from social import *
from basemodel import *