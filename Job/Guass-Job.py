from Gauss.Configuration import *
importOptions("$APPCONFIGOPTS/Gauss/Beam6500GeV-md100-2017-nu1.6.py")
importOptions("$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py")
importOptions("$APPCONFIGOPTS/Gauss/DataType-2017.py")
importOptions("$APPCONFIGOPTS/Gauss/RICHRandomHits.py")
importOptions("$DECFILESROOT/options/46000214.py")
importOptions("$LBPYTHIA8ROOT/options/Pythia8.py")
importOptions("$GAUSSOPTS/GenStandAlone.py")

GaussGen = GenInit("GaussGen")
GaussGen.FirstEventNumber = 1
GaussGen.RunNumber = 1082

from Configurables import LHCbApp
LHCbApp().DDDBtag = 'dddb-20170721-3'
LHCbApp().CondDBtag = 'sim-20170721-2-vc-md100'
LHCbApp().EvtMax = 3
