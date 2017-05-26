# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: matrix.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='matrix.proto',
  package='bmeg',
  syntax='proto3',
  serialized_pb=b'\n\x0cmatrix.proto\x12\x04\x62meg\"\x82\x02\n\x0eGeneExpression\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03gid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\r\n\x05\x61lias\x18\x05 \x03(\t\x12$\n\x05scale\x18\x06 \x01(\x0e\x32\x15.bmeg.ExpressionScale\x12\x14\n\x0c\x62iosample_id\x18\x07 \x01(\t\x12:\n\x0b\x65xpressions\x18\x08 \x03(\x0b\x32%.bmeg.GeneExpression.ExpressionsEntry\x1a\x32\n\x10\x45xpressionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x8a\x01\n\x06\x43ohort\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03gid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x11\n\thasSample\x18\x07 \x03(\t\x12\x11\n\thasMatrix\x18\x08 \x03(\t\"x\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03gid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x11\n\thasMember\x18\x07 \x03(\t\"\x94\x01\n\x0c\x44oubleVector\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03gid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12.\n\x06values\x18\x04 \x03(\x0b\x32\x1e.bmeg.DoubleVector.ValuesEntry\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"m\n\x0c\x43ohortMatrix\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03gid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0e\n\x06method\x18\x04 \x01(\t\x12\x11\n\thasVector\x18\x05 \x03(\t\x12\x13\n\x0bhasKeyspace\x18\x06 \x03(\t\"M\n\x08Keyspace\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03gid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0c\n\x04keys\x18\x05 \x03(\t\"J\n\x10MatrixVectorEdge\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02in\x18\x02 \x01(\t\x12\x0b\n\x03out\x18\x03 \x01(\t\x12\x0f\n\x07rowName\x18\x04 \x01(\t\"c\n\x0eMatrixAnalysis\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03gid\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x14\n\x0csourceMatrix\x18\x04 \x03(\t\x12\x14\n\x0cresultMatrix\x18\x05 \x03(\t*B\n\x0f\x45xpressionScale\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nREAD_COUNT\x10\x01\x12\x08\n\x04TPKM\x10\x02\x12\x08\n\x04RPKM\x10\x03\x62\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EXPRESSIONSCALE = _descriptor.EnumDescriptor(
  name='ExpressionScale',
  full_name='bmeg.ExpressionScale',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_COUNT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TPKM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RPKM', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1064,
  serialized_end=1130,
)
_sym_db.RegisterEnumDescriptor(_EXPRESSIONSCALE)

ExpressionScale = enum_type_wrapper.EnumTypeWrapper(_EXPRESSIONSCALE)
UNKNOWN = 0
READ_COUNT = 1
TPKM = 2
RPKM = 3



_GENEEXPRESSION_EXPRESSIONSENTRY = _descriptor.Descriptor(
  name='ExpressionsEntry',
  full_name='bmeg.GeneExpression.ExpressionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.GeneExpression.ExpressionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.GeneExpression.ExpressionsEntry.value', index=1,
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
  serialized_start=231,
  serialized_end=281,
)

_GENEEXPRESSION = _descriptor.Descriptor(
  name='GeneExpression',
  full_name='bmeg.GeneExpression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.GeneExpression.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='bmeg.GeneExpression.gid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.GeneExpression.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.GeneExpression.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alias', full_name='bmeg.GeneExpression.alias', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='bmeg.GeneExpression.scale', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='bmeg.GeneExpression.biosample_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expressions', full_name='bmeg.GeneExpression.expressions', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GENEEXPRESSION_EXPRESSIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=281,
)


_COHORT = _descriptor.Descriptor(
  name='Cohort',
  full_name='bmeg.Cohort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Cohort.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='bmeg.Cohort.gid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.Cohort.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.Cohort.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='bmeg.Cohort.location', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='bmeg.Cohort.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasSample', full_name='bmeg.Cohort.hasSample', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasMatrix', full_name='bmeg.Cohort.hasMatrix', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=284,
  serialized_end=422,
)


_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='bmeg.Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Project.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='bmeg.Project.gid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.Project.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.Project.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='bmeg.Project.location', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='bmeg.Project.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasMember', full_name='bmeg.Project.hasMember', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=424,
  serialized_end=544,
)


_DOUBLEVECTOR_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='bmeg.DoubleVector.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.DoubleVector.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.DoubleVector.ValuesEntry.value', index=1,
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
  serialized_start=650,
  serialized_end=695,
)

_DOUBLEVECTOR = _descriptor.Descriptor(
  name='DoubleVector',
  full_name='bmeg.DoubleVector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.DoubleVector.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='bmeg.DoubleVector.gid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.DoubleVector.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='bmeg.DoubleVector.values', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DOUBLEVECTOR_VALUESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=695,
)


_COHORTMATRIX = _descriptor.Descriptor(
  name='CohortMatrix',
  full_name='bmeg.CohortMatrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.CohortMatrix.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='bmeg.CohortMatrix.gid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.CohortMatrix.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='bmeg.CohortMatrix.method', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasVector', full_name='bmeg.CohortMatrix.hasVector', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasKeyspace', full_name='bmeg.CohortMatrix.hasKeyspace', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=697,
  serialized_end=806,
)


_KEYSPACE = _descriptor.Descriptor(
  name='Keyspace',
  full_name='bmeg.Keyspace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.Keyspace.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='bmeg.Keyspace.gid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.Keyspace.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.Keyspace.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keys', full_name='bmeg.Keyspace.keys', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=808,
  serialized_end=885,
)


