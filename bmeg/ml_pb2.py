# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ml.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ml.proto',
  package='bmeg',
  syntax='proto3',
  serialized_pb=b'\n\x08ml.proto\x12\x04\x62meg\"\x9a\x03\n\x11SignatureTraining\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03gid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x10\n\x08predicts\x18\x04 \x01(\t\x12\x11\n\tphenotype\x18\x05 \x01(\t\x12\x10\n\x08quantile\x18\x06 \x03(\x01\x12\x11\n\tintercept\x18\x07 \x01(\x01\x12?\n\x0c\x63oefficients\x18\x08 \x03(\x0b\x32).bmeg.SignatureTraining.CoefficientsEntry\x12;\n\nbackground\x18\t \x03(\x0b\x32\'.bmeg.SignatureTraining.BackgroundEntry\x12\x18\n\x10\x62\x61\x63kgroundCohort\x18\n \x03(\t\x12\x14\n\x0csignatureFor\x18\x0b \x03(\t\x1a\x33\n\x11\x43oefficientsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x31\n\x0f\x42\x61\x63kgroundEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"O\n\x17SignatureExpressionEdge\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02in\x18\x02 \x01(\t\x12\x0b\n\x03out\x18\x03 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\x01\x62\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SIGNATURETRAINING_COEFFICIENTSENTRY = _descriptor.Descriptor(
  name='CoefficientsEntry',
  full_name='bmeg.SignatureTraining.CoefficientsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.SignatureTraining.CoefficientsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.SignatureTraining.CoefficientsEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=378,
)

_SIGNATURETRAINING_BACKGROUNDENTRY = _descriptor.Descriptor(
  name='BackgroundEntry',
  full_name='bmeg.SignatureTraining.BackgroundEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.SignatureTraining.BackgroundEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.SignatureTraining.BackgroundEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=429,
)

_SIGNATURETRAINING = _descriptor.Descriptor(
  name='SignatureTraining',
  full_name='bmeg.SignatureTraining',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.SignatureTraining.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='bmeg.SignatureTraining.gid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.SignatureTraining.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predicts', full_name='bmeg.SignatureTraining.predicts', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phenotype', full_name='bmeg.SignatureTraining.phenotype', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantile', full_name='bmeg.SignatureTraining.quantile', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intercept', full_name='bmeg.SignatureTraining.intercept', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coefficients', full_name='bmeg.SignatureTraining.coefficients', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='background', full_name='bmeg.SignatureTraining.background', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backgroundCohort', full_name='bmeg.SignatureTraining.backgroundCohort', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signatureFor', full_name='bmeg.SignatureTraining.signatureFor', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATURETRAINING_COEFFICIENTSENTRY, _SIGNATURETRAINING_BACKGROUNDENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=429,
)


_SIGNATUREEXPRESSIONEDGE = _descriptor.Descriptor(
  name='SignatureExpressionEdge',
  full_name='bmeg.SignatureExpressionEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.SignatureExpressionEdge.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in', full_name='bmeg.SignatureExpressionEdge.in', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out', full_name='bmeg.SignatureExpressionEdge.out', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='bmeg.SignatureExpressionEdge.level', index=3,
      number=4, type=1, cpp_type=5, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=510,
)

_SIGNATURETRAINING_COEFFICIENTSENTRY.containing_type = _SIGNATURETRAINING
_SIGNATURETRAINING_BACKGROUNDENTRY.containing_type = _SIGNATURETRAINING
_SIGNATURETRAINING.fields_by_name['coefficients'].message_type = _SIGNATURETRAINING_COEFFICIENTSENTRY
_SIGNATURETRAINING.fields_by_name['background'].message_type = _SIGNATURETRAINING_BACKGROUNDENTRY
DESCRIPTOR.message_types_by_name['SignatureTraining'] = _SIGNATURETRAINING
DESCRIPTOR.message_types_by_name['SignatureExpressionEdge'] = _SIGNATUREEXPRESSIONEDGE

SignatureTraining = _reflection.GeneratedProtocolMessageType('SignatureTraining', (_message.Message,), dict(

  CoefficientsEntry = _reflection.GeneratedProtocolMessageType('CoefficientsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATURETRAINING_COEFFICIENTSENTRY,
    __module__ = 'ml_pb2'
    # @@protoc_insertion_point(class_scope:bmeg.SignatureTraining.CoefficientsEntry)
    ))
  ,

  BackgroundEntry = _reflection.GeneratedProtocolMessageType('BackgroundEntry', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATURETRAINING_BACKGROUNDENTRY,
    __module__ = 'ml_pb2'
    # @@protoc_insertion_point(class_scope:bmeg.SignatureTraining.BackgroundEntry)
    ))
  ,
  DESCRIPTOR = _SIGNATURETRAINING,
  __module__ = 'ml_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.SignatureTraining)
  ))
_sym_db.RegisterMessage(SignatureTraining)
_sym_db.RegisterMessage(SignatureTraining.CoefficientsEntry)
_sym_db.RegisterMessage(SignatureTraining.BackgroundEntry)

SignatureExpressionEdge = _reflection.GeneratedProtocolMessageType('SignatureExpressionEdge', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATUREEXPRESSIONEDGE,
  __module__ = 'ml_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.SignatureExpressionEdge)
  ))
_sym_db.RegisterMessage(SignatureExpressionEdge)


_SIGNATURETRAINING_COEFFICIENTSENTRY.has_options = True
_SIGNATURETRAINING_COEFFICIENTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
_SIGNATURETRAINING_BACKGROUNDENTRY.has_options = True
_SIGNATURETRAINING_BACKGROUNDENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
# @@protoc_insertion_point(module_scope)
