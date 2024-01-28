import subprocess

def run_traceroute(destination):
    command = ['traceroute', destination]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        return output.decode('utf-8')
    else:
        return error.decode('utf-8')

# Example usage
destination =input('write a domain or url: ')
result = run_traceroute(destination)
print(result)