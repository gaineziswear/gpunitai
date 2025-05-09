# install_cuquantum.py
import subprocess
import os
import sys

cuda_versions = ["12", "11"]

def has_cuda_libs():
    for version in cuda_versions:
        lib = f"libnvrtc.so.{version}"
        try:
            subprocess.run(["ldconfig", "-p"], check=True, stdout=subprocess.PIPE)
            subprocess.run(["ldconfig", "-p"], check=True, stdout=subprocess.PIPE).stdout.decode().index(lib)
            return version
        except:
            continue
    return None

def install_cuquantum(version):
    try:
        print(f"Installing cuquantum-cu{version}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"cuquantum-cu{version}"])
    except subprocess.CalledProcessError:
        print(f"[!] Failed to install cuquantum-cu{version}")
        sys.exit(1)

def main():
    version = has_cuda_libs()
    if version:
        install_cuquantum(version)
    else:
        print("⚠️  CUDA not detected. Skipping cuquantum installation.")

if __name__ == "__main__":
    main()
