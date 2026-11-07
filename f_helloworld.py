import sys
import logging
import ctypes

"""
F Hello World
- Fireflame_13
"""


variables = {}
debug = False

V_PRINT = print
def print(*args, **kwargs):
    global debug
    if debug:
        V_PRINT(*args, **kwargs)

V_TYPE = type

def type_(arg):
    cls = arg.__class__
    if cls == V_INT:
        return int_
    elif cls == V_FLOAT:
        return float_
    elif cls == V_STRING:
        return str_
    elif cls == V_LIST:
        return list_
    elif cls == V_DICT:
        return dict_
    elif cls == V_TUPLE:
        return tuple_
    elif cls == V_SET:
        return set_
    else:
        return cls

type = type_

V_INT = int
V_FLOAT = float
V_STRING = str
V_LIST = list
V_DICT = dict
V_TUPLE = tuple
V_SET = set

class int_(int):
    def __new__(cls, *args):
        return V_INT(*args)

class float_(float):
    def __new__(cls, *arg):
        return V_FLOAT(*arg)

class str_(str):
    def __new__(cls, *arg):
        return V_STRING(*arg)

class list_(list):
    def __new__(cls, *arg):
        return V_LIST(*arg)

class dict_(dict):
    def __new__(cls, *arg):
        return V_DICT(*arg)

class tuple_(tuple):
    def __new__(cls, *arg):
        return V_TUPLE(*arg)

class set_(set):
    def __new__(cls, *arg):
        return V_SET(*arg)

int = int_
float = float_
str = str_
list = list_
dict = dict_
tuple = tuple_
set = set_

def arithmeticSequenceGenerator(start, finish, interval=1):
    def generator(start, finish, interval):
        variable.newvar("arithmeticSequenceGenerator_n", start)
        if start > finish:
            if interval > 0:
                error.valueerror("'interval' must be lesser than zero when 'start' is greater than 'finish'")
                return None
        if start < finish:
            if interval < 0:
                error.valueerror("'interval' must be greater than zero when 'start' is lesser than 'finish'")
                return None
        if start == finish:
            return [start]
        if interval == 0:
            if start != finish:
                error.valueerror("'start' must be not equal to 'finish' when 'interval' is zero'")
                return None
        while boolean.true:
            if variable.getvar("arithmeticSequenceGenerator_n") >= finish:
                break
            yield variable.getvar("arithmeticSequenceGenerator_n")
            variable.setvar(
                "arithmeticSequenceGenerator_n",
                variable.getvar("arithmeticSequenceGenerator_n") + interval
            )

    generator_return = generator(start, finish, interval)
    generator_list = list(generator_return)
    return generator_list


def new(object_, *init):
    return object_(init)


def operator(arg1, arg2, opr):
    cls1 = numOperation(arg1)
    cls2 = numOperation(arg2)

    def class_opr(arg1, arg2, opr):
        isint = boolean.true
        if type(arg1) is not int:
            isint = boolean.false
        if type(arg2) is not int:
            isint = boolean.false

        if opr == "+":
            if isint:
                return numOperation.int_add(arg1, arg2)
            else:
                return py_operation.add(arg1, arg2)

        if opr == "-":
            if isint:
                return numOperation.int_sub(arg1, arg2)
            else:
                return py_operation.sub(arg1, arg2)

        if opr == "*":
            if isint:
                return numOperation.int_mul(arg1, arg2)
            else:
                return py_operation.mul(arg1, arg2)

        if opr == "/":
            if isint:
                return numOperation.int_div(arg1, arg2)
            else:
                return py_operation.div(arg1, arg2)

        if opr == "**":
            return arg1 ** arg2

        if opr == "%":
            return arg1 % arg2

    fcls = class_opr(cls1, cls2, opr)
    return fcls.getValue()

class py_operation:

    @classmethod
    def add(cls, arg1, arg2):
        return arg1.__add__(arg2)

    @classmethod
    def sub(cls, arg1, arg2):
        return arg1.__sub__(arg2)

    @classmethod
    def mul(cls, arg1, arg2):
        return arg1.__mul__(arg2)

    @classmethod
    def div(cls, arg1, arg2):
        return arg1.__truediv__(arg2)


class numOperation:
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def valueType(self):
        return type(self.value)

    @classmethod
    def int_add(cls, x, y):
        num1 = x
        num2 = y

        if type(x) is not int:
            error.typeerror(f"{x} must be an integer")
            return None
        if type(y) is not int:
            error.typeerror(f"{y} must be an integer")
            return None
        if y == 0:
            return x
        if x == 0:
            return y
        if -x == y:
            return 0

        num1 = integer.absolute_value(num1)
        num2 = integer.absolute_value(num2)

        if num2 > 0:
            while boolean.true:
                if num2 <= 0:
                    break
                num2 -= 1
                num1 += 1
        elif num2 < 0:
            while boolean.true:
                if num2 >= 0:
                    break
                num2 += 1
                num1 -= 1

        return num1

    @classmethod
    def int_sub(cls, x, y):
        sub = cls.int_add(x, -y)
        return sub

    @classmethod
    def int_mul(cls, x, y):
        if type(x) is not int:
            error.typeerror(f"{x} must be an integer")
            return None
        if type(y) is not int:
            error.typeerror(f"{y} must be an integer")
            return None

        if y == 0:
            return 0
        if x == 0:
            return 0

        mul = 0
        if x < y:
            x, y = y, x
        if integer.is_negative(x) and integer.is_negative(y):
            x = -x
            y = -y
        if integer.is_positive(x) and integer.is_negative(y):
            x, y = y, x

        for i in arithmeticSequenceGenerator(0, y):
            mul = cls.int_add(mul, x)

        return mul

    @classmethod
    def int_div(cls, x, y):
        if type(x) is not int:
            error.typeerror(f"{x} must be an integer")
            return None
        if type(y) is not int:
            error.typeerror(f"{y} must be an integer")
            return None
        if y == 0:
            raise ZeroDivisionError("Division by zero")
        if x == 0:
            return 0

        if x < y:
            x, y = y, x
        if integer.is_negative(x) and integer.is_negative(y):
            x = -x
            y = -y
        if integer.is_positive(x) and integer.is_negative(y):
            x, y = y, x

        num1 = 0
        num2 = 0
        while boolean.true:
            if num1 >= x:
                break
            num2 += 1
            num1 += y

        return num2

    def __add__(self, other):
        return numOperation(self.value + other.value)

    def __sub__(self, other):
        return numOperation(self.value - other.value)

    def __mul__(self, other):
        return numOperation(self.value * other.value)

    def __truediv__(self, other):
        return numOperation(self.value / other.value)

    def __floordiv__(self, other):
        return numOperation(self.value // other.value)

    def __mod__(self, other):
        return numOperation(self.value % other.value)

    def __divmod__(self, other):
        return numOperation(self.value // other.value)

    def __pow__(self, other):
        return numOperation(self.value ** other.value)

    def __lt__(self, other):
        return numOperation(self.value < other.value)

    def __le__(self, other):
        return numOperation(self.value <= other.value)

    def __gt__(self, other):
        return numOperation(self.value > other.value)

    def __ge__(self, other):
        return numOperation(self.value >= other.value)

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class boolean:
    true = bool(1)
    false = bool(0)


class error:
    @classmethod
    def typeerror(cls, msg):
        raise TypeError(msg)

    @classmethod
    def syntaxerror(cls, msg):
        raise SyntaxError(msg)

    @classmethod
    def nameerror(cls, msg):
        raise NameError(msg)

    @classmethod
    def valueerror(cls, msg):
        raise ValueError(msg)

    @classmethod
    def runtimeerror(cls, msg):
        raise RuntimeError(msg)


class variable:
    @classmethod
    def newvar(cls, name, value):
        globals().setdefault(name, value)

    @classmethod
    def setvar(cls, name, value):
        globals().update({name: value})

    @classmethod
    def delvar(cls, name):
        del globals()[name]

    @classmethod
    def getvar(cls, name):
        return globals()[name]

    @classmethod
    def globallist(cls):
        return globals()


class string:

    @classmethod
    def newstr(cls, name, value):
        if not (type(name) is character.typestr):
            error.typeerror(f"{name} is not a string")
        else:
            if not (name in variable.globallist()):
                if type(value) is character.typestr:
                    variable.newvar(name, value)
                else:
                    error.typeerror(f"{value} is not a string")
            else:
                error.nameerror(f"{name} is already set")

    @classmethod
    def setstr(cls, name, value):
        if not (type(name) is character.typestr):
            error.typeerror(f"{name} is not a string")
        else:
            if name in variable.globallist():
                if type(value) is character.typestr:
                    variable.setvar(name, value)
                else:
                    error.typeerror(f"{value} is not a string")
            else:
                error.nameerror(f"{name} is not already set")

    @classmethod
    def getstr(cls, name):
        if type(name) is not character.typestr:
            error.typeerror(f"{name} is not a string")
        else:
            if name in variable.globallist():
                return variable.getvar(name)
            else:
                error.nameerror(f"{name} is not already set")

    @classmethod
    def delstr(cls, name):
        if type(name) is not character.typestr:
            error.typeerror(f"{name} is not a string")
        else:
            if name in variable.globallist():
                variable.delvar(name)
            else:
                error.nameerror(f"{name} is not already set")


class integer:

    @classmethod
    def newint(cls, name, value):
        if not (type(name) is int):
            error.typeerror(f"{name} is not a integer")
        else:
            if not (name in variable.globallist()):
                if type(value) is int:
                    variable.newvar(name, value)
                else:
                    error.typeerror(f"{value} is not a integer")
            else:
                error.nameerror(f"{name} is already set")

    @classmethod
    def setint(cls, name, value):
        if not (type(name) is int):
            error.typeerror(f"{name} is not a integer")
        else:
            if name in variable.globallist():
                if type(value) is int:
                    variable.setvar(name, value)
                else:
                    error.typeerror(f"{value} is not a integer")
            else:
                error.nameerror(f"{name} is not already set")

    @classmethod
    def getint(cls, name):
        if type(name) is int:
            error.typeerror(f"{name} is not a integer")
        else:
            if name in variable.globallist():
                return variable.getvar(name)
            else:
                error.nameerror(f"{name} is not already set")

    @classmethod
    def delint(cls, name):
        if type(name) is int:
            error.typeerror(f"{name} is not a integer")
        else:
            if name in variable.globallist():
                variable.delvar(name)
            else:
                error.nameerror(f"{name} is not already set")

    @classmethod
    def generate_integer(cls, *args):
        if args is None:
            return 0
        return len(args)

    @classmethod
    def is_negative(cls, arg):
        if arg < 0:
            return boolean.true
        else:
            return boolean.false

    @classmethod
    def is_positive(cls, arg):
        if arg > 0:
            return boolean.true
        else:
            return boolean.false

    @classmethod
    def absolute_value(cls, arg):
        if arg == 0:
            return 0
        if arg > 0:
            return arg
        if arg < 0:
            return -arg

    @classmethod
    def charToHex(cls, char):
        ctx = {
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15
        }
        for i in range(10):
            ctx[f"{i}"] = i
        return ctx[char]

    @classmethod
    def stringToHex(cls, string):
        h = 0
        for i in range(len(string)):
            h += cls.charToHex(string[i]) * (16 ** (len(string) - (i + 1)))
        return hex(h)

    @classmethod
    def hexTostring(cls, h):
        return chr(int(h, 16))


class floats:

    @classmethod
    def newfloat(cls, name, value):
        if not (type(name) is float):
            error.typeerror(f"{name} is not a float")
        else:
            if not (name in variable.globallist()):
                if type(value) is float:
                    variable.newvar(name, value)
                else:
                    error.typeerror(f"{value} is not a float")
            else:
                error.nameerror(f"{name} is already set")

    @classmethod
    def setfloat(cls, name, value):
        if not (type(name) is float):
            error.typeerror(f"{name} is not a float")
        else:
            if name in variable.globallist():
                if type(value) is float:
                    variable.setvar(name, value)
                else:
                    error.typeerror(f"{value} is not a float")
            else:
                error.nameerror(f"{name} is not already set")

    @classmethod
    def getfloat(cls, name):
        if type(name) is float:
            error.typeerror(f"{name} is not a float")
        else:
            if name in variable.globallist():
                return variable.getvar(name)
            else:
                error.nameerror(f"{name} is not already set")

    @classmethod
    def delfloat(cls, name):
        if type(name) is float:
            error.typeerror(f"{name} is not a float")
        else:
            if name in variable.globallist():
                variable.delvar(name)
            else:
                error.nameerror(f"{name} is not already set")


class character:
    typestr = type("")
    letters = list("abcdefghijklmnopqrstuvwxyz")
    numbers = [f"{i}" for i in range(10)]

    @classmethod
    def to_unicode(cls, value):
        if type(value) is character.typestr:
            return ord(value)
        elif type(value) is int:
            if value < 0 or value > 9:
                error.typeerror(f"{value} is not a valid integer")
            return operator(value, 48, '-')
        else:
            error.typeerror(f"{value} is not a string or integer")

    @classmethod
    def char_from_unicode(cls, value):
        if type(value) is int:
            return chr(value)
        else:
            error.typeerror(f"{value} is not a integer")

    @classmethod
    def caesarCipherChar(cls, value, offset):
        if type(value) is character.typestr:
            if value == " ":
                return " "
            if value in cls.numbers:
                n = operator(operator(int(value), offset, '+'), 10, '%')
                return n
            if type(offset) is int:
                s = chr(operator(ord(value), offset, '+'))
                if s in cls.letters:
                    return s
                else:
                    if ord(s) > ord('z'):
                        s = cls.caesarCipherChar(s, -26)
                    if ord(s) < ord('a'):
                        s = cls.caesarCipherChar(s, 26)
                    return s
            else:
                error.typeerror(f"{value} is not a integer")
        else:
            error.typeerror(f"{value} is not a letter")

    @classmethod
    def caesarCipher(cls, value, offset):
        if type(value) is not character.typestr:
            error.typeerror(f"{value} is not a character")
        if type(offset) is not int:
            error.typeerror(f"{offset} is not a integer")
        rs = ""
        for i in range(0, len(value)):
            rs = rs + cls.caesarCipherChar(value[i], offset)
        return rs

    @classmethod
    def caesarCipherDecode(cls, value, offset):
        return cls.caesarCipher(value, -offset)

    @classmethod
    def charHexadecimal(cls, char):
        if type(char) is not character.typestr:
            if len(char) != 1:
                error.typeerror(f"{char} is not a character")
                return None

        o = ord(char)
        if o > 0xff:
            error.valueerror(f"{char} can not convert to a hexadecimal number")

        n = hex(o)
        return n

    @classmethod
    def stringHexadecimal(cls, string):
        if type(string) is not character.typestr:
            error.typeerror(f"{string} is not a string")
            return None

        h = ""
        for i in string:
            ih = cls.charHexadecimal(i)
            h = h + ih

        return h

    @classmethod
    def hexStringToString(cls, hs):
        if type(hs) is not cls.typestr:
            error.typeerror(f"{hs} is not a string")
            return None
        if len(hs) % 2 == 1:
            error.typeerror(f"{hs} is not a valid hexadecimal number")
            return None

        hslen = len(hs)
        hsstringlen = int(hslen / 2)
        slist = stack(None, )
        for i in range(hslen):
            if i % 2 == 1:
                continue
            slist.append(hs[i:i + 2])

        hstack = stack(None, )
        for i in range(hsstringlen):
            hstack.append(slist.get(i))
        hlist = hstack.get()

        s = ""
        for i in hlist:
            sh = integer.hexTostring(i)
            s = s + sh

        return s

    @classmethod
    def stringToHex(cls, string):
        h = ""
        for i in string:
            h = h + hex(ord(i))[-2:]

        return h


class outputter:

    skip = boolean.true
    exittip = "\n"
    exitcode = 0
    def __init__(self, skip=boolean.true, exittip="按下回车键退出...\n", exitcode=0):
        self.skip = skip
        self.exittip = exittip
        self.exitcode = exitcode

    def exit_(self, skip_=skip):
        if skip_:
            return 0

        self.output(self.exittip)
        inp = inputter()
        _ = inp.input_()
        exit(self.exitcode)

    def sys_output(self, output):
        sys.stdout.write(output)
        sys.stdout.flush()

    def logging_info(self, info):
        logging.basicConfig(level=logging.INFO)
        logging.info(info)

    def ctypes_output(self, output):
        libc = ctypes.CDLL(None)
        libc.printf(output.encode('utf-8'))

    def ctypes_wprintf(self, output):
        libc = ctypes.cdll.msvcrt
        txt = "%1s"
        libc.wprintf(txt, output)

    def output(self, output, end='\n'):
        if output is None:
            if end is None or end == "":
                return self
            else:
                self.output(end, "")

        if type(end) != type(""):
            if end is not None:
                error.typeerror(f"{end} is not a string")
                return None
        if type(output) is character.typestr:
            try:
                self.sys_output(output + end)
            except:
                try:
                    self.ctypes_wprintf(output + end)
                except:
                    try:
                        self.ctypes_output(output + end)
                    except:
                        try:
                            self.logging_info(output + end)
                        except:
                            error.runtimeerror(f"failed to print string {output}")
                        finally:
                            pass
                    finally:
                        pass
                finally:
                    pass
            finally:
                if end is None or end == "":
                    pass
                else:
                    self.output(end, "")
                return self

        else:
            error.typeerror(f"{output} is not a string")
            return None
class inputter:

    def __init__(self, default_input_hint=None):
        self.default_input_hint = default_input_hint

    def sys_input(self):
        line = sys.stdin.readline().strip()
        return line

    def input_with_hint(self, hint):
        out = outputter()
        out.output(hint, "")
        inp_ = None
        try:
            inp_ = self.sys_input()
        except:
            try:
                inp_ = input()
            except:
                error.runtimeerror(f"failed to input {hint}")
                return None
            finally:
                return inp_
        finally:
            return inp_

    def input_(self, hint=None):
        if not (type(hint) is character.typestr):
            error.typeerror(f"{hint} is not a string")
            return None
        if hint is None:
            inp = self.input_with_hint(self.default_input_hint)
        else:
            inp = self.input_with_hint(hint)
        return inp

    def input_withend(self, end, hint=None):
        inp = self.input_(hint)
        print(end)
        return inp


class stack:

    def __init__(self, *args):
        if type(args) is not tuple:
            error.typeerror(f"{args} is not a tuple")
        if args == (None,):
            self.stack = []
        else:
            self.stack = list(args)

    def pop(self):
        self.stack.pop()

    def append(self, item):
        self.stack.append(item)

    def delete(self):
        del self

    def get(self, arg=None):
        if arg is None:
            return self.stack
        else:
            if type(arg) is not int:
                error.typeerror(f"{arg} is not an integer")
            else:
                return self.stack[arg]

    def length(self):
        return len(self.stack)

class random:
    last_rand = 0
    default_seed = 2147483647
    @classmethod
    def randint1(cls, last):
        rand1 = last >> 5
        rand2 = last << 3
        rand = (rand1 ^ rand2) >> 1
        return rand

    @classmethod
    def randint2(cls, last):
        rand = (1664525 * last + 1013904223) % 4294967296
        return rand

    @classmethod
    def randint(cls, minn, maxn, seed=default_seed, randmode=1):
        if type(seed) is not int:
            error.typeerror(f"{seed} is not an integer")
            return None
        if type(minn) is not int:
            error.typeerror(f"{minn} is not an integer")
            return None
        if type(maxn) is not int:
            error.typeerror(f"{maxn} is not an integer")
            return None

        if cls.last_rand == 0:
            cls.last_rand = seed

        if randmode == 1:
            cls.last_rand = cls.randint1(cls.last_rand)
        elif randmode == 2:
            cls.last_rand = cls.randint2(cls.last_rand)
        else:
            error.valueerror(f"{randmode} is not a valid random mode")

        return minn + (cls.last_rand % integer.absolute_value(maxn - minn))
class op:
    @classmethod
    def lt(cls, arg1, arg2):
        return arg1 < arg2

    @classmethod
    def gt(cls, arg1, arg2):
        return arg1 > arg2

    @classmethod
    def le(cls, arg1, arg2):
        return arg1 <= arg2

    @classmethod
    def ge(cls, arg1, arg2):
        return arg1 >= arg2

    @classmethod
    def eq(cls, arg1, arg2):
        return arg1 == arg2

    @classmethod
    def ne(cls, arg1, arg2):
        return arg1 != arg2

    @classmethod
    def add(cls, arg1, arg2):
        return arg1 + arg2

    @classmethod
    def sub(cls, arg1, arg2):
        return arg1 - arg2

    @classmethod
    def mul(cls, arg1, arg2):
        return arg1 * arg2

    @classmethod
    def div(cls, arg1, arg2):
        return arg1 / arg2

    @classmethod
    def mod(cls, arg1, arg2):
        return arg1 % arg2

class datas:
    def __init__(self, var, sto):
        self.var = var
        self.sto = sto
        string.newstr(var, '')
        string.newstr(sto, '')

    def __lshift__(self, other):
        string.setstr(self.sto, f'{string.getstr(self.sto)}0')
        if other == {}:
            self.conv()
        return self

    def __rshift__(self, other):
        string.setstr(self.sto, f'{string.getstr(self.sto)}1')
        if other == {}:
            self.conv()
        return self

    def conv(self):
        s = hex(int(string.getstr(self.sto), 2))[2:]
        string.setstr(self.var, string.getstr(self.var) + s)
        string.setstr(self.sto, '')
        return self

class Codes:
    index = 0

    def __hash__(self):
        Codes.index += 1
        return Codes.index

    def do(self):
        pass
class Code(Codes):

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def do(self):
        return self.func(*self.args, **self.kwargs)
class GetVariable(Codes):
    def __init__(self, var):
        self.var = var

    def do(self):
        global variables
        print(f'Get: {variables=} {self.var=}\n')
        return variables[self.var]
class SetVariable(Codes):
    def __init__(self, var, value):
        self.var = var
        self.value = value

    def do(self):
        global variables
        print(f'Set: {variables=} {self.value.__class__=} {self.value.__class__.__bases__=} {self.value.__class__.__bases__[0] == Codes=} {self.var=} {self.value=} {self=}')
        if self.value.__class__.__bases__[0] == Codes:
            print(f'  Set: self.value.do(): {self.value.do()}\n')
            variables[self.var] = self.value.do()
        else:
            variables[self.var] = self.value
        print()
class If(Codes):
    def __init__(self, condition, than, else_=()):
        self.condition = condition
        self.than = than
        self.else_ = else_

    def do(self):
        if self.condition.do():
            for c in self.than:
                c.do()
        else:
            if self.else_ == ():
                return
            for c in self.else_:
                c.do()
class For(Codes):
    def __init__(self, init, judge, loop, code):
        self.init = init
        self.judge = judge
        self.loop = loop
        self.code = code

    def do(self):
        self.init.do()
        while self.judge.do():
            for item in self.code:
                item.do()
            self.loop.do()
class Op(Codes):
    def __init__(self, v1, op, v2):
        self.v1 = v1
        self.op = op
        self.v2 = v2

    def do(self):
        if isinstance(self.v1, str):
            return self.op(variable.getvar(self.v1), self.v2)
        elif isinstance(self.v1, Codes):
            return self.op(self.v1.do(), self.v2)
        else:
            return self.op(self.v1, self.v2)
class Print(Codes):
    def __init__(self, *arg):
        self.arg = arg

    def do(self):
        outputter().output(''.join([str(item.do()) for item in self.arg]))
class NameSpace:
    def __init__(self, *func):
        self.func = func

    def run(self):
        for c in self.func:
            c.do()

def main():
    global variables
    d = datas('var', 'sto')
    d = d << () >> () >> () >> {} << () >> () >> () >> {} << () >> () >> () >> {} \
        << () >> () << () << {} << () >> () >> () << {} << () << () << () >> {} << () >> () >> () << {} \
        << () << () << () >> {} << () >> () >> () << {} << () >> () << () << {} << () << () >> () << {} \
        << () << () << () << {} << () >> () >> () << {} >> () >> () << () << {} << () >> () >> () << {} \
        << () >> () << () << {} << () >> () >> () << {} << () >> () >> () >> {} << () >> () >> () << {} \
        << () << () << () >> {} << () >> () >> () >> {} << () << () >> () >> {}

    code_ = var
    code = code_
    out = new(outputter,)
    clen = int(len(code_) / 2)
    variables['lst'] = stack(None,)
    NameSpace(
        For(
            SetVariable('i', 0),
            Op(GetVariable('i'), op.lt, clen),
            SetVariable('i', Op(
                GetVariable('i'), op.add, 1
            )),
            (
                SetVariable('seed', random.default_seed),
                Code(eval, 'getattr(random, "last_rand", variables["seed"])'),
                SetVariable('code', code_),
                SetVariable('rand1', getattr(random, 'randint')(0, 26, randmode=1)),
                SetVariable('rand2', getattr(random, 'randint')(0, 26, randmode=2)),
                SetVariable('code', Code(eval, 'character.hexStringToString(variables["code"])')),
                SetVariable('code', Code(eval, 'character.caesarCipherDecode(variables["code"], variables["rand2"])')),
                SetVariable('code', Code(eval, 'character.caesarCipherDecode(variables["code"], variables["rand1"])')),
                Code(eval, 'variables["lst"].append(variables["code"][variables["i"]])')
            )
        )
    ).run()

    lst = variables['lst']
    s = ""
    for i in lst.get():
        s = s + i
    out.output(s)


if __name__ == '__main__':
    main()
