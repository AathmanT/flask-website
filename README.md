# flask-website  

## tethne only works for Python 2.7  

## tethne problems  

When tethne is installed using "pip install tethne" only the 0.8 version is installed

But this code will give error for this version  
dtm = tethne.model.corpus.dtmmodel.from_gerrish('data/' + conference + '/output/','data/' + conference + '/metadata.dat','data/' + conference + '/vocabulary.dat')

copy the model folder given in the tethne fix folder and paste it into data/venv/Lib/site-packages/tethene
And hit replace button when copying

then edit the __init__.py file in tethne folder like this.  

from tethne.classes.paper import Paper  
from tethne.classes.corpus import Corpus  
from tethne.classes.streaming import StreamingCorpus  
from tethne.classes.feature import Feature, FeatureSet, \  
                                   StructuredFeature, StructuredFeatureSet  
from tethne.classes.graphcollection import GraphCollection  
from tethne.networks.base import *  
from tethne.networks.authors import *  
from tethne.networks.papers import *  
from tethne.networks.features import *  
from tethne.writers.graph import write_graphml, write_csv  
from tethne.writers.corpus import write_documents, write_documents_dtm  
#from tethne.model.corpus.mallet import LDAModel  
from model import *  
from tethne.utilities import tokenize, normalize  

## plotnine installation problems  
if installing plotnine gives error
manually download   
shapely,    
fiona,   
pyproj   
from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj
