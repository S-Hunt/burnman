# BurnMan - a lower mantle toolkit
# Copyright (C) 2012, 2013, Heister, T., Unterborn, C., Rose, I. and Cottaar, S.
# Released under GPL v2 or later.

"""
Other minerals
^^^^^^^^^^^^^^

"""

import burnman.mineral_helpers as bmb
from burnman.mineral import Mineral

from SLB_2011 import periclase, wuestite


class ferropericlase(bmb.HelperSolidSolution):
    def __init__(self, fe_num):
        base_materials = [periclase(), wuestite()]
        molar_fraction = [1. - fe_num, 0.0 + fe_num] # keep the 0.0 +, otherwise it is an array sometimes
        bmb.HelperSolidSolution.__init__(self, base_materials, molar_fraction)


class Speziale_fe_periclase(bmb.HelperSpinTransition):
    def __init__(self):
        bmb.HelperSpinTransition.__init__(self, 60.0e9, Speziale_fe_periclase_LS(), Speziale_fe_periclase_HS())
        self.cite = 'Speziale et al. 2007'


class Speziale_fe_periclase_HS(Mineral):
    """
    Speziale et al. 2007, Mg#=83
    """
    def __init__(self):
        self.params = {
                        'equation_of_state': 'mgd3',
                        'V_0': 22.9e-6,
                        'K_0': 157.5e9,
                        'Kprime_0': 3.92,
                        'molar_mass': .04567,
                        'n': 2,
                        'Debye_0': 587,
                        'grueneisen_0': 1.46,
                        'q_0': 1.2 }
        Mineral.__init__(self)

class Speziale_fe_periclase_LS(Mineral):
    """
    Speziale et al. 2007, Mg#=83
    """
    def __init__(self):
        self.params = {
                        'equation_of_state': 'mgd3',
                        'V_0': 21.49e-6,
                        'K_0': 186.0e9,
                        'Kprime_0': 4.6,
                        'molar_mass': .04567,
                        'n': 2,
                        'Debye_0': 587.,
                        'grueneisen_0': 1.46,
                        'q_0': 1.2  }
        Mineral.__init__(self)






