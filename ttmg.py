import os
from sys import exit as exx
import time
import uuid
import re
from subprocess import Popen,PIPE
import shutil,urllib.request,subprocess

HOME = os.path.expanduser("~")
CWD = os.getcwd()

def checkAvailable(path_="", userPath=False):
    from os import path as _p

    if path_ == "":
        return False
    else:
        return (
            _p.exists(path_)
            if not userPath
            else _p.exists(f"/usr/local/sessionSettings/{path_}")
        )

def accessSettingFile(file="", setting={}, v=True):
    from json import load, dump

    if not isinstance(setting, dict):
        if v:print("Only accept Dictionary object.")
        exx()
    fullPath = f"/usr/local/sessionSettings/{file}"
    try:
        if not len(setting):
            if not checkAvailable(fullPath):
                if v:print(f"File unavailable: {fullPath}.")
                exx()
            with open(fullPath) as jsonObj:
                return load(jsonObj)
        else:
            with open(fullPath, "w+") as outfile:
                dump(setting, outfile)
    except:
        if v:print(f"Error accessing the file: {fullPath}.")

def displayUrl(data, btc='b', pNamU='Public URL: ', EcUrl=None, ExUrl=None, cls=True):
    from IPython.display import HTML, clear_output

    if cls:
        clear_output()
    showTxT = pNamU
    showUrL = ExUrl
    if btc == 'b':
          # blue
          bttxt = 'hsla(210, 50%, 85%, 1)'
          btcolor = 'hsl(210, 80%, 42%)'
          btshado = 'hsla(210, 40%, 52%, .4)'
    elif btc == 'g':
          # green
          bttxt = 'hsla(110, 50%, 85%, 1)'
          btcolor = 'hsla(110, 86%, 56%, 1)'
          btshado = 'hsla(110, 40%, 52%, .4)'
    elif btc == 'r':
          # red
          bttxt = 'hsla(10, 50%, 85%, 1)'
          btcolor = 'hsla(10, 86%, 56%, 1)'
          btshado = 'hsla(10, 40%, 52%, .4)'

    return display(HTML('''<style>@import url('https://fonts.googleapis.com/css?family=Source+Code+Pro:200,900');  :root {   --text-color: '''+bttxt+''';   --shadow-color: '''+btshado+''';   --btn-color: '''+btcolor+''';   --bg-color: #141218; }  * {   box-sizing: border-box; } button { position:relative; padding: 10px 20px;     border: none;   background: none;   cursor: pointer;      font-family: "Source Code Pro";   font-weight: 900;   font-size: 100%;     color: var(--text-color);      background-color: var(--btn-color);   box-shadow: var(--shadow-color) 2px 2px 22px;   border-radius: 4px;    z-index: 0;     overflow: hidden;    }  button:focus {   outline-color: transparent;   box-shadow: var(--btn-color) 2px 2px 22px; }  .right::after, button::after {   content: var(--content);   display: block;   position: absolute;   white-space: nowrap;   padding: 40px 40px;   pointer-events:none; }  button::after{   font-weight: 200;   top: -30px;   left: -20px; }   .right, .left {   position: absolute;   width: 100%;   height: 100%;   top: 0; } .right {   left: 66%; } .left {   right: 66%; } .right::after {   top: -30px;   left: calc(-66% - 20px);      background-color: var(--bg-color);   color:transparent;   transition: transform .4s ease-out;   transform: translate(0, -90%) rotate(0deg) }  button:hover .right::after {   transform: translate(0, -47%) rotate(0deg) }  button .right:hover::after {   transform: translate(0, -50%) rotate(-7deg) }  button .left:hover ~ .right::after {   transform: translate(0, -50%) rotate(7deg) }  /* bubbles */ button::before {   content: '';   pointer-events: none;   opacity: .6;   background:     radial-gradient(circle at 20% 35%,  transparent 0,  transparent 2px, var(--text-color) 3px, var(--text-color) 4px, transparent 4px),     radial-gradient(circle at 75% 44%, transparent 0,  transparent 2px, var(--text-color) 3px, var(--text-color) 4px, transparent 4px),     radial-gradient(circle at 46% 52%, transparent 0, transparent 4px, var(--text-color) 5px, var(--text-color) 6px, transparent 6px);    width: 100%;   height: 300%;   top: 0;   left: 0;   position: absolute;   animation: bubbles 5s linear infinite both; }  @keyframes bubbles {   from {     transform: translate();   }   to {     transform: translate(0, -66.666%);   } }    Resources</style><center><a href="'''+showUrL+'''" target="_blank"><div style="width: 570px;   height: 80px; padding-top:15px"><button style='--content: "'''+showTxT+'''";'">   <div class="left"></div>'''+showTxT+'''<div class="right"></div> </div></button></a></center>'''))

