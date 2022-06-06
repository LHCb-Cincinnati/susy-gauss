__author__ = "Mohamed Elashri <mohamed.elashri@cern.ch>"
__date__ = "2022-06-06"

# ============================================================================
from Configurables import Generation, Special, Pythia8Production

gen = Generation() 
gen.addTool( Special )
gen.Special.addTool( Pythia8Production)
gen.Special.KeepOriginalProperties = True
prod = Generation().Special.Pythia8Production

gen.PileUpTool = "FixedLuminosityForRareProcess"

prod.Commands = [
    "SUSY:qqbar2chi+-chi0 = on",
    "SUSY:qqbar2chi+chi-  = on",
    "Main:timesAllowErrors = 0",
    "SLHA:verbose = 3",
    "Print:quiet = off"
]

# ============================================================================

from Configurables import GaudiSequencer, GaussMonitor__CheckLifeTimeHepMC, GaussMonitor__CheckLifeTimeMC

GenMonitor = GaudiSequencer( "GenMonitor" )
GenMonitor.Members += [
    GaussMonitor__CheckLifeTimeHepMC("HepMCLifeTime",Particles = [
        "~chi_10"
    ]
  )
]

SimMonitor = GaudiSequencer( "SimMonitor" )
SimMonitor.Members += [
    GaussMonitor__CheckLifeTimeMC("MCLifeTime", Particles = [
        "~chi_10"
    ]
  )   
]
