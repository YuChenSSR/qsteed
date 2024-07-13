# This code is part of QSteed.
#
# (C) Copyright 2024 Beijing Academy of Quantum Information Sciences
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABC, abstractmethod
from typing import Union

from quafu import QuantumCircuit
from quafu.elements import Instruction

from qsteed.dag.dagcircuit import DAGCircuit


class BasePass(ABC):
    """
    The Metaclass for qsteed transpiler passes.
    """

    @abstractmethod
    def run(self, circuit: Union[QuantumCircuit, DAGCircuit, Instruction]):
        pass


class UnrollPass(BasePass):
    """
    The UnrollPass for qsteed transpiler unroll.
    """

    def __init__(self) -> None:
        self.rule = []
        self.parameter_type = 'constant_gate'  # or 'parameterized_gate'
        self.original = 'cx'
        self.basis = ['cx', 'rx', 'ry', 'rz', 'id']
        self.global_phase = 0

    @abstractmethod
    def run(self, circuit: Union[QuantumCircuit, DAGCircuit, Instruction]):
        pass