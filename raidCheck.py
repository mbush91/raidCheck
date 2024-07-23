import paho.mqtt.client as mqtt
import subprocess

perccli_cmd = ['/bin/perccli64', '/c0' ,'show','all']

def main() :
  print("HI")

  try :
    result = subprocess.run(perccli_cmd, capture_output=True, text=True, check=True)
    output = result.stdout
    error = result.stderr
    print("Command output:")
    print(output)
    print("Command error:")
    print(error)

    with open("/out/last.txt", 'w') as f :
      f.write(output)

  except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")
    print(f"Error output: {e.stderr}")

if __name__ == "__main__":
  main()
