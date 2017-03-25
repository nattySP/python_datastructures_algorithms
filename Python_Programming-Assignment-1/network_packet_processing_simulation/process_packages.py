# python3
import argparse # remove for submission

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        packet = request
        if not len(self.finish_time_):
            packet.start_time = packet.arrival_time
        else:
            last_packet_finish = self.finish_time_[-1].finish_time
            if last_packet_finish < packet.arrival_time:
                packet.start_time = packet.arrival_time
            else:
                packet.start_time = last_packet_finish

        packet.finish_time = packet.start_time + packet.process_time

        if len(self.finish_time_) < self.size:
            self.finish_time_.append(packet)
            return Response(False, packet.start_time)
        else:
            while len(self.finish_time_) and self.finish_time_[0].finish_time <= packet.arrival_time:
                self.finish_time_.pop(0)

            if len(self.finish_time_) < self.size:
                self.finish_time_.append(packet)
                return Response(False, packet.start_time)
            else:
                return Response(True, -1)

# def ReadRequests(count, lines):
#     requests = []
#     for line in lines:
#         arrival_time, process_time = map(int, line.strip().split())
#         requests.append(Request(arrival_time, process_time))
#     return requests

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    # remove before submission
    # parser = argparse.ArgumentParser()
    # parser.add_argument("filename", help="The filename to be processed")
    # args = parser.parse_args()
    # lines = list()
    # if args.filename:
    #     with open(args.filename) as f:
    #         for line in f:
    #                 lines.append(line)
    # end remove before submission

    # size, count = map(int, lines.pop(0).strip().split())
    size, count = map(int, input().strip().split())
    # requests = ReadRequests(count, lines)
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
