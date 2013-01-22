# encoding: utf-8
# module gdb
# from (built-in)
# by generator 1.118
# no doc

# imports
import gdb.prompt as prompt # /Users/manuel/arm-cs-tools/share/gdb/python/gdb/prompt.pyc
import gdb.command as command # /Users/manuel/arm-cs-tools/share/gdb/python/gdb/command/__init__.pyc
import events as events # <module 'events' (built-in)>

# Variables with simple values

ARCH_FRAME = 5

BP_ACCESS_WATCHPOINT = 8

BP_BREAKPOINT = 1

BP_HARDWARE_WATCHPOINT = 6

BP_NONE = 0

BP_READ_WATCHPOINT = 7

BP_WATCHPOINT = 5

COMMAND_BREAKPOINTS = 6
COMMAND_DATA = 1
COMMAND_FILES = 3
COMMAND_MAINTENANCE = 11
COMMAND_NONE = -1
COMMAND_OBSCURE = 10
COMMAND_RUNNING = 0
COMMAND_STACK = 2
COMMAND_STATUS = 5
COMMAND_SUPPORT = 4
COMMAND_TRACEPOINTS = 7

COMPLETE_COMMAND = 3
COMPLETE_FILENAME = 1
COMPLETE_LOCATION = 2
COMPLETE_NONE = 0
COMPLETE_SYMBOL = 4

DUMMY_FRAME = 1

FRAME_UNWIND_INNER_ID = 4

FRAME_UNWIND_NO_REASON = 0

FRAME_UNWIND_NO_SAVED_PC = 6

FRAME_UNWIND_NULL_ID = 1

FRAME_UNWIND_OUTERMOST = 2

FRAME_UNWIND_SAME_ID = 5

FRAME_UNWIND_UNAVAILABLE = 3

HOST_CONFIG = 'x86_64-apple-darwin12.2.0'

INLINE_FRAME = 2

NORMAL_FRAME = 0

PARAM_AUTO_BOOLEAN = 1

PARAM_BOOLEAN = 0
PARAM_ENUM = 10
PARAM_FILENAME = 7
PARAM_INTEGER = 3

PARAM_OPTIONAL_FILENAME = 6

PARAM_STRING = 4

PARAM_STRING_NOESCAPE = 5

PARAM_UINTEGER = 2
PARAM_ZINTEGER = 8

PYTHONDIR = '/Users/manuel/arm-cs-tools/share/gdb/python'

SENTINEL_FRAME = 6

SIGTRAMP_FRAME = 4

STDERR = 1
STDLOG = 2
STDOUT = 0

SYMBOL_FUNCTIONS_DOMAIN = 1

SYMBOL_LABEL_DOMAIN = 3

SYMBOL_LOC_ARG = 4
SYMBOL_LOC_BLOCK = 10
SYMBOL_LOC_COMPUTED = 14
SYMBOL_LOC_CONST = 1

SYMBOL_LOC_CONST_BYTES = 11

SYMBOL_LOC_LABEL = 9
SYMBOL_LOC_LOCAL = 7

SYMBOL_LOC_OPTIMIZED_OUT = 13

SYMBOL_LOC_REF_ARG = 5

SYMBOL_LOC_REGISTER = 3

SYMBOL_LOC_REGPARM_ADDR = 6

SYMBOL_LOC_STATIC = 2
SYMBOL_LOC_TYPEDEF = 8
SYMBOL_LOC_UNDEF = 0
SYMBOL_LOC_UNRESOLVED = 12

SYMBOL_STRUCT_DOMAIN = 2

SYMBOL_TYPES_DOMAIN = 2

SYMBOL_UNDEF_DOMAIN = 0

SYMBOL_VARIABLES_DOMAIN = 0

SYMBOL_VAR_DOMAIN = 1

TAILCALL_FRAME = 3

TARGET_CONFIG = 'arm-none-eabi'

