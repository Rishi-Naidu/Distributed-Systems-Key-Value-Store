import grpc
import kv_store_pb2
import kv_store_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = kv_store_pb2_grpc.KeyValueStoreStub(channel)

        # Test put
        put_response = stub.Put(kv_store_pb2.PutRequest(key='hello', value='world'))
        print(put_response.message)

        # Test get
        get_response = stub.Get(kv_store_pb2.GetRequest(key='hello'))
        print(get_response.value)

if __name__ == '__main__':
    run()
