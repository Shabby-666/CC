import os
url = input("Enter URL:")
port = input("Enter Port:")
path = input("Enter Path:")
agreement = input("http or https?:")
while True:
  os.system(f"ab -n 1000 -c 1000 {agreement}://{url}:{port}/{path}")
