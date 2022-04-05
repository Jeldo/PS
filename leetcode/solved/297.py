class Codec:
    def serialize(self, root):
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data):
        if data == '#':
            return None

        values = deque(data.split(' '))
        head = node = TreeNode(values.popleft())
        nodes = deque([node])

        while values:
            node = nodes.popleft()
            value = values.popleft()
            if value != '#':
                node.left = TreeNode(val=value)
                nodes.append(node.left)
            else:
                node.left = None
            value = values.popleft()
            if value != '#':
                node.right = TreeNode(val=value)
                nodes.append(node.right)
            else:
                node.right = None

        return head
