from stlcpsr import parser
import stlc_cmd


def run(e: str, p=False):
    cmds = parser.parse(e)
    res = stlc_cmd.run_cmds(cmds, p=p)
    print("")
    return res
