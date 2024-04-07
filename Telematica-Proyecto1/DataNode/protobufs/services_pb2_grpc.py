# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import services_pb2 as services__pb2


class ServicesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendBlock = channel.unary_unary(
                '/services.Services/SendBlock',
                request_serializer=services__pb2.GetBlock.SerializeToString,
                response_deserializer=services__pb2.GetBlockResponse.FromString,
                )


class ServicesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServicesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.SendBlock,
                    request_deserializer=services__pb2.GetBlock.FromString,
                    response_serializer=services__pb2.GetBlockResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.Services', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Services(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.Services/SendBlock',
            services__pb2.GetBlock.SerializeToString,
            services__pb2.GetBlockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
