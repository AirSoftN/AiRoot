import os
import subprocess
import shutil

def is_root():
    """Check if the user has root access."""
    return os.geteuid() == 0

def install_tsu():
    """Install tsu to enable root access."""
    if shutil.which("tsu") is None:
        print("Installing tsu to enable root access...")
        subprocess.run(["pkg", "install", "tsu", "-y"])
        print("tsu installed. You can now access root using 'tsu'.")
    else:
        print("'tsu' is already installed.")

def install_dependencies():
    """Install necessary packages like fish shell and figlet."""
    print("Installing required packages...")
    subprocess.run(["pkg", "update", "-y"])
    subprocess.run(["pkg", "install", "fish", "-y"])
    subprocess.run(["pkg", "install", "figlet", "-y"])
    print("Dependencies installed.")

def configure_fish(simulate_root=False):
    """Configure fish shell with custom prompt."""
    fish_config_path = os.path.expanduser("~/.config/fish/config.fish")
    
    # Ensure the fish configuration directory exists
    os.makedirs(os.path.dirname(fish_config_path), exist_ok=True)
    
    # Customize the prompt
    with open(fish_config_path, "w") as config_file:
        if simulate_root:
            config_file.write("""
# Simulate a root prompt for non-root users
function fish_prompt
    set_color red
    figlet -f slant AiRoot
    set_color normal
    echo -n "AirRoot@localhost (fake-root) " (prompt_pwd)
    echo -n ' -> '
end
""")
        else:
            config_file.write("""
# Real root prompt
function fish_prompt
    set_color green
    figlet -f slant AiRoot
    set_color normal
    echo -n (whoami)@localhost (prompt_pwd)
    echo -n ' -> '
end
""")
    print("Fish shell has been configured with the custom prompt.")

def set_fish_as_default():
    """Set fish as the default shell."""
    print("Setting fish as the default shell...")
    subprocess.run(["chsh", "-s", "/data/data/com.termux/files/usr/bin/fish"])

def main():
    """Main function to manage root access and configuration."""
    print("Starting AirRoot setup...")

    # Check if user has root access
    root_access = is_root()

    if root_access:
        print("Root access detected.")
    else:
        print("Root access not detected. Simulating root environment...")
        install_tsu()

    # Install dependencies (fish shell, figlet, etc.)
    install_dependencies()

    # Configure fish shell based on whether root access is available
    if root_access:
        configure_fish(simulate_root=False)
    else:
        configure_fish(simulate_root=True)

    # Set fish as the default shell
    set_fish_as_default()

    print("Setup complete. Please restart your terminal to apply changes.")

if __name__ == "__main__":
    main()

# To run the script: python main.py