TYPE_CODE_ARRAY = 2
TYPE_CODE_BITSTRING = 14
TYPE_CODE_BOOL = 21
TYPE_CODE_CHAR = 20
TYPE_CODE_COMPLEX = 22
TYPE_CODE_DECFLOAT = 25
TYPE_CODE_ENUM = 5
TYPE_CODE_ERROR = 15
TYPE_CODE_FLAGS = 6
TYPE_CODE_FLT = 9
TYPE_CODE_FUNC = 7
TYPE_CODE_INT = 8

TYPE_CODE_INTERNAL_FUNCTION = 27

TYPE_CODE_MEMBERPTR = 18
TYPE_CODE_METHOD = 16
TYPE_CODE_METHODPTR = 17
TYPE_CODE_NAMESPACE = 24
TYPE_CODE_PTR = 1
TYPE_CODE_RANGE = 12
TYPE_CODE_REF = 19
TYPE_CODE_SET = 11
TYPE_CODE_STRING = 13
TYPE_CODE_STRUCT = 3
TYPE_CODE_TYPEDEF = 23
TYPE_CODE_UNION = 4
TYPE_CODE_VOID = 10

VERSION = '7.4.1'

WP_ACCESS = 2
WP_READ = 1
WP_WRITE = 0

# functions

def block_for_pc(*args, **kwargs): # real signature unknown
    """ Return the block containing the given pc value, or None. """
    pass


def breakpoints(*args, **kwargs): # real signature unknown
    """ Return a tuple of all breakpoint objects """
    pass


def current_objfile(*args, **kwargs): # real signature unknown
    """ Return the current Objfile being loaded, or None. """
    pass


def current_progspace(*args, **kwargs): # real signature unknown
    """ Return the current Progspace. """
    pass


def decode_line(String): # real signature unknown; restored from __doc__
    """
    decode_line (String) -> Tuple.  Decode a string argument the way
    that 'break' or 'edit' does.  Return a tuple containing two elements.
    The first element contains any unparsed portion of the String parameter
    (or None if the string was fully parsed).  The second element contains
    a tuple that contains all the locations that match, represented as
    gdb.Symtab_and_line objects (or None).
    """
    pass


def default_visualizer(*args, **kwargs): # real signature unknown
    """ Find the default visualizer for a Value. """
    pass


def execute(*args, **kwargs): # real signature unknown
    """ Execute a gdb command """
    pass


def flush(*args, **kwargs): # real signature unknown
    """ Flush gdb's filtered stdout stream. """
    pass


def frame_stop_reason_string(*args, **kwargs): # real signature unknown
    """
    stop_reason_string (Integer) -> String.
    Return a string explaining unwind stop reason.
    """
    pass


def history(*args, **kwargs): # real signature unknown
    """ Get a value from history """
    pass


def inferiors(): # real signature unknown; restored from __doc__
    """
    inferiors () -> (gdb.Inferior, ...).
    Return a tuple containing all inferiors.
    """
    pass


def lookup_global_symbol(name, domain=None): # real signature unknown; restored from __doc__
    """
    lookup_global_symbol (name [, domain]) -> symbol
    Return the symbol corresponding to the given name (or None).
    """
    pass


