import os
import subprocess
import shutil

repo_dir = r'C:\Users\parent\Coding\Open-Source Projects\HyperSpace'
Command = []
print("Welcome to HyperSpace")
print()
print("Current App:", end=' ')
if os.path.exists(r"C:\\Users\\parent\\Coding\\Open-Source Projects\\HyperSpace\\blender"):
    print("Blender")
elif os.path.exists(r"C:\\Users\\parent\\Coding\\Open-Source Projects\\HyperSpace\\krita"):
    print("Krita")
else:
    print("No Apps Yet!")
print()
print()
def port(App):
    if App == "blender":
        if not os.path.exists(r"C:\\Users\\parent\\Coding\\Open-Source Projects\\HyperSpace\\blender"):
            subprocess.run(['git', 'checkout', 'main'], cwd=repo_dir)
            subprocess.run(['git','reset','--hard'], cwd=repo_dir)
            subprocess.run(['git', 'pull'], cwd=repo_dir)
            print("Porting Completed.")
            print("Hang on while we open the app for you.")
            subprocess.run([r"C:\Users\parent\Coding\Open-Source Projects\HyperSpace\blender\blender-4.3.0-windows-x64\blender-4.3.0-windows-x64\blender-launcher.exe"])
        else:
            print("Action already completed.")
            subprocess.run([r"C:\Users\parent\Coding\Open-Source Projects\HyperSpace\blender\blender-4.3.0-windows-x64\blender-4.3.0-windows-x64\blender-launcher.exe"])
    elif App == "krita":
        if not os.path.exists(r"C:\\Users\\parent\\Coding\\Open-Source Projects\\HyperSpace\\krita"):
            subprocess.run(['git', 'checkout', 'krita'], cwd=repo_dir)
            subprocess.run(['git','reset','--hard'], cwd=repo_dir)
            subprocess.run(['git', 'pull'], cwd=repo_dir)
            print("Porting Completed.")
            print("Hang on while we open the app for you.")
            subprocess.run([r"C:\Users\parent\Coding\Open-Source Projects\HyperSpace\krita\krita-x64-5.2.6\krita-x64-5.2.6\bin\krita.exe"])
        else:
            print("Action already completed.")
            subprocess.run([r"C:\Users\parent\Coding\Open-Source Projects\HyperSpace\krita\krita-x64-5.2.6\krita-x64-5.2.6\bin\krita.exe"])

def swipe(App):
    if App == "blender":
        if os.path.exists(r"C:\\Users\\parent\\Coding\\Open-Source Projects\\HyperSpace\\blender"):
            # git checkout main
            subprocess.run(['git', 'checkout', 'main'], cwd=repo_dir)
            # git lfs install
            subprocess.run(['git', 'lfs', 'install'], cwd=repo_dir)
            # git lfs track "blender/blender-4.3.0-windows-x64/blender-4.3.0-windows-x64/blender.pdb"
            subprocess.run(['git', 'lfs', 'track', 'blender/blender-4.3.0-windows-x64/blender-4.3.0-windows-x64/blender.pdb'], cwd=repo_dir)
            #  git lfs track "blender/blender-4.3.0-windows-x64/blender-4.3.0-windows-x64/cycles_kernel_oneapi_aot.dll"
            subprocess.run(['git', 'lfs', 'track', 'blender/blender-4.3.0-windows-x64/blender-4.3.0-windows-x64/cycles_kernel_oneapi_aot.dll'], cwd=repo_dir)
            subprocess.run(['git', 'add', '--all'], cwd=repo_dir)
            subprocess.run(['git', 'commit', '-m', 'Auto commit'], cwd=repo_dir)
            subprocess.run(['git', 'push', 'origin', 'main'], cwd=repo_dir)
            # Remove-Item -Path "C:\Users\parent\Coding\Open-Source Projects\HyperSpace\blender" -Recurse -Force
            shutil.rmtree(r"C:\\Users\\parent\\Coding\\Open-Source Projects\\HyperSpace\\blender")
            print("Swiping Completed.")
        else:
            print("Action already completed.")
    elif App == "krita":
        if os.path.exists(r"C:\\Users\\parent\\Coding\\Open-Source Projects\\HyperSpace\\krita"):
            # git checkout main
            subprocess.run(['git', 'checkout', 'krita'], cwd=repo_dir)
            subprocess.run(['git', 'add', '--all'], cwd=repo_dir)
            subprocess.run(['git', 'commit', '-m', 'Auto commit'], cwd=repo_dir)
            subprocess.run(['git', 'push', '--set-upstream', 'origin', 'krita'], cwd=repo_dir)
            # Remove-Item -Path "C:\Users\parent\Coding\Open-Source Projects\HyperSpace\krita" -Recurse -Force
            shutil.rmtree(r"C:\\Users\\parent\\Coding\\Open-Source Projects\\HyperSpace\\krita")
            print("Swiping Completed.")
        else:
            print("Action already completed.")

while True:
    print()
    RawCommand = input("Enter Command: ")
    Command = RawCommand.lower().split(" ")
    if len(Command) == 1:
        print("Invalid Command!")
        print("2nd Argument Missing.")
    elif Command[0] == "port":
        port(Command[1])
    elif Command[0] == "swipe":
        swipe(Command[1])
    elif Command[0] == "start":
        if Command[1] == "blender":
            print("Starting Blender...")
            subprocess.run([r"C:\Users\parent\Coding\Open-Source Projects\HyperSpace\blender\blender-4.3.0-windows-x64\blender-4.3.0-windows-x64\blender-launcher.exe"])
        elif Command[1] == "krita":
            print("Starting Krita...")
            subprocess.run([r"C:\Users\parent\Coding\Open-Source Projects\HyperSpace\krita\krita-x64-5.2.6\krita-x64-5.2.6\bin\krita.exe"])
    elif Command[0] == "exit":
        break
