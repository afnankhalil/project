from datetime import datetime as dt

#duration for the website to be blocked
duration = dt(2022,2,12,21)
#sites the user want to block
website = input("enter the website you want to block: ")
site_block = []
site_block.append(website)

#it is a text file from where localhost is taken
host_path = "/etc/host"

#it is describing the local computer address
redirect = input("enter the localhost address: ")

def blocked_sites():
    if dt.now()<duration:
        print("blocked sites")
        with open(host_path, "r+") as hostfile:
            #its looking into the hostfile if there is any website that is inputed by the user
            host_content = hostfile.read()
            for site in site_block:
                #it is showing if the site is not in the hostfile then put the site inside the hostfile to block the website
                if site not in host_path:
                    hostfile.write(redirect + " " + site)
                
    else:
        print("unblock sites")
        with open(host_path, "r+") as hostfile:
            #it is reading the lines that is written in the hostfile
            line = hostfile.readlines()
            for line in line:
                #it is saying that if the site is not in the hostfile then just write the line in the hostfile
                if not(site in host_path for site in site_block):
                    hostfile.write(line)
                    
#it triggers the functions to start running
if __name__ == "__main__":
    blocked_sites()        