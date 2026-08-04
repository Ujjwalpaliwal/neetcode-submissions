class Solution:
    def simplifyPath(self, path: str) -> str:
         # Step 1: Split path by '/'
        components = path.split('/')
        # Example: "/neetcode/practice//...///../courses"
        # -> ['', 'neetcode', 'practice', '', '...', '', '', '..', 'courses']
        
        # Step 2: Stack to store valid directories
        stack = []
        
        # Step 3: Process each component
        for component in components:
            if component == '' or component == '.':
                # Empty or current directory -> ignore
                continue
            elif component == '..':
                # Parent directory -> go back
                if stack:  # Only pop if stack is not empty
                    stack.pop()
            else:
                # Valid directory or file name
                stack.append(component)
        
        # Step 4: Build the simplified path
        # Join with '/' and add leading '/'
        return '/' + '/'.join(stack)