# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market_data.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11market_data.proto\x12\x0bmarket_data\"\"\n\x14GetMarketDataRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"&\n\x15ListMarketDataRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\"\x91\x01\n\nMarketData\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0c\n\x04open\x18\x03 \x01(\x02\x12\x0c\n\x04high\x18\x04 \x01(\x02\x12\x0b\n\x03low\x18\x05 \x01(\x02\x12\r\n\x05\x63lose\x18\x06 \x01(\x02\x12\x11\n\tadj_close\x18\x07 \x01(\x02\x12\x0e\n\x06volume\x18\x08 \x01(\x02\x12\x0e\n\x06symbol\x18\t \x01(\t2\xb5\x01\n\x11MarketDataService\x12M\n\rGetMarketData\x12!.market_data.GetMarketDataRequest\x1a\x17.market_data.MarketData\"\x00\x12Q\n\x0eListMarketData\x12\".market_data.ListMarketDataRequest\x1a\x17.market_data.MarketData\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'market_data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETMARKETDATAREQUEST']._serialized_start=34
  _globals['_GETMARKETDATAREQUEST']._serialized_end=68
  _globals['_LISTMARKETDATAREQUEST']._serialized_start=70
  _globals['_LISTMARKETDATAREQUEST']._serialized_end=108
  _globals['_MARKETDATA']._serialized_start=111
  _globals['_MARKETDATA']._serialized_end=256
  _globals['_MARKETDATASERVICE']._serialized_start=259
  _globals['_MARKETDATASERVICE']._serialized_end=440
# @@protoc_insertion_point(module_scope)
