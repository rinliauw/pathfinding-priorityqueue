class PriorityQueue:

    def __init__(self):
        self.queue = [] 

    # for checking if the queue is empty 
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue 
    def insert(self, data):
        self.queue.append(data)
  
    # for popping an element based on f_cost. Lower f_cost means higher priority
    def priority_pop(self):
        if len(self.queue) == 0:
            return None
        if len(self.queue) == 1:
            item = self.queue[0]
            del self.queue[0]
            return item
        minimum = 0
        for i in range(len(self.queue)): 
            if self.queue[i].f_cost < self.queue[minimum].f_cost: 
                minimum = i 
        item = self.queue[minimum]
        del self.queue[minimum]
        return item

    # a function to check if a data is already in the queue
    def contains(self, data):
        data_pos = data.position
        for i in range(len(self.queue)):
            if self.queue[i].position == data_pos:
                return True
        return False

    #a function to get the priority(f_cost) of a data
    def get_priority(self, data):
        for i in range(len(self.queue)):
            if self.queue[i].position == data.position:
                return self.queue[i].f_cost

    #update the priority of a data in the queue
    def update_priority(self, data, new_cost):
        for i in range(len(self.queue)):
            if self.queue[i].position == data.position:
                self.queue[i].f_cost = new_cost