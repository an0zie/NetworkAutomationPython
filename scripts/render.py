from jinja2 import Environment, FileSystemLoader
import yaml

#-------------------- Load YAML inventory--------------------
with open("inventory.yaml") as f:
    data = yaml.safe_load(f)

#---------------- Ask user which device they want-------------------------
target_name = input("Enter device hostname (e.g. HR-BR-R19 or CORE-R1): ").strip()

found_device = None
found_site = None

# ---------------Search through all sites and devices---------------
for site_name, site in data["sites"].items():
    for dev in site["devices"]:
        if dev["name"].lower() == target_name.lower():
            found_device = dev
            found_site = site
            break
    if found_device:
        break

if not found_device:
    print(f"Device '{target_name}' not found in inventory.")
    exit()

# -------------Setup Jinja2------------------
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("config.j2")

# --------------Render configuration for THIS device only-------------------
output = template.render(
    name=found_device["name"],
    role=found_device["role"],
    site=found_site,
    lan_svi=found_device.get("lan_svi"),
    uplink=found_device.get("uplink"),
    loopback=found_device.get("loopback"),
    mgmt_ip=found_device.get("mgmt_ip"),
    domain=data["vars"]["domain"],
    login=data["vars"]["login"],
)

print("\n=== GENERATED CONFIG ===\n")
print(output)
