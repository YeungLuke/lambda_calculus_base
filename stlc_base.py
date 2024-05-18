from typing import Set
import abc


class Term:
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass

    @abc.abstractmethod
    def __eq__(self, o: object) -> bool:
        pass

    @abc.abstractmethod
    def isval(self) -> bool:
        pass

    @abc.abstractmethod
    def eval(self, _) -> 'Term':
        pass

    @abc.abstractmethod
    def full_beta(self, _) -> 'Term':
        pass

    def subst(self, v: str, t: 'Term') -> 'Term':
        return self

    def fv(self) -> Set[str]:
        return set()
