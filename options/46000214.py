# This is the output which should be correct (to make .dec produce this is still under development)

# file /afs/cern.ch/user/m/melashri/private/susy-sim/GaussDev_v49r21/Gen/DecFiles/options/46000214.py generated: Mon, 06 Jun 2022 09:49:46
#
# Event Type: 46000214
#
# ASCII decay Descriptor: pp -> (~chi_1+ -> ~chi_10  pi+ ' )
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DissTracks.py" )
from Configurables import Generation
Generation().EventType = 46000214
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "Pythia8Production"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/DissTracks_100GeV_mAMSB.dec"
Generation().Special.CutTool = ""
# To-Do
#Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/Chi10InAccMuInAcc"
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/SusyBRpV.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHASpectrumFile = "DissTracks_100GeV_mAMSB.LHspc"
from Configurables import PythiaLSP
Generation().Special.addTool( PythiaLSP )
Generation().Special.PythiaLSP.LSPID = [ 1000022, 1000024 ]
from Configurables import LoKi__FullGenEventCut
## To-Do
#Generation().addTool( LoKi__FullGenEventCut, "Chi10InAccMuInAcc" )
#GenLevelSelection = Generation().Chi10InAccMuInAcc
""" GenLevelSelection.Preambulo += [
      "from GaudiKernel.SystemOfUnits import GeV, mrad, mm, meter"
    , "GEVZ                   =  GFAEVX( GVZ, LoKi.Constants.InvalidDistance )"
    , "GEVRHO                 =  GFAEVX( GVRHO, LoKi.Constants.HugeDistance )"
    , "inAcceptance           = ( GTHETA < 400.*mrad ) & ( GP > 2.0*GeV )"
    , "isNeutralino           = ( '~chi_10' == GABSID )"
    , "isChargino             = ( '~chi_1+' == GABSID )"
]
"""
from Configurables import GenerationToSimulation 
GenerationToSimulation("GenToSim").KeepCode = "( '~chi_1+' == GABSID )" # Keep MCParticles Charginos
### Particle properties
spcFileName = "$DECFILESROOT/lhafiles/DissTracks_100GeV_mAMSB.LHspc"
specialSusyParticles = [ "1000022","1000024" ]

import sys,os
sys.path.append(os.path.expandvars("$DECFILESROOT/scripts/"))
from SuSySLHAFunctions import getParticlePropertiesAndPythia8Commands
pps, ppCommands = getParticlePropertiesAndPythia8Commands(spcFileName, specialSusyParticles)

Generation().Special.Pythia8Production.Commands += [
      "SLHA:file            %s" % spcFileName
    , "SLHA:useDecayTable = true"
    ] + ppCommands

from Configurables import LHCb__ParticlePropertySvc