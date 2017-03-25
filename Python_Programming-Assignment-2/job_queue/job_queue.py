# python3
# import argparse # remove for submission

class Job:
    def __init__(self, worker_index, start_time, finish_time):
        self.worker_index = worker_index
        self.start_time = start_time
        self.finish_time = finish_time

class PriorityQueue:
    def __init__(self, size):
        self.size = size
        self.unassignedWorkers = [i for i in range(size)]
        self.result = []
        self.storage = []

    def getParent(self, i):
        return self.storage[i // 2]

    def getLeftChild(self, i):
        return self.storage[2*i]

    def getRightChild(self, i):
        return self.storage[(2 * i) + 1]

    def swap(self, index, index2):
        tempVar = self.storage[index]
        self.storage[index] = self.storage[index2]
        self.storage[index2] = tempVar

    def compareJobs(self, index1, index2):
        job1 = self.storage[index1]
        job2 = self.storage[index2]

        if job1.finish_time < job2.finish_time:
            return True
        elif job1.finish_time == job2.finish_time:
            if job1.worker_index < job2.worker_index:
                return True
        else:
            return False


    def siftUp(self, index):
        while index > 0 and self.compareJobs(index, index // 2):
            parent_index  = index // 2
            self.swap(index, parent_index)
            index = parent_index

    def siftDown(self, index):
        minIndex = index
        leftChildIndex = 2 * index
        if leftChildIndex < len(self.storage) and self.compareJobs(leftChildIndex, minIndex):
            minIndex = leftChildIndex
        rightChildIndex = (2 * index) + 1
        if rightChildIndex < len(self.storage) and self.compareJobs(rightChildIndex, minIndex):
            minIndex = rightChildIndex

        if minIndex is not index:
            self.swap(index, minIndex)
            self.siftDown(minIndex)

    def insert(self, job):
        if len(self.storage) == self.size:
            raise IndexError('job queue is full')
        self.storage.append(job)
        self.siftUp(len(self.storage) - 1)

    def extractMin(self):
        self.swap(0, len(self.storage) - 1)
        finished_job = self.storage.pop()
        self.siftDown(0)
        return finished_job

    def addJob(self, jobLength):
        if len(self.storage) < self.size and len(self.unassignedWorkers):
            worker = self.unassignedWorkers.pop(0)
            self.insert(Job(worker, 0, jobLength))
            self.result.append((worker, 0))
        else:
            # extractMin and get information from finished job to insert new job
            finished_job = self.extractMin()
            new_job = Job(finished_job.worker_index, finished_job.finish_time, finished_job.finish_time + jobLength)
            self.insert(new_job)
            self.result.append((new_job.worker_index, new_job.start_time))





class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.priorityQueue = PriorityQueue(self.num_workers)
        assert m == len(self.jobs)

    # def read_data(self):
    #     # remove before submission
    #     parser = argparse.ArgumentParser()
    #     parser.add_argument("filename", help="The filename to be processed")
    #     args = parser.parse_args()
    #     lines = list()
    #     if args.filename:
    #         with open(args.filename) as f:
    #             for line in f:
    #                 lines.append(line)
    #                 # end remove before submission
    #     self.num_workers, m = map(int, lines[0].split())
    #     self.jobs = list(map(int, lines[1].split()))
    #     self.priorityQueue = PriorityQueue(self.num_workers)
    #     assert m == len(self.jobs)

    def write_response(self):
        for job in self.priorityQueue.result:
            print(job[0], job[1])

    def assign_jobs(self):
        for job in self.jobs:
            self.priorityQueue.addJob(job)


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

