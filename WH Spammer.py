try:
	import requests, os, colorama
except:
	os.system('pip install requests')
	os.system('pip install colorama')

from colorama import Fore

os.system('cls')
os.system('title Simple Webhook Spammer - By Kaneki')

banner = f"""
			██╗    ██╗██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗███████╗██████╗ 
			██║    ██║██║  ██║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗
			██║ █╗ ██║███████║    ███████╗██████╔╝███████║██╔████╔██║█████╗  ██████╔╝
			██║███╗██║██╔══██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗
			╚███╔███╔╝██║  ██║    ███████║██║     ██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
			 ╚══╝╚══╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
 


""".replace('█',f'\033[1;31m█{Fore.RESET}')


def main():
	print(banner)
	webhook = input(f"[{Fore.RED}>{Fore.RESET}] - Webhook Link > ")
	username = input(f"[{Fore.RED}>{Fore.RESET}] - Name of Webhook > ")
	picture = input(f"[{Fore.RED}>{Fore.RESET}] - Picture (default None) > ")
	message = input(f"[{Fore.RED}>{Fore.RESET}] - Message to Spam > ")

	data = {
	    'content': message,
	    'username': username,
	    'avatar_url': picture
	}

	sent = 0
	failed = 0

	while True:
		r = requests.post(webhook, data=data)

		if r.status_code == 204:
			sent += 1
			print(f"{Fore.GREEN}[+] - Message sent !{Fore.RESET}")
			os.system(f'title Simple Webhook Spammer ^| By Kaneki - Sent : {sent} ^| Failed : {failed}')
		else:
			failed += 1
			print(f"{Fore.RED}[-] - Couldn't send !{Fore.RESET}")
			os.system(f'title Simple Webhook Spammer ^| By Kaneki - Sent : {sent} ^| Failed : {failed}')


main()
