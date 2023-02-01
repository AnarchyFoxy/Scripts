import os

os.system("git status")

print("Which file?")

file = input()

os.system(f"git add {file}")

os.system("echo \"What is your commit message?\"")

commit = input()

os.system(f"git commit -m \"{commit}\"")

os.system("git push")
