from stlcpsr import parser
import stlc_ctx


def process_exp(exp, ctx, p):
    try:
        cmds = parser.parse(exp)
        for cmd in cmds:
            _, ctx = cmd.process(ctx, p)
    except Exception as e:
        print("wrong exp: ", exp)
        print(e)
    return ctx


def shell():
    ctx = stlc_ctx.Context()
    p = False
    loop = True
    exp = ""
    ln = 1
    while loop:
        line = input("{}> ".format(ln))
        ln += 1
        if line == 'detail':
            p = not p
        elif line == 'exit':
            loop = False
        elif line == 'ctx':
            print(ctx)
        elif line == 'forget':
            ctx = stlc_ctx.Context()
        elif len(line) and line.strip()[-1] == ';':
            exp = exp + line + '\n'
            ctx = process_exp(exp, ctx, p)
            exp = ""
        else:
            exp = exp + line + '\n'


if __name__ == "__main__":
    shell()