_MATRIXVECTOREDGE = _descriptor.Descriptor(
  name='MatrixVectorEdge',
  full_name='bmeg.MatrixVectorEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.MatrixVectorEdge.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in', full_name='bmeg.MatrixVectorEdge.in', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out', full_name='bmeg.MatrixVectorEdge.out', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rowName', full_name='bmeg.MatrixVectorEdge.rowName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=887,
  serialized_end=961,
)


_MATRIXANALYSIS = _descriptor.Descriptor(
  name='MatrixAnalysis',
  full_name='bmeg.MatrixAnalysis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bmeg.MatrixAnalysis.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='bmeg.MatrixAnalysis.gid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bmeg.MatrixAnalysis.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sourceMatrix', full_name='bmeg.MatrixAnalysis.sourceMatrix', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resultMatrix', full_name='bmeg.MatrixAnalysis.resultMatrix', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=963,
  serialized_end=1062,
)

_GENEEXPRESSION_EXPRESSIONSENTRY.containing_type = _GENEEXPRESSION
_GENEEXPRESSION.fields_by_name['scale'].enum_type = _EXPRESSIONSCALE
_GENEEXPRESSION.fields_by_name['expressions'].message_type = _GENEEXPRESSION_EXPRESSIONSENTRY
_DOUBLEVECTOR_VALUESENTRY.containing_type = _DOUBLEVECTOR
_DOUBLEVECTOR.fields_by_name['values'].message_type = _DOUBLEVECTOR_VALUESENTRY
DESCRIPTOR.message_types_by_name['GeneExpression'] = _GENEEXPRESSION
DESCRIPTOR.message_types_by_name['Cohort'] = _COHORT
DESCRIPTOR.message_types_by_name['Project'] = _PROJECT
DESCRIPTOR.message_types_by_name['DoubleVector'] = _DOUBLEVECTOR
DESCRIPTOR.message_types_by_name['CohortMatrix'] = _COHORTMATRIX
DESCRIPTOR.message_types_by_name['Keyspace'] = _KEYSPACE
DESCRIPTOR.message_types_by_name['MatrixVectorEdge'] = _MATRIXVECTOREDGE
DESCRIPTOR.message_types_by_name['MatrixAnalysis'] = _MATRIXANALYSIS
DESCRIPTOR.enum_types_by_name['ExpressionScale'] = _EXPRESSIONSCALE

GeneExpression = _reflection.GeneratedProtocolMessageType('GeneExpression', (_message.Message,), dict(

  ExpressionsEntry = _reflection.GeneratedProtocolMessageType('ExpressionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _GENEEXPRESSION_EXPRESSIONSENTRY,
    __module__ = 'matrix_pb2'
    # @@protoc_insertion_point(class_scope:bmeg.GeneExpression.ExpressionsEntry)
    ))
  ,
  DESCRIPTOR = _GENEEXPRESSION,
  __module__ = 'matrix_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.GeneExpression)
  ))
_sym_db.RegisterMessage(GeneExpression)
_sym_db.RegisterMessage(GeneExpression.ExpressionsEntry)

Cohort = _reflection.GeneratedProtocolMessageType('Cohort', (_message.Message,), dict(
  DESCRIPTOR = _COHORT,
  __module__ = 'matrix_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Cohort)
  ))
_sym_db.RegisterMessage(Cohort)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), dict(
  DESCRIPTOR = _PROJECT,
  __module__ = 'matrix_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Project)
  ))
_sym_db.RegisterMessage(Project)

DoubleVector = _reflection.GeneratedProtocolMessageType('DoubleVector', (_message.Message,), dict(

  ValuesEntry = _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), dict(
    DESCRIPTOR = _DOUBLEVECTOR_VALUESENTRY,
    __module__ = 'matrix_pb2'
    # @@protoc_insertion_point(class_scope:bmeg.DoubleVector.ValuesEntry)
    ))
  ,
  DESCRIPTOR = _DOUBLEVECTOR,
  __module__ = 'matrix_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.DoubleVector)
  ))
_sym_db.RegisterMessage(DoubleVector)
_sym_db.RegisterMessage(DoubleVector.ValuesEntry)

CohortMatrix = _reflection.GeneratedProtocolMessageType('CohortMatrix', (_message.Message,), dict(
  DESCRIPTOR = _COHORTMATRIX,
  __module__ = 'matrix_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.CohortMatrix)
  ))
_sym_db.RegisterMessage(CohortMatrix)

Keyspace = _reflection.GeneratedProtocolMessageType('Keyspace', (_message.Message,), dict(
  DESCRIPTOR = _KEYSPACE,
  __module__ = 'matrix_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.Keyspace)
  ))
_sym_db.RegisterMessage(Keyspace)

MatrixVectorEdge = _reflection.GeneratedProtocolMessageType('MatrixVectorEdge', (_message.Message,), dict(
  DESCRIPTOR = _MATRIXVECTOREDGE,
  __module__ = 'matrix_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.MatrixVectorEdge)
  ))
_sym_db.RegisterMessage(MatrixVectorEdge)

MatrixAnalysis = _reflection.GeneratedProtocolMessageType('MatrixAnalysis', (_message.Message,), dict(
  DESCRIPTOR = _MATRIXANALYSIS,
  __module__ = 'matrix_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.MatrixAnalysis)
  ))
_sym_db.RegisterMessage(MatrixAnalysis)


_GENEEXPRESSION_EXPRESSIONSENTRY.has_options = True
_GENEEXPRESSION_EXPRESSIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
_DOUBLEVECTOR_VALUESENTRY.has_options = True
_DOUBLEVECTOR_VALUESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), b'8\001')
# @@protoc_insertion_point(module_scope)