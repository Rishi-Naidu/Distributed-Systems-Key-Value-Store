import grpc
from concurrent import futures
import kv_store_pb2
import kv_store_pb2_grpc

class KeyValueStoreServicer(kv_store_pb2_grpc.KeyValueStoreServicer):
    def __init__(self):
        self.store = {}

    def Get(self, request, context):
        key = request.key
        return kv_store_pb2.GetResponse(value=self.store.get(key, "Key not found"))

    def Put(self, request, context):
        self.store[request.key] = request.value
        return kv_store_pb2.PutResponse(message="Key-Value stored successfully")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kv_store_pb2_grpc.add_KeyValueStoreServicer_to_server(KeyValueStoreServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
