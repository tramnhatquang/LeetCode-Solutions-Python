class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Notice that: if we process each char in the string, it's hard to process the case when .. or ...

        We can split the path by '/' and then process each case:
        Initialize a stack to process each char in the split_list since we have to pop the top of stack if the current char is '..'
        Ex: /home/.. -> after splitting: ['', 'home', '..']
        """
        split_path = path.split('/')
        print(f'Split path: {split_path}')
        stack = []
        for char in split_path:
            if char == '..':
                if stack:
                    stack.pop()
            # case: a no operation when a '.' or an empty string
            elif char == '.' or not char:
                continue
            else:
                # finally, a legitimate directory name, so we add it
                stack.append(char)

        print(f'Stack: {stack}')
        # the canonial path starts with a '/'
        return '/' + '/'.join(stack)

        # time: O(n) = space, n is length of string