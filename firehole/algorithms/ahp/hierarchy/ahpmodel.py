# -*- coding: utf-8 -*-
"""ahp.hierarchy.ahpmodel

This module contains the class definition for the AHP Model Node (root) in the hierarchy model.
"""

import numpy as np

from firehole.algorithms.ahp.hierarchy import AHPCriterion
from firehole.algorithms.ahp.methods import EigenvalueMethod
from firehole.algorithms.ahp.utils import normalize_priorities


class AHPModel:
    """AHPModel

    Args:
        model (dict): The Analytic Hierarchy Process model.
        solver (ahp.methods): Method used when calculating the priorities of the lower layer.
    """

    def __init__(self, model, solver=EigenvalueMethod):
        self.solver = solver()
        self.preference_matrices = model['preferenceMatrices']

        criteria = model.get('criteria')
        self.criteria = [AHPCriterion(n, model, solver=solver) for n in criteria]

    def get_priorities(self, round_results=True, decimals=3):
        """Get the priority of the nodes in the level below this node.

        Args:
            round_results (bool): Return rounded priorities. Default is True.
            decimals (int): Number of decimals to round to, ignored if `round_results=False`. Default is 3.

        Returns:
            Global priorities of the alternatives in the model, rounded to `decimals` positions if `round_results=True`.
        """
        crit_pm = np.array(self.preference_matrices['criteria'])
        crit_pr = self.solver.estimate(crit_pm)

        crit_attr_pr = [criterion.get_priorities() for criterion in self.criteria]
        priorities = normalize_priorities(crit_attr_pr, crit_pr)

        if round_results:
            return np.around(priorities, decimals=decimals)

        return priorities
