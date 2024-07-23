import paho.mqtt.client as mqtt
import re
import subprocess
import json

perccli_cmd = ['/bin/perccli64', '/c0' ,'show','all']

def parse_perccli(output) -> dict :

  out = {}

  pattern = re.compile(r'([0-9]+)\s+([0-9]+)\s+([0-9]+)\s+([0-9]+:[0-9]+)\s+([0-9]+)\s+(DRIVE|RAID[0-5])\s+(Onln|Rbld|Optl|Dgrd|Pdgd|Offln)')
  m = pattern.findall(output)

  for disk in m :
    k = 'DRIVE'+disk[0]
    if k in out :
      d = "DISK"+disk[2]
      if d not in out[k] :
        out[k][d] = disk[6]
      else :
        raise Exception("Repeated Disk!")
    else :
      out[k] = {
       "DISK"+disk[2] : disk[6]
      }

  fmt = json.dumps(out,indent=2)
  print(fmt)

  return out

def report_disk(states) :
  pass

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
