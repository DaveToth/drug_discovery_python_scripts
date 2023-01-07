import os
import pathlib

def vina(receptor, ccoords, scoords, exh, cpus, seed):
    path_to_vina = "/chemical_libraries/vina_daves_version"
    run_commands = open("/home/toth/run.txt", 'w')

    path = "/chemical_libraries"
    os.chdir(path)
    files = os.walk(os.getcwd())

    for fi in files:
        if(fi[1] == []):
            for i in range(len(fi[2])):
                ligand = fi[0] + "/" + fi[2][i]
                if(ligand.endswith("COMBINED")):
                    continue
                elif("OUT" in ligand):
                    continue
                else:
                    out = fi[0] + "/OUT" + fi[2][i]
                    run_commands.write(command(path_to_vina, receptor, ligand, out, ccoords, scoords, exh, cpus, seed) + "\n")

    run_commands.close()


def command(path_to_vina, receptor, ligand, out, ccoords, scoords , exh, cpus, seed):
    runCommand = path_to_vina + " --receptor " + receptor + " --ligand " + ligand + " --out " + out + " --center_x " + str(ccoords[0]) + " --center_y " + str(ccoords[1]) + " --center_z " +  str(ccoords[2]) + " --size_x " + str(scoords[0]) + " --size_y " + str(scoords[1]) + " --size_z " +  str(scoords[2]) + " --exhaustiveness " +  str(exh) + " --cpu " +  str(cpus) + " --seed " +  str(seed)
    return runCommand


def main():
    vina("/home/toth/NSP_12_nosupport.pdbqt", [105.791518869, 86.3353519887, 79.0370232688], [30.1507643113, 32.4340164565, 35.9012230317], 8, 1, 21)

main()