def lookup_symbol(name, block=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    lookup_symbol (name [, block] [, domain]) -> (symbol, is_field_of_this)
    Return a tuple with the symbol corresponding to the given name (or None) and
    a boolean indicating if name is a field of the current implied argument
    `this' (when the current language is object-oriented).
    """
    pass


def lookup_type(name, block=None): # real signature unknown; restored from __doc__
    """
    lookup_type (name [, block]) -> type
    Return a Type corresponding to the given name.
    """
    return type(*(), **{})


def newest_frame(): # real signature unknown; restored from __doc__
    """
    newest_frame () -> gdb.Frame.
    Return the newest frame object.
    """
    pass


def objfiles(*args, **kwargs): # real signature unknown
    """ Return a sequence of all loaded objfiles. """
    pass


def parameter(*args, **kwargs): # real signature unknown
    """ Return a gdb parameter's value """
    pass


def parse_and_eval(String): # real signature unknown; restored from __doc__
    """
    parse_and_eval (String) -> Value.
    Parse String as an expression, evaluate it, and return the result as a Value.
    """
    pass


def post_event(*args, **kwargs): # real signature unknown
    """ Post an event into gdb's event loop. """
    pass


def progspaces(*args, **kwargs): # real signature unknown
    """ Return a sequence of all progspaces. """
    pass


def selected_frame(): # real signature unknown; restored from __doc__
    """
    selected_frame () -> gdb.Frame.
    Return the selected frame object.
    """
    pass


def selected_inferior(): # real signature unknown; restored from __doc__
    """
    selected_inferior () -> gdb.Inferior.
    Return the selected inferior object.
    """
    pass


def selected_thread(): # real signature unknown; restored from __doc__
    """
    selected_thread () -> gdb.InferiorThread.
    Return the selected thread object.
    """
    pass


def solib_name(Long): # real signature unknown; restored from __doc__
    """
    solib_name (Long) -> String.
    Return the name of the shared library holding a given address, or None.
    """
    pass


def string_to_argv(String): # real signature unknown; restored from __doc__
    """
    string_to_argv (String) -> Array.
    Parse String and return an argv-like array.
    Arguments are separate by spaces and may be quoted.
    """
    pass


def target_charset(): # real signature unknown; restored from __doc__
    """
    target_charset () -> string.
    Return the name of the current target charset.
    """
    pass


def target_wide_charset(): # real signature unknown; restored from __doc__
    """
    target_wide_charset () -> string.
    Return the name of the current target wide charset.
    """
    pass


def write(*args, **kwargs): # real signature unknown
    """ Write a string using gdb's filtered stream. """
    pass


# classes

class Block(object):
    """ GDB block object """
    def is_valid(self): # real signature unknown; restored from __doc__
        """
        is_valid () -> Boolean.
        Return true if this block is valid, false if not.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    end = property(lambda self: object()) # default
    function = property(lambda self: object()) # default
    global_block = property(lambda self: object()) # default
    is_global = property(lambda self: object()) # default
    is_static = property(lambda self: object()) # default
    start = property(lambda self: object()) # default
    static_block = property(lambda self: object()) # default
    superblock = property(lambda self: object()) # default


class BlockIterator(object):
    """ GDB block syms iterator object """
    def is_valid(self): # real signature unknown; restored from __doc__
        """
        is_valid () -> Boolean.
        Return true if this block iterator is valid, false if not.
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Breakpoint(object):
    """ GDB breakpoint object """
    def delete(self, *args, **kwargs): # real signature unknown
        """ Delete the underlying GDB breakpoint. """
        pass

    def is_valid(self, *args, **kwargs): # real signature unknown
        """ Return true if this breakpoint is valid, false if not. """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    commands = property(lambda self: object()) # default
    condition = property(lambda self: object()) # default
    enabled = property(lambda self: object()) # default
    expression = property(lambda self: object()) # default
    hit_count = property(lambda self: object()) # default
    ignore_count = property(lambda self: object()) # default
    location = property(lambda self: object()) # default
    number = property(lambda self: object()) # default
    silent = property(lambda self: object()) # default
    task = property(lambda self: object()) # default
    thread = property(lambda self: object()) # default
    type = property(lambda self: object()) # default
    visible = property(lambda self: object()) # default


class Event(object):
    """ GDB event object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ThreadEvent(Event):
    """ GDB thread event object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class StopEvent(ThreadEvent):
    """ GDB stop event object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class BreakpointEvent(StopEvent):
    """ GDB breakpoint stop event object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Command(object):
    """ GDB command object """
    def dont_repeat(self, *args, **kwargs): # real signature unknown
        """ Prevent command repetition when user enters empty line. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ContinueEvent(ThreadEvent):
    """ GDB continue event object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class error(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object()) # default


class EventRegistry(object):
    """ GDB event registry object """
    def connect(self, *args, **kwargs): # real signature unknown
        """ Add function """
        pass

    def disconnect(self, *args, **kwargs): # real signature unknown
        """ Remove function """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ExitedEvent(Event):
    """ GDB exited event object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Field(object):
    """ GDB field object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class FinishBreakpoint(Breakpoint):
    """ GDB finish breakpoint object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    return_value = property(lambda self: object()) # default


class Frame(object):
    """ GDB frame object """
    def block(self): # real signature unknown; restored from __doc__
        """
        block () -> gdb.Block.
        Return the frame's code block.
        """
        pass

    def find_sal(self): # real signature unknown; restored from __doc__
        """
        find_sal () -> gdb.Symtab_and_line.
        Return the frame's symtab and line.
        """
        pass

    def function(self): # real signature unknown; restored from __doc__
        """
        function () -> gdb.Symbol.
        Returns the symbol for the function corresponding to this frame.
        """
        pass

    def is_valid(self): # real signature unknown; restored from __doc__
        """
        is_valid () -> Boolean.
        Return true if this frame is valid, false if not.
        """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """
        name () -> String.
        Return the function name of the frame, or None if it can't be determined.
        """
        pass

    def newer(self): # real signature unknown; restored from __doc__
        """
        newer () -> gdb.Frame.
        Return the frame called by this frame.
        """
        pass

    def older(self): # real signature unknown; restored from __doc__
        """
        older () -> gdb.Frame.
        Return the frame that called this frame.
        """
        pass

    def pc(self): # real signature unknown; restored from __doc__
        """
        pc () -> Long.
        Return the frame's resume address.
        """
        pass

    def read_var(self, variable): # real signature unknown; restored from __doc__
        """
        read_var (variable) -> gdb.Value.
        Return the value of the variable in this frame.
        """
        pass

    def select(self, *args, **kwargs): # real signature unknown
        """ Select this frame as the user's current frame. """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """
        type () -> Integer.
        Return the type of the frame.
        """
        pass

    def unwind_stop_reason(self): # real signature unknown; restored from __doc__
        """
        unwind_stop_reason () -> Integer.
        Return the reason why it's not possible to find frames older than this.
        """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


class Function(object):
    """ GDB function object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class GdbError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object()) # default


class Inferior(object):
    """ GDB inferior object """
    def is_valid(self): # real signature unknown; restored from __doc__
        """
        is_valid () -> Boolean.
        Return true if this inferior is valid, false if not.
        """
        pass

    def read_memory(self, address, length): # real signature unknown; restored from __doc__
        """
        read_memory (address, length) -> buffer
        Return a buffer object for reading from the inferior's memory.
        """
        return buffer(*(), **{})

    def search_memory(self, address, length, pattern): # real signature unknown; restored from __doc__
        """
        search_memory (address, length, pattern) -> long
        Return a long with the address of a match, or None.
        """
        return 0

    def threads(self, *args, **kwargs): # real signature unknown
        """ Return all the threads of this inferior. """
        pass

    def write_memory(self, address, buffer, length=None): # real signature unknown; restored from __doc__
        """
        write_memory (address, buffer [, length])
        Write the given buffer object to the inferior's memory.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    num = property(lambda self: object()) # default
    pid = property(lambda self: object()) # default
    was_attached = property(lambda self: object()) # default


class InferiorThread(object):
    """ GDB thread object """
    def is_exited(self): # real signature unknown; restored from __doc__
        """
        is_exited () -> Boolean
        Return whether the thread is exited.
        """
        return False

    def is_running(self): # real signature unknown; restored from __doc__
        """
        is_running () -> Boolean
        Return whether the thread is running.
        """
        return False

    def is_stopped(self): # real signature unknown; restored from __doc__
        """
        is_stopped () -> Boolean
        Return whether the thread is stopped.
        """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """
        is_valid () -> Boolean.
        Return true if this inferior thread is valid, false if not.
        """
        pass

    def switch(self): # real signature unknown; restored from __doc__
        """
        switch ()
        Makes this the GDB selected thread.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    name = property(lambda self: object()) # default
    num = property(lambda self: object()) # default
    ptid = property(lambda self: object()) # default


class Membuf(object):
    """ GDB memory buffer object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


class MemoryError(error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class NewObjFileEvent(Event):
    """ GDB new object file event object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Objfile(object):
    """ GDB objfile object """
    def is_valid(self): # real signature unknown; restored from __doc__
        """
        is_valid () -> Boolean.
        Return true if this object file is valid, false if not.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    filename = property(lambda self: object()) # default
    pretty_printers = property(lambda self: object()) # default


class Parameter(object):
    """ GDB parameter object """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class Progspace(object):
    """ GDB progspace object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    filename = property(lambda self: object()) # default
    pretty_printers = property(lambda self: object()) # default


class SignalEvent(StopEvent):
    """ GDB signal event object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Symbol(object):
    """ GDB symbol object """
    def is_valid(self): # real signature unknown; restored from __doc__
        """
        is_valid () -> Boolean.
        Return true if this symbol is valid, false if not.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    addr_class = property(lambda self: object()) # default
    is_argument = property(lambda self: object()) # default
    is_constant = property(lambda self: object()) # default
    is_function = property(lambda self: object()) # default
    is_variable = property(lambda self: object()) # default
    linkage_name = property(lambda self: object()) # default
    name = property(lambda self: object()) # default
    print_name = property(lambda self: object()) # default
    symtab = property(lambda self: object()) # default
    type = property(lambda self: object()) # default


class Symtab(object):
    """ GDB symtab object """
    def fullname(self): # real signature unknown; restored from __doc__
        """
        fullname () -> String.
        Return the symtab's full source filename.
        """
        pass

    def is_valid(self): # real signature unknown; restored from __doc__
        """
        is_valid () -> Boolean.
        Return true if this symbol table is valid, false if not.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    filename = property(lambda self: object()) # default
    objfile = property(lambda self: object()) # default


class Symtab_and_line(object):
    """ GDB symtab_and_line object """
    def is_valid(self): # real signature unknown; restored from __doc__
        """
        is_valid () -> Boolean.
        Return true if this symbol table and line is valid, false if not.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    line = property(lambda self: object()) # default
    pc = property(lambda self: object()) # default
    symtab = property(lambda self: object()) # default


class Type(object):
    """ GDB type object """
    def array(self, LOW_BOUND=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        array ([LOW_BOUND,] HIGH_BOUND) -> Type
        Return a type which represents an array of objects of this type.
        The bounds of the array are [LOW_BOUND, HIGH_BOUND] inclusive.
        If LOW_BOUND is omitted, a value of zero is used.
        """
        pass

    def const(self): # real signature unknown; restored from __doc__
        """
        const () -> Type
        Return a const variant of this type.
        """
        return Type

    def fields(self): # real signature unknown; restored from __doc__
        """
        fields () -> list
        Return a list holding all the fields of this type.
        Each field is a gdb.Field object.
        """
        return []

    def get(self, k, default=None): # real signature unknown; restored from __doc__
        """
        T.get(k[,default]) -> returns field named k in T, if it exists;
        otherwise returns default, if supplied, or None if not.
        """
        pass

    def has_key(self, k): # real signature unknown; restored from __doc__
        """ T.has_key(k) -> True if T has a field named k, else False """
        return False

    def items(self): # real signature unknown; restored from __doc__
        """
        items () -> list
        Return a list of (name, field) pairs of this type.
        Each field is a gdb.Field object.
        """
        return []

    def iteritems(self): # real signature unknown; restored from __doc__
        """
        iteritems () -> an iterator over the (name, field)
        pairs of this type.  Each field is a gdb.Field object.
        """
        pass

    def iterkeys(self): # real signature unknown; restored from __doc__
        """ iterkeys () -> an iterator over the field names of this type. """
        pass

    def itervalues(self): # real signature unknown; restored from __doc__
        """
        itervalues () -> an iterator over the fields of this type.
        Each field is a gdb.Field object.
        """
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """
        keys () -> list
        Return a list holding all the fields names of this type.
        """
        return []

    def pointer(self): # real signature unknown; restored from __doc__
        """
        pointer () -> Type
        Return a type of pointer to this type.
        """
        return Type

    def range(self): # real signature unknown; restored from __doc__
        """
        range () -> tuple
        Return a tuple containing the lower and upper range for this type.
        """
        return ()

    def reference(self): # real signature unknown; restored from __doc__
        """
        reference () -> Type
        Return a type of reference to this type.
        """
        return Type

    def strip_typedefs(self): # real signature unknown; restored from __doc__
        """
        strip_typedefs () -> Type
        Return a type formed by stripping this type of all typedefs.
        """
        return Type

    def target(self): # real signature unknown; restored from __doc__
        """
        target () -> Type
        Return the target type of this type.
        """
        return Type

    def template_argument(self, arg, block=None): # real signature unknown; restored from __doc__
        """
        template_argument (arg, [block]) -> Type
        Return the type of a template argument.
        """
        return Type

    def unqualified(self): # real signature unknown; restored from __doc__
        """
        unqualified () -> Type
        Return a variant of this type without const or volatile attributes.
        """
        return Type

    def values(self): # real signature unknown; restored from __doc__
        """
        values () -> list
        Return a list holding all the fields of this type.
        Each field is a gdb.Field object.
        """
        return []

    def volatile(self): # real signature unknown; restored from __doc__
        """
        volatile () -> Type
        Return a volatile variant of this type
        """
        return Type

    def __contains__(self, k): # real signature unknown; restored from __doc__
        """ T.__contains__(k) -> True if T has a field named k, else False """
        return False

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    code = property(lambda self: object()) # default
    sizeof = property(lambda self: object()) # default
    tag = property(lambda self: object()) # default


class TypeIterator(object):
    """ GDB type iterator object """
    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass


class Value(object):
    """ GDB value object """
    def cast(self, *args, **kwargs): # real signature unknown
        """ Cast the value to the supplied type. """
        pass

    def dereference(self, *args, **kwargs): # real signature unknown
        """ Dereferences the value. """
        pass

    def dynamic_cast(self, gdb_Type): # real signature unknown; restored from __doc__
        """
        dynamic_cast (gdb.Type) -> gdb.Value
        Cast the value to the supplied type, as if by the C++ dynamic_cast operator.
        """
        pass

    def fetch_lazy(self, *args, **kwargs): # real signature unknown
        """ Fetches the value from the inferior, if it was lazy. """
        pass

    def lazy_string(self, encoding=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        lazy_string ([encoding]  [, length]) -> lazy_string
        Return a lazy string representation of the value.
        """
        pass

    def reinterpret_cast(self, gdb_Type): # real signature unknown; restored from __doc__
        """
        reinterpret_cast (gdb.Type) -> gdb.Value
        Cast the value to the supplied type, as if by the C++
        reinterpret_cast operator.
        """
        pass

    def string(self, encoding=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        string ([encoding] [, errors] [, length]) -> string
        Return Unicode string representation of the value.
        """
        pass

    def __abs__(self): # real signature unknown; restored from __doc__
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y): # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __float__(self): # real signature unknown; restored from __doc__
        """ x.__float__() <==> float(x) """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __invert__(self): # real signature unknown; restored from __doc__
        """ x.__invert__() <==> ~x """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __long__(self): # real signature unknown; restored from __doc__
        """ x.__long__() <==> long(x) """
        pass

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __or__(self, y): # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __pos__(self): # real signature unknown; restored from __doc__
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None): # real signature unknown; restored from __doc__
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rand__(self, y): # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __ror__(self, y): # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rpow__(self, x, z=None): # real signature unknown; restored from __doc__
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rrshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rxor__(self, y): # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __xor__(self, y): # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass

    address = property(lambda self: object()) # default
    dynamic_type = property(lambda self: object()) # default
    is_lazy = property(lambda self: object()) # default
    is_optimized_out = property(lambda self: object()) # default
    type = property(lambda self: object()) # default


# variables with complex values

pretty_printers = []

__path__ = [
    '/Users/manuel/arm-cs-tools/share/gdb/python/gdb',
]

