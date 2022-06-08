"""
@file

Main configuration file for long-lived Dissaperance Tracks analysis

pp->( ~chi_1+ -> ~chi_10 pi+ )

Concrete dec files can specify a parameter point by setting the SLHA spectrum file

@code
#
# InsertPythonCode
# 
# Generation().Special.Pythia8Production.Commands.append("SLHA:file MyModelSpectrum.slha")
# 
# EndInserPythonCode
#
@endcode

@author Mohamed Elashri <mohamed.elashri@cern.ch>
@date 2022-06-06
"""
__author__ = "Mohamed Elashri <mohamed.elashri@cern.ch>"
__date__ = "2022-06-06"

# ============================================================================
from Configurables import Generation, Special, Pythia8Production, PythiaLSP
gen = Generation() 
gen.addTool( Special )
gen.Special.addTool( Pythia8Production)
gen.Special.KeepOriginalProperties = True
gen.addTool( Special )
prod = Generation().Special.Pythia8Production

#Pile-up and luminosity
gen.PileUpTool = "FixedLuminosityForRareProcess"


prod.Commands = [
    #"SUSY:all = on",
    "SUSY:qqbar2chi+-chi0 = on",
    "SUSY:qqbar2chi+chi-  = on",
    "Main:timesAllowErrors = 10",
    "SLHA:verbose = 3",
    "Print:quiet = off",
    "HadronLevel:Hadronize = off",
    "PartonLevel:FSR = off"
]


