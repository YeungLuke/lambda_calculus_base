from typing import List, Tuple
import abc

from stlc_base import Term
from stlc_bind import Binding
from stlc_ctx import Context


class Command():
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def process(self, ctx: Context, p=False) -> Tuple[Term, Context]:
        pass


class Eval(Command):
    def __init__(self, t: Term) -> None:
        super().__init__()
        self.t = t

    def __str__(self) -> str:
        return "{}".format(self.t)

    def eval(self, t: Term, ctx=Context({}), p=False) -> Term:
        while not t.isval():
            if p:
                print(t)
            t = t.eval(ctx)
        return t

    def full_beta(self, t: Term, ctx=Context({}), p=False) -> Term:
        while True:
            if p:
                print(t)
            n = t.full_beta(ctx)
            if n == t:
                break
            t = n
        return t

    def process(self, ctx: Context, p=False) -> Tuple[Term, Context]:
        t = self.t
        t = self.eval(self.t, ctx, p)
        print("result:", t)
        r = self.full_beta(t, ctx, p)
        if r != t:
            print("full_beta:", r)
        return r, ctx


class Bind(Command):
    def __init__(self, name: str, bind: Binding) -> None:
        super().__init__()
        self.name = name
        self.bind = bind

    def __str__(self) -> str:
        return "{} = {}".format(self.name, self.bind)

    def process(self, ctx: Context, _=False) -> Tuple[Term, Context]:
        return None, ctx.addbinding(self.name, self.bind)


class Assert(Command):
    def __init__(self, t1: Term, t2: Term) -> None:
        super().__init__()
        self.c1 = Eval(t1)
        self.c2 = Eval(t2)

    def __str__(self) -> str:
        return "assert ({}) = ({})".format(self.c1, self.c2)

    def process(self, ctx: Context, p=False) -> Tuple[Term, Context]:
        print("exp: {}".format(self.c1))
        r1, ctx = self.c1.process(ctx, p)
        print("exp: {}".format(self.c2))
        r2, ctx = self.c2.process(ctx, p)
        if r1 != r2:
            raise AssertionError("({} = {}) not equal to ({} = {})".format(self.c1, r1, self.c2, r2))
        return r1, ctx


def run_cmds(cmds: List[Command], ctx=Context(), p=False) -> Term:
    t = None
    for cmd in cmds:
        print("command:", cmd)
        t, ctx = cmd.process(ctx, p)

    return t
