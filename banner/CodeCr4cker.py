from pyfiglet import Figlet

# ANSI escape sequences for color
GREEN = "\033[32;1m"
CYAN = "\033[36;1m"
RESET = "\033[0m"

def banner():
    print(GREEN)
    print("+" + "="*66 + "+")
    f = Figlet(font='block')
    print(f.renderText('CodeCr4cker'))
    print("+" + "="*66 + "+")
    print(RESET)

# Simulated client session output
banner()
print(CYAN + "Connected to darknet chat. Type /quit to exit." + RESET)
prompt = GREEN + "root@localhost:~# " + RESET
promp = RED + "root@localhost:~# " + RESET
print()
print(prompt + "Welcome")

print(prompt + "What is your Name")
print(promp + input(""))
print(prompt + "How Are you?")
print(promp + input(""))

