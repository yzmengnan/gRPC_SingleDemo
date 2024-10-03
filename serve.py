# @Time         : 2024/10/3 20:37
# @Author       : Yang Qiang
# @File         : serve.py
# @Description  :

import logging
import grpc
import service_definition_pb2_grpc as sd_grpc
import service_definition_pb2 as sd_pb

from concurrent import futures


class MyServer(sd_grpc.MyMessage):

    def GetPosition(self, request, context):
        # data = request
        # a = data.index
        # print(a)
        if request.index == 2:
            return sd_pb.Positions(p1=20.3)
        elif request.index == 3:
            return sd_pb.Positions(p1=10.3)

    def SendPosition(self, request, context):
        print(request.p1)
        return sd_pb.Index(index=33)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sd_grpc.add_MyMessageServicer_to_server(MyServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
