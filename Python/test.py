print(type(dir(__builtins__)))
print(len(dir(__builtins__)))

print([s for s in dir(__builtins__) if s.endswith('Warning')])
