class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visit = [False for i in range(len(arr))]
        stepStack = [arr[-2], arr[-1]]
        stepCount = 0

        while not stepStack:
            step = stepStack.pop()
            visit[step] = True
            if step == 0: return stepCount

            if step - 1 >= 0 and not visit[step - 1]: stepStack.append(step - 1)
            if step + 1 <= len(arr) and not visit[step - 1]: stepStack.append(step - 1)
            for i in range(0, step - 1):
                if arr[i] == arr[step] and not visit[i]:
                    stepStack.append(i)
                    break

