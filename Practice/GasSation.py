class Solution:
    def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    
        total_gas = 0
        current_gas = 0

        start_index = 0

        for i, (gasz, costz) in enumerate(zip(gas, cost)):
            net_gas = gasz - costz

            total_gas += net_gas
            current_gas += net_gas

            if current_gas < 0:
                current_gas = 0
                start_index = i + 1
        
        if total_gas >= 0:
            return start_index
        else:
            return -1



print(Solution.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])) # 3
print(Solution.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3])) #-1