import os

cleaned = set()
checked = []

def parse_cookies(cookie_string):
    cookies = {}
    for line in cookie_string.strip().split("\n"):
        if line == "" or line[0] == "#":
            continue
        # Split the line into name-value pairs
        clean = line.strip().split("\t")
        a,b,c = clean[0],clean[-2],clean[-1]

        # Parse the domain and path from the value
        cookies[b] = {
            "value": c,
            "domain": a
        }
    return cookies

def check_cookies(cookies):
    required_cookies = {
        "roblox.": [".ROBLOSECURITY"],
        "google.": ["SID"],
        "paypal.": ["login_email","x-pp-s"],
        "steampowered.": ["steamLoginSecure"],
        "steamcommunity.": ["steamLoginSecure"],
        "geoguessr.": ["_ncfa"],
        "twitter.": ["auth_token"],
        "youtube.": ["__Secure-3PSID"],
        "live.": ["__Host-MSAAUTHP","JSHP"],
        "playvalorant.": ["__Secure-id_hint", "__Secure-access_token"],
        "soundcloud.": ["oauth_token"],
        "amazon.": ["session-id"],
        "disqus.": ["disqusauth"],
        "instagram.": ["sessionid"],
        "spotify.": ["sp_adid", "sp_t"],
        "twitch.": ["twilight-user"],
        "vacban.": ["userinit"],
        "rockstargames.": ["BearerToken"],
        "netflix.": ["NetflixId"],
        "neverlose.": ["auth"],
        "reddit.": ["reddit_session"],
        "sellix.": ["AWSALBTG"],
        "unknownskids.": ["xf_session","xf_user"],
        "duolingo.": ["jwt_token"],
        "leboncoin.": ["luat"],
        "bloxflip.": ["_iidt"],
        "stake.": ["session"],
        "earnit.": ["earnit.gg"],
        "cracked.": ["mybbuser"],
        "azure.":  ["FedAuth"],
        "trello.": ["token"],
        "adobe.": ["forterToken"],
        "facebook.": ["sb"],
        "indeed.": ["SHOE"],
        "shien.": ["sessionID_shein"],
        "wish.": ["sweeper_session"],
        "battlelog.": ["ips4_IPSSessionFront"],
    }
    
    for _, cookie in cookies.items():
        domain = cookie["domain"]
        domain_clean = domain
        if domain[0] == ".":
            domain=domain[1:]
        domain=domain.split(".")[-2]+"."
        if domain in required_cookies:
            if all(required_cookie in [name for name, _ in cookies.items()] for required_cookie in required_cookies[domain]):
                send_to_cleaned(domain_clean)

def send_to_cleaned(domain):
    global cleaned
    global checked
    tmp = domain.split(".")[-2]
    if tmp not in checked:
        checked.append(tmp)
        print(f"{tmp} found!")
    for line in cookie_string.strip().split("\n"):
        if line == "" or line[0] == "#":
            continue
        if domain in line.strip().split("\t")[0]:
            cleaned.add(line)

# Reading the cookie from a file
cookie_file = input("Cookie file name: ")
if cookie_file[0] == '"':
    cookie_file=cookie_file[1:-1]
file_path = "\\".join(cookie_file.split("\\")[:-1])+"\\"

with open(cookie_file, "r") as file:
    cookie_string = file.read()


cookies = parse_cookies(cookie_string)

check_cookies(cookies)

unique_lines = list(cleaned)
unique_lines = "\n".join(unique_lines)
output_file = "clean_"+cookie_file.split("\\")[-1]
if os.path.exists(file_path+output_file):
    while True:
        overwrite = input(f"{output_file} already exists, do you want to overwrite (y,n): ")
        if overwrite in ("y", "Y"):
            break
        elif overwrite in ("n", "N"):
            i = 1
            tmp=output_file.split(".")[0]
            while os.path.exists(f"{file_path}clean_{tmp}_{i}.txt"):
                i += 1
            output_file = f"{tmp}_{i}.txt"
            break

with open(file_path+output_file, "w") as file:
    file.write(unique_lines)
print(f"Finished writing to {file_path+output_file}")
        
    
