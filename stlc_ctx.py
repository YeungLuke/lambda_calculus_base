import copy
from typing import Dict

from stlc_base import Term
from stlc_bind import Binding, TmAbbBind


class Context:
    def __init__(self, c: Dict[str, Binding] = {}) -> None:
        super().__init__()
        self.c = c

    def __contains__(self, key: str) -> bool:
        return key in self.c

    def __str__(self) -> str:
        return '\n'.join(["{} = {};".format(k, b) for k, b in self.c.items()])

    def addbinding(self, x: str, bind: Binding) -> 'Context':
        c = copy.copy(self.c)
        c[x] = bind
        return Context(c)
    
    def removebinding(self, x: str) -> 'Context':
        c = copy.copy(self.c)
        c.pop(x, None)
        return Context(c)

    def getbinding(self, x: str) -> Binding:
        if x in self.c:
            return self.c[x]
        raise LookupError("{} not in cxt {}".format(x, list(self.c.keys())))

    def getterm(self, x: str) -> 'Term':
        bind = self.getbinding(x)
        if isinstance(bind, TmAbbBind):
            return bind.t
        raise TypeError("getterm: Wrong kind of binding for variable {} {}".format(x, bind))
