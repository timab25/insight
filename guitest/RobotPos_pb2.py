# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RobotPos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RobotPos.proto',
  package='insight_msgs',
  serialized_pb=_b('\n\x0eRobotPos.proto\x12\x0cinsight_msgs\"7\n\x08RobotPos\x12\r\n\x05pos_x\x18\x01 \x02(\x01\x12\r\n\x05pos_y\x18\x02 \x02(\x01\x12\r\n\x05pos_z\x18\x03 \x02(\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ROBOTPOS = _descriptor.Descriptor(
  name='RobotPos',
  full_name='insight_msgs.RobotPos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_x', full_name='insight_msgs.RobotPos.pos_x', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_y', full_name='insight_msgs.RobotPos.pos_y', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_z', full_name='insight_msgs.RobotPos.pos_z', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['RobotPos'] = _ROBOTPOS

RobotPos = _reflection.GeneratedProtocolMessageType('RobotPos', (_message.Message,), dict(
  DESCRIPTOR = _ROBOTPOS,
  __module__ = 'RobotPos_pb2'
  # @@protoc_insertion_point(class_scope:insight_msgs.RobotPos)
  ))
_sym_db.RegisterMessage(RobotPos)


# @@protoc_insertion_point(module_scope)
