# siwp2005-final-project


# Installation
## Install Dokcer and Docker Compose

## Ubuntu

## Windows
> if you are using windows, you can run the ubuntu image using your windows `WSL` subsystem
## WSL 2 with ubuntu Installation
### Enable wsl
- Open PowerShell as Administrator
- Enable WSL feature
    ```
      dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

    ```
- Enable Virtual Machine
    ```
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

    ```
    ![image](https://hackmd.io/_uploads/Hkps9rsV0.png)
- Restart your computer. 
> you need to restart your windows to see the effect whether you can run wsl on your windows
    
- Validate your wsl
    ```
    wsl --version
    ```
- ![image](https://hackmd.io/_uploads/HkL7oHiVC.png)
- set WSL 2 as default version
    ```
    wsl --set-default-version 2
    ```
- ![image](https://hackmd.io/_uploads/SyeviHsVR.png)


### Using Ubuntu on WSL 2

- check which linux distro are availables on your windows 
```
wsl --list --online
```
![image](https://hackmd.io/_uploads/SkS3aHs40.png)

- install ubuntu
```
wsl.exe --install -d <DistroName>
```
please change `<DistroName>` with the ubuntu distro list on your windows, we will use `Ubuntu-22.04`
`wsl.exe --install -d Ubuntu-22.04` then follow the instruction set ubuntu username and password

![image](https://hackmd.io/_uploads/ByBsy8iEA.png)
