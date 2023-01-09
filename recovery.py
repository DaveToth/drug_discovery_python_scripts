import os
from os import path


def recovery():
    path = "/chemical_libraries"
    os.chdir(path)
    run = open("/chemical_libraries/commands.txt", 'r')
    temp = open("/chemical_libraries/recovery.txt", 'w')
    run_lst = run.readlines()
    missing = 0
    found = 0

    for command in run_lst:
        #print(command)
        #exit()
        start_location = command.index("--out") + 6
        end_location = command.index("--center") -1
        output_path = command[start_location:end_location]
        #print("\n\n" + output_path)
        #exit()
        if(os.path.exists(output_path)):
            print("found " + output_path)
            #continue
            found = found + 1
        else:
            print("MISSING " + output_path)
            temp.write(command)
            missing = missing + 1
    temp.close()
    run.close()
    print("found:", found)
    print("missing:", missing)
    os.remove("/chemical_libraries/commands.txt")
    os.rename("/chemical_libraries/recovery.txt", "/chemical_libraries/commands.txt")

def main():
    recovery()


main()
