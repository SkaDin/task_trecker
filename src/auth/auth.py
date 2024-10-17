import grpc
from fastapi import APIRouter

from protos.gen.python import sso_pb2_grpc

router = APIRouter()


def get_grpc_client():
    channel = grpc.insecure_channel("localhost:40040")
    return sso_pb2_grpc.AuthStub(channel)
