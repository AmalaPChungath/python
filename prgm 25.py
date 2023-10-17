d=[(1,'apple'),(2,'mango'),(3,'orange'),(4,'banana')]
d=dict(d)
invert={(v,k) for (k,v) in d.items()}
print(invert)
