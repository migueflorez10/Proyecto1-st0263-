# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eservices.proto\x12\x08services\"\x18\n\x08NameFile\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x05Nodes\x12\x0c\n\x04keys\x18\x01 \x01(\x0c\x12\x0e\n\x06values\x18\x02 \x01(\x0c\"(\n\nUploadFile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x05\",\n\x0bNodesToSend\x12\x0e\n\x06\x62locks\x18\x01 \x01(\x05\x12\r\n\x05nodes\x18\x02 \x03(\t\"\x11\n\x0fGetFilesRequest\"!\n\x10GetFilesResponse\x12\r\n\x05\x66iles\x18\x01 \x03(\t\"3\n\x08GetBlock\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04\x66ile\x18\x02 \x01(\t\x12\r\n\x05\x62lock\x18\x03 \x01(\x05\"\x12\n\x10GetBlockResponse2\xfe\x01\n\x08Services\x12\x31\n\x08SendNode\x12\x12.services.NameFile\x1a\x0f.services.Nodes\"\x00\x12;\n\nManageFile\x12\x14.services.UploadFile\x1a\x15.services.NodesToSend\"\x00\x12\x43\n\x08GetFiles\x12\x19.services.GetFilesRequest\x1a\x1a.services.GetFilesResponse\"\x00\x12=\n\tSendBlock\x12\x12.services.GetBlock\x1a\x1a.services.GetBlockResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NAMEFILE']._serialized_start=28
  _globals['_NAMEFILE']._serialized_end=52
  _globals['_NODES']._serialized_start=54
  _globals['_NODES']._serialized_end=91
  _globals['_UPLOADFILE']._serialized_start=93
  _globals['_UPLOADFILE']._serialized_end=133
  _globals['_NODESTOSEND']._serialized_start=135
  _globals['_NODESTOSEND']._serialized_end=179
  _globals['_GETFILESREQUEST']._serialized_start=181
  _globals['_GETFILESREQUEST']._serialized_end=198
  _globals['_GETFILESRESPONSE']._serialized_start=200
  _globals['_GETFILESRESPONSE']._serialized_end=233
  _globals['_GETBLOCK']._serialized_start=235
  _globals['_GETBLOCK']._serialized_end=286
  _globals['_GETBLOCKRESPONSE']._serialized_start=288
  _globals['_GETBLOCKRESPONSE']._serialized_end=306
  _globals['_SERVICES']._serialized_start=309
  _globals['_SERVICES']._serialized_end=563
# @@protoc_insertion_point(module_scope)
