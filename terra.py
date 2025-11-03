import subprocess

import subprocess

def terraform_run(command):
    process = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print("STDOUT:\n", process.stdout)
    print("STDERR:\n", process.stderr)
    print(f"\nExit code: {process.returncode}")


directory="/Users/Admin/Desktop/Python/python-workshop-practice/terra-automate/Wanderlust-Mega-Project/terraform"
#command = f"terraform -chdir={directory} init"
#command = f"terraform -chdir={directory} plan"
#command = f"terraform -chdir={directory} apply -auto-approve"
command = f"terraform -chdir={directory} destroy -auto-approve"

terraform_run(command)