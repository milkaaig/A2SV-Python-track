class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        print(tasks)
        short = [tasks[3]]
        length = len(tasks)

        for i in range(3, (length ) - 4 ,4):
            short.append(tasks[i + 4])

       
        time = []
        leng = len(processorTime)
        processorTime.sort(reverse = True)

        for i in range(leng):
            time.append(short[i]  + processorTime[i])
      
        
        return max(time)