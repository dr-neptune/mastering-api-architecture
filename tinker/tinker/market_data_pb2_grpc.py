# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import market_data_pb2 as market__data__pb2


class MarketDataServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMarketData = channel.unary_unary(
                '/market_data.MarketDataService/GetMarketData',
                request_serializer=market__data__pb2.GetMarketDataRequest.SerializeToString,
                response_deserializer=market__data__pb2.MarketData.FromString,
                )
        self.ListMarketData = channel.unary_stream(
                '/market_data.MarketDataService/ListMarketData',
                request_serializer=market__data__pb2.ListMarketDataRequest.SerializeToString,
                response_deserializer=market__data__pb2.MarketData.FromString,
                )


class MarketDataServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMarketData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMarketData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMarketData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMarketData,
                    request_deserializer=market__data__pb2.GetMarketDataRequest.FromString,
                    response_serializer=market__data__pb2.MarketData.SerializeToString,
            ),
            'ListMarketData': grpc.unary_stream_rpc_method_handler(
                    servicer.ListMarketData,
                    request_deserializer=market__data__pb2.ListMarketDataRequest.FromString,
                    response_serializer=market__data__pb2.MarketData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'market_data.MarketDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MarketDataService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMarketData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/market_data.MarketDataService/GetMarketData',
            market__data__pb2.GetMarketDataRequest.SerializeToString,
            market__data__pb2.MarketData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMarketData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/market_data.MarketDataService/ListMarketData',
            market__data__pb2.ListMarketDataRequest.SerializeToString,
            market__data__pb2.MarketData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)