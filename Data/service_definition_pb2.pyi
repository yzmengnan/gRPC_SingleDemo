from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Index(_message.Message):
    __slots__ = ("index",)
    INDEX_FIELD_NUMBER: _ClassVar[int]
    index: int
    def __init__(self, index: _Optional[int] = ...) -> None: ...

class Positions(_message.Message):
    __slots__ = ("p1", "j1", "j2", "j3", "j4", "j5", "j6")
    P1_FIELD_NUMBER: _ClassVar[int]
    J1_FIELD_NUMBER: _ClassVar[int]
    J2_FIELD_NUMBER: _ClassVar[int]
    J3_FIELD_NUMBER: _ClassVar[int]
    J4_FIELD_NUMBER: _ClassVar[int]
    J5_FIELD_NUMBER: _ClassVar[int]
    J6_FIELD_NUMBER: _ClassVar[int]
    p1: float
    j1: float
    j2: float
    j3: float
    j4: float
    j5: float
    j6: float
    def __init__(self, p1: _Optional[float] = ..., j1: _Optional[float] = ..., j2: _Optional[float] = ..., j3: _Optional[float] = ..., j4: _Optional[float] = ..., j5: _Optional[float] = ..., j6: _Optional[float] = ...) -> None: ...
