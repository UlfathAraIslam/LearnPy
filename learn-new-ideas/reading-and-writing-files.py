with open("hello.txt", "w",encoding="utf-8") as f:
    f.write("হ্যালো, こんにちは")
with open("hello.txt",'r',encoding="utf-8") as f:
    print(f.read())