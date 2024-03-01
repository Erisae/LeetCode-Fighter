class Solution:
    def calculate(self, s: str) -> int:
        op_stack, num_stack = [], []
        # op_stack, num_stack
        # +- -> do it flat(without */), loop
        # */ -> do it right away, whatever new changes made
        # ) found -> do +- in between ()

        def pp():
            while len(op_stack) > 0 and (op_stack[-1] == '*' or op_stack[-1] == '/'):
                op = op_stack.pop()
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                if op == '*':
                    num_stack.append(num1 * num2)
                elif op == '/':
                    num_stack.append(int(num2 / num1))

        def p(num, ops, nums):
            for i in range(len(ops)):
                if ops[i] == '+':
                    num += nums[i]
                else:
                    num -= nums[i]
            return num

        idx = 0
        n = len(s)
        while idx < n:

            # if operator
            if not s[idx].isdigit() and s[idx] != ')':
                op_stack.append(s[idx])
                idx += 1
                continue
            elif s[idx] == ')': # do until popping '('
                ops = []
                nums = []
                # check + and -
                while op_stack[-1] != '(':
                    ops.append(op_stack.pop())
                    nums.append(num_stack.pop())
                op_stack.pop()
                num = num_stack.pop()

                num = p(num, ops, nums)
                num_stack.append(num)
                
                # check * and /
                pp()
                idx += 1
                continue

            # get number
            num = ""
            while idx < n and s[idx].isdigit():
                num += s[idx]
                idx += 1
            num_stack.append(int(num))

            # check * and /
            pp()

        # check * and /
        pp()

        # check + and -
        return p(num_stack[0], op_stack, num_stack[1:])

            


        