import subprocess  
import sys  
import os  
import importlib.util  
import importlib.machinery  

def install_package(package):  
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])  


required_packages = ["tqdm", "requests", "beautifulsoup4"]  


for package in required_packages:  
    try:  
        importlib.import_module(package)  
    except ImportError:  
        print(f"Installing {package}...")  
        install_package(package)  
        print(f"Successfully installed {package}.\n")  

import requests  
from tqdm import tqdm
from pyfiglet import figlet_format
import time 

print(figlet_format('SS Collection', font= "larry3d"))  
time.sleep(1)  

ericzim = {  
    "MFTECmd": "https://f001.backblazeb2.com/file/EricZimmermanTools/MFTECmd.zip",  
    "Bstrings": "https://f001.backblazeb2.com/file/EricZimmermanTools/bstrings.zip",  
    "RegistryExplorer": "https://f001.backblazeb2.com/file/EricZimmermanTools/net6/RegistryExplorer.zip",  
    "TimelineExp": "https://f001.backblazeb2.com/file/EricZimmermanTools/net6/TimelineExplorer.zip",  
    "WxTCmd": "https://download.ericzimmermanstools.com/WxTCmd.zip"  
}  
 
nirsoft_tools = {  
    "Winprefetchview": "https://www.nirsoft.net/utils/winprefetchview-x64.zip",  
    "ADSView": "https://www.nirsoft.net/utils/alternatestreamview-x64.zip",  
    "ShellBagsView": "https://www.nirsoft.net/utils/shellbagsview.zip",  
    "USBDeview": "https://www.nirsoft.net/utils/usbdeview.zip",    
}  
 
espouken_tools = {  
    "BAMParser": "https://github.com/spokwn/BAM-parser/releases/download/v1.2.7/BAMParser.exe",  
    "JournalTrace": "https://github.com/spokwn/JournalTrace/releases/download/1.2/JournalTrace.exe",  
    "PrefetchParser": "https://github.com/spokwn/prefetch-parser/releases/download/v1.5.4/PrefetchParser.exe",  
    "ProcessParser": "https://github.com/spokwn/process-parser/releases/download/v0.5.4/ProcessParser.exe",  
    "PcaSvcExec": "https://github.com/spokwn/pcasvc-executed/releases/download/v0.8.6/PcaSvcExecuted.exe"  
}  
other_tools = {
    "Hayabusa": "https://github.com/Yamato-Security/hayabusa/releases/download/v3.1.0/hayabusa-3.1.0-win-x64.zip",
    
}
def download_file(url, save_path):  
    response = requests.get(url, stream=True)  
    total_size = int(response.headers.get('content-length', 0))  

    os.makedirs(os.path.dirname(save_path), exist_ok=True)  

    with open(save_path, "wb") as file, tqdm(  
        desc=os.path.basename(save_path),  
        total=total_size,  
        unit='B',  
        unit_scale=True,  
        unit_divisor=1024,  
    ) as progress_bar:  
        for chunk in response.iter_content(chunk_size=8192):  
            file.write(chunk)  
            progress_bar.update(len(chunk))  

def download_toolset(toolset_name, toolset, save_directory):  
    choice = input(f"Would you like to download {toolset_name} tools? [Y/N] ").strip().upper()  
    if choice != "Y":  
        print(f"Skipping {toolset_name} tools download.")  
        return  

    print(f"Downloading {toolset_name} tools...")  
    time.sleep(2)  
    for tool_name, tool_url in toolset.items():  
        file_extension = os.path.splitext(tool_url)[1]  
        save_path = os.path.join(save_directory, f"{tool_name}{file_extension}")  
        print(f"Downloading {tool_name}...")  
        download_file(tool_url, save_path)  
        print(f"{tool_name} downloaded successfully!")

        def download_toolest(toolset_name, toolset, save_directory):
            choice = input(f"Would you like to download {toolset_name} tools? [Y/N] ")  
            if choice != 'Y':
                print("Skipping")
            return
        print(f"Downloading {toolset_name} tools...")
        file_extension = os.path.splitext(tool_url)[1]
        save_path = os.path.join(save_directory, f"{tool_name}{file_extension}")
        download_file(tool_url, save_path)
        print(f"{tool_name} downloaded successfully!")

save_directory = input("Enter the directory where you want to save the files: ").strip()  

if not save_directory:  
    save_directory = os.getcwd()  
else:  
    save_directory = os.path.abspath(save_directory)  
    save_directory = save_directory.rstrip(os.sep)  

os.makedirs(save_directory, exist_ok=True)  

download_toolset("Eric Zimmerman's", ericzim, save_directory)  
download_toolset("Nirsoft", nirsoft_tools, save_directory)  
download_toolset("Espouken's", espouken_tools, save_directory)
download_toolset("Other", other_tools, save_directory)