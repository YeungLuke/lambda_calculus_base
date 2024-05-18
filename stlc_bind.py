from stlc_base import Term


class Binding:
    def __init__(self) -> None:
        pass


class NameBind(Binding):
    def __init__(self) -> None:
        super().__init__()


class TmAbbBind(Binding):
    def __init__(self, t: 'Term') -> None:
        super().__init__()
        self.t = t

    def __str__(self) -> str:
        return str(self.t)
