# @Time         : 2024/10/3 20:47
# @Author       : Yang Qiang
# @File         : client.py
# @Description  :
import time

import grpc

import service_definition_pb2 as sd_pb
import service_definition_pb2_grpc as sd_pb_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = sd_pb_grpc.MyMessageStub(channel)

data = sd_pb.Index(index=2)

start = time.time()
f = stub.GetPosition(data).p1

print(f)

data = sd_pb.Positions(p1=0.5)

f = stub.SendPosition(data).index

print(f)

end = time.time()

print(end-start)



