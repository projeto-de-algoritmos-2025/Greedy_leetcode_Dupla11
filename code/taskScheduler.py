class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def scheduler(tasks, n):
            info_scheduler = {}
            for task in tasks:
                info_scheduler[task] = info_scheduler.get(task, 0) + 1 #cria uma estrutura de dicionario. Ex: {'A': 3, 'B': 3}
            
            heap = [(-freq, task) for task, freq in info_scheduler.items()] #cria uma heap com as frequencias negativas. Ex: [(-3, 'A'), (-3, 'B')]
            heapq.heapify(heap) #fila de prioridade
            
            cooldown = deque() #fila normal
            tempo = 0
            while cooldown or heap:
                tempo += 1
                if heap:
                    freq, task = heapq.heappop(heap)
                    if freq + 1 < 0:
                        cooldown.append((tempo + n, freq + 1, task))

                if cooldown and cooldown[0][0] == tempo:
                    _, freq, task = cooldown.popleft()
                    heapq.heappush(heap, (freq, task))
            return tempo

        return scheduler(tasks, n)    