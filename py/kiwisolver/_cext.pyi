# --------------------------------------------------------------------------------------
# Copyright (c) 2021, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# --------------------------------------------------------------------------------------

from typing import Any, Iterable, NoReturn, Tuple, type_check_only

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal  # type: ignore

__version__: str
__kiwi_version__: str

# Types
@type_check_only
class Strength:
    @property
    def weak(self) -> float: ...
    @property
    def medium(self) -> float: ...
    @property
    def strong(self) -> float: ...
    @property
    def required(self) -> float: ...
    def create(
        self,
        a: int | float,
        b: int | float,
        c: int | float,
        weight: int | float = 1.0,
        /,
    ) -> float: ...

# This is meant as a singleton and users should not access the Strength type.
strength: Strength

class Variable:
    """Variable to express a constraint in a solver."""

    __hash__: None  # type: ignore
    def __init__(self, name: str = "", context: Any = None, /) -> None: ...
    def name(self) -> str:
        """Get the name of the variable."""
        ...
    def setName(self, name: str, /) -> Any:
        """Set the name of the variable."""
        ...
    def value(self) -> float:
        """Get the current value of the variable."""
        ...
    def context(self) -> Any:
        """Get the context object associated with the variable."""
        ...
    def setContext(self, context: Any, /) -> Any:
        """Set the context object associated with the variable."""
        ...
    def __neg__(self) -> Term: ...
    def __add__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __radd__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __sub__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __rsub__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __mul__(self, other: float) -> Term: ...
    def __rmul__(self, other: float) -> Term: ...
    def __truediv__(self, other: float) -> Term: ...
    def __rtruediv__(self, other: float) -> Term: ...
    def __eq__(self, other: float | Variable | Term | Expression) -> Constraint: ...  # type: ignore
    def __ge__(self, other: float | Variable | Term | Expression) -> Constraint: ...
    def __le__(self, other: float | Variable | Term | Expression) -> Constraint: ...
    def __ne__(self, other: Any) -> NoReturn: ...
    def __gt__(self, other: Any) -> NoReturn: ...
    def __lt__(self, other: Any) -> NoReturn: ...

class Term:
    """Product of a variable by a constant pre-factor."""

    __hash__: None  # type: ignore
    def __init__(
        self, variable: Variable, coefficient: int | float = 1.0, /  # noqa
    ) -> None: ...
    def coefficient(self) -> float:
        """Get the coefficient for the term."""
        ...
    def variable(self) -> Variable:
        """Get the variable for the term."""
        ...
    def value(self) -> float:
        """Get the value for the term."""
        ...
    def __neg__(self) -> Term: ...
    def __add__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __radd__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __sub__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __rsub__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __mul__(self, other: float) -> Term: ...
    def __rmul__(self, other: float) -> Term: ...
    def __truediv__(self, other: float) -> Term: ...
    def __rtruediv__(self, other: float) -> Term: ...
    def __eq__(self, other: float | Variable | Term | Expression) -> Constraint: ...  # type: ignore
    def __ge__(self, other: float | Variable | Term | Expression) -> Constraint: ...
    def __le__(self, other: float | Variable | Term | Expression) -> Constraint: ...
    def __ne__(self, other: Any) -> NoReturn: ...
    def __gt__(self, other: Any) -> NoReturn: ...
    def __lt__(self, other: Any) -> NoReturn: ...

class Expression:
    """Sum of terms and an additional constant."""

    __hash__: None  # type: ignore
    def __init__(
        self, terms: Iterable[Term], constant: int | float = 0.0, /  # noqa
    ) -> None: ...
    def constant(self) -> float:
        "" "Get the constant for the expression." ""
        ...
    def terms(self) -> Tuple[Term, ...]:
        """Get the tuple of terms for the expression."""
        ...
    def value(self) -> float:
        """Get the value for the expression."""
        ...
    def __neg__(self) -> Expression: ...
    def __add__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __radd__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __sub__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __rsub__(self, other: float | Variable | Term | Expression) -> Expression: ...
    def __mul__(self, other: float) -> Expression: ...
    def __rmul__(self, other: float) -> Expression: ...
    def __truediv__(self, other: float) -> Expression: ...
    def __rtruediv__(self, other: float) -> Expression: ...
    def __eq__(self, other: float | Variable | Term | Expression) -> Constraint: ...  # type: ignore
    def __ge__(self, other: float | Variable | Term | Expression) -> Constraint: ...
    def __le__(self, other: float | Variable | Term | Expression) -> Constraint: ...
    def __ne__(self, other: Any) -> NoReturn: ...
    def __gt__(self, other: Any) -> NoReturn: ...
    def __lt__(self, other: Any) -> NoReturn: ...

class Constraint:
    def __init__(
        self,
        expression: Expression,
        op: Literal["=="] | Literal["<="] | Literal[">="],
        strength: float
        | Literal["weak"]
        | Literal["medium"]
        | Literal["strong"]
        | Literal["required"] = "required",
        /,
    ) -> None: ...
    def expression(self) -> Expression:
        """Get the expression object for the constraint."""
        ...
    def op(self) -> Literal["=="] | Literal["<="] | Literal[">="]:
        """Get the relational operator for the constraint."""
        ...
    def strength(self) -> float:
        """Get the strength for the constraint."""
        ...
    def __or__(
        self,
        other: float
        | Literal["weak"]
        | Literal["medium"]
        | Literal["strong"]
        | Literal["required"],
    ) -> Constraint: ...
    def __ror__(
        self,
        other: float
        | Literal["weak"]
        | Literal["medium"]
        | Literal["strong"]
        | Literal["required"],
    ) -> Constraint: ...

class Solver:
    """Kiwi solver class."""

    def __init__(self) -> None: ...
    def addConstraint(self, constraint: Constraint, /) -> None:
        """Add a constraint to the solver."""
        ...
    def removeConstraint(self, constraint: Constraint, /) -> None:
        """Remove a constraint from the solver."""
        ...
    def hasConstraint(self, constraint: Constraint, /) -> bool:
        """Check whether the solver contains a constraint."""
        ...
    def addEditVariable(
        self,
        variable: Variable,
        strength: float
        | Literal["weak"]
        | Literal["medium"]
        | Literal["strong"]
        | Literal["required"],
        /,
    ) -> None:
        """Add an edit variable to the solver."""
        ...
    def removeEditVariable(self, variable: Variable, /) -> None:
        """Remove an edit variable from the solver."""
        ...
    def hasEditVariable(self, variable: Variable, /) -> bool:
        """Check whether the solver contains an edit variable."""
        ...
    def suggestValue(self, variable: Variable, value: int | float, /) -> None:
        """Suggest a desired value for an edit variable."""
        ...
    def updateVariables(self) -> None:
        """Update the values of the solver variables."""
        ...
    def reset(self) -> None:
        """Reset the solver to the initial empty starting condition."""
        ...
    def dump(self) -> None:
        """Dump a representation of the solver internals to stdout."""
        ...
    def dumps(self) -> str:
        """Dump a representation of the solver internals to a string."""
        ...