def findProcess(process, command="", isPid=False):
    from psutil import pids, Process

    if isinstance(process, int):
        if process in pids():
            return True
    else:
        for pid in pids():
            try:
                p = Process(pid)
                if process in p.name():
                    for arg in p.cmdline():
                        if command in str(arg):
                            return True if not isPid else str(pid)
                        else:
                            pass
                else:
                    pass
            except:
                continue

def installAutoSSH():
    if checkAvailable("/usr/bin/autossh"):
        return
    else:
        runSh("apt-get install autossh -qq -y")

def runSh(args, *, output=False, shell=False, cd=None):
    import subprocess, shlex

    if not shell:
        if output:
            proc = subprocess.Popen(
                shlex.split(args), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cd
            )
            while True:
                output = proc.stdout.readline()
                if output == b"" and proc.poll() is not None:
                    return
                if output:
                    print(output.decode("utf-8").strip())
        return subprocess.run(shlex.split(args), cwd=cd).returncode
    else:
        if output:
            return (
                subprocess.run(
                    args,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    cwd=cd,
                )
                .stdout.decode("utf-8")
                .strip()
            )
        return subprocess.run(args, shell=True, cwd=cd).returncode

def loadingAn(name="cal"):
      from IPython.display import HTML

      if name == "cal":
          return display(HTML('<style>.lds-ring {   display: inline-block;   position: relative;   width: 34px;   height: 34px; } .lds-ring div {   box-sizing: border-box;   display: block;   position: absolute;   width: 34px;   height: 34px;   margin: 4px;   border: 5px solid #cef;   border-radius: 50%;   animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;   border-color: #cef transparent transparent transparent; } .lds-ring div:nth-child(1) {   animation-delay: -0.45s; } .lds-ring div:nth-child(2) {   animation-delay: -0.3s; } .lds-ring div:nth-child(3) {   animation-delay: -0.15s; } @keyframes lds-ring {   0% {     transform: rotate(0deg);   }   100% {     transform: rotate(360deg);   } }</style><div class="lds-ring"><div></div><div></div><div></div><div></div></div>'))
      elif name == "lds":
          return display(HTML('''<style>.lds-hourglass {  display: inline-block;  position: relative;  width: 34px;  height: 34px;}.lds-hourglass:after {  content: " ";  display: block;  border-radius: 50%;  width: 34px;  height: 34px;  margin: 0px;  box-sizing: border-box;  border: 20px solid #dfc;  border-color: #dfc transparent #dfc transparent;  animation: lds-hourglass 1.2s infinite;}@keyframes lds-hourglass {  0% {    transform: rotate(0);    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);  }  50% {    transform: rotate(900deg);    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);  }  100% {    transform: rotate(1800deg);  }}</style><div class="lds-hourglass"></div>'''))

def textAn(TEXT, ty='d'):
      from IPython.display import HTML

      if ty == 'd':
            return display(HTML('''<style>@import url(https://fonts.googleapis.com/css?family=Raleway:400,700,900,400italic,700italic,900italic);#wrapper {   font: 17px 'Raleway', sans-serif;animation: text-shadow 1.5s ease-in-out infinite;    margin-left: auto;    margin-right: auto;    }#container {    display: flex;    flex-direction: column;    float: left;     }@keyframes text-shadow { 0% 20% {          transform: translateY(-0.1em);        text-shadow:             0 0.1em 0 #0c2ffb,             0 0.1em 0 #2cfcfd,             0 -0.1em 0 #fb203b,             0 -0.1em 0 #fefc4b;    }    40% {          transform: translateY(0.1em);        text-shadow:             0 -0.1em 0 #0c2ffb,             0 -0.1em 0 #2cfcfd,             0 0.1em 0 #fb203b,             0 0.1em 0 #fefc4b;    }       60% {        transform: translateY(-0.1em);        text-shadow:             0 0.1em 0 #0c2ffb,             0 0.1em 0 #2cfcfd,             0 -0.1em 0 #fb203b,             0 -0.1em 0 #fefc4b;    }   }@media (prefers-reduced-motion: reduce) {    * {      animation: none !important;      transition: none !important;    }}</style><div id="wrapper"><div id="container">'''+TEXT+'''</div></div>'''))
      elif ty == 'twg':
            textcover = str(len(TEXT)*0.55)
            return display(HTML('''<style>@import url(https://fonts.googleapis.com/css?family=Anonymous+Pro);.line-1{font-family: 'Anonymous Pro', monospace;    position: relative;   border-right: 1px solid;    font-size: 15px;   white-space: nowrap;    overflow: hidden;    }.anim-typewriter{  animation: typewriter 0.4s steps(44) 0.2s 1 normal both,             blinkTextCursor 600ms steps(44) infinite normal;}@keyframes typewriter{  from{width: 0;}  to{width: '''+textcover+'''em;}}@keyframes blinkTextCursor{  from{border-right:2px;}  to{border-right-color: transparent;}}</style><div class="line-1 anim-typewriter">'''+TEXT+'''</div>'''))

def updateCheck(self, Version):
    class UpdateChecker(object):

      def __init__(self):
          getMessage = self.getMessage
          getVersion = self.getVersion

      def getVersion(self, currentTag):
          from urllib.request import urlopen
          from lxml.etree import XML

          url = self.URL
          update = urlopen(url).read()
          root = XML(update)
          cur_version = root.find(".//"+currentTag)
          current = cur_version.text
          return current

      def getMessage(self, messageTag):
          from urllib.request import urlopen
          from lxml.etree import XML

          url = self.URL
          update = urlopen(url).read()
          root = XML(update)
          mess = root.find(".//"+messageTag)
          message = mess.text
          return message

    check = UpdateChecker()
    check.URL = "https://raw.githubusercontent.com/hackingguy/Bug-Hunting-Colab/master/update.xml"
    currentVersion = check.getVersion("currentVersion")
    message = check.getMessage("message")

    if Version != currentVersion:
        from IPython.display import HTML

        print("Script Update Checker: Version "+currentVersion+" "+message+" Your version: "+Version+"")
        display(HTML('<div style="background-color: #4caf50!important;text-align: center;padding-top:-1px;padding-bottom: 9px;boder:1px"><h4 style="padding-top:5px"><a target="_blank" href="https://colab.research.google.com/github/hackingguy/Bug-Hunting-Colab/" style="color: #fff!important;text-decoration: none;color: inherit;background-color:transparent;font-family: Segoe UI,Arial,sans-serif;font-weight: 400;font-size: 20px;">Open Latest Version</a></h4></div>'))
        return True
    else:
        print("Script Update Checker: Your script is up to date")

def _download(url, path):
    try:
        with urllib.request.urlopen(url) as response:
            with open(path, 'wb') as outfile:
                shutil.copyfileobj(response, outfile)
    except:
        print("Failed to download ", url)
        raise

def argoTunnel():
    _download("https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.tgz", "cloudflared.tgz")
    shutil.unpack_archive("cloudflared.tgz")
    cfd_proc = subprocess.Popen(
        ["./cloudflared", "tunnel", "--url", "ssh://localhost:22", "--logfile", "cloudflared.log", "--metrics", "localhost:49589"],
        stdout = subprocess.PIPE,
        universal_newlines = True
        )
    time.sleep(4)
    if cfd_proc.poll() != None:
        raise RuntimeError("Failed to run cloudflared. Return code:" + str(cloudflared.returncode) + "\nSee clouldflared.log for more info.")
    hostname = None
    # Sometimes it takes long time to display user host name in cloudflared metrices.
    for i in range(20):
        with urllib.request.urlopen("http://127.0.0.1:49589/metrics") as response:
            text = str(response.read())
            sub = "\\ncloudflared_tunnel_user_hostnames_counts{userHostname=\"https://"
            begin = text.find(sub)
            if begin == -1:
                time.sleep(10)
                #print("Retry reading cloudflared user hostname")
                continue
            end = text.index("\"", begin + len(sub))
            hostname = text[begin + len(sub) : end]
            break
        if hostname == None:
            raise RuntimeError("Failed to get user hostname from cloudflared")
    return hostname
