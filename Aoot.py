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

def ensure_real_root():
    """Ensure the user has true root access."""
    if not is_root():
        print("No real root access detected.")
        print("Please ensure you are running Termux with root privileges.")
        print("Install a root manager (Magisk) if necessary.")
        exit(1)

def install_dependencies():
    """Install necessary packages like fish shell, figlet, and any other useful utilities."""
    print("Installing required packages...")
    subprocess.run(["pkg", "update", "-y"])
    subprocess.run(["pkg", "install", "fish", "-y"])
    subprocess.run(["pkg", "install", "figlet", "-y"])
    subprocess.run(["pkg", "install", "zsh", "-y"])  # Adding zsh for additional shell options
    subprocess.run(["pkg", "install", "tsu", "-y"])  # Ensuring tsu for root access
    print("Dependencies installed.")

def configure_fish_with_powerline():
    """Configure fish shell with a modern, powerful UI using powerline and figlet for fonts."""
    fish_config_path = os.path.expanduser("~/.config/fish/config.fish")
    
    # Ensure the fish configuration directory exists
    os.makedirs(os.path.dirname(fish_config_path), exist_ok=True)

    # Custom fish prompt with figlet and colorful modern UI
    with open(fish_config_path, "w") as config_file:
        config_file.write("""
# Custom fish prompt using figlet for AiRoot
function fish_prompt
    set_color red
    figlet -f slant AiRoot
    set_color yellow
    echo -n (whoami)@localhost (prompt_pwd) ' -> '
    set_color normal
end
""")
    print("Fish shell has been configured with a modern UI and custom prompt.")

def set_fish_as_default():
    """Set fish as the default shell for Termux."""
    print("Setting fish as the default shell...")
    subprocess.run(["chsh", "-s", "/data/data/com.termux/files/usr/bin/fish"])

def main():
    """Main function to handle root access and configuration."""
    print("Starting AirRoot setup...")

    # Ensure the user has real root access
    ensure_real_root()

    # Install root tools like tsu and fish shell
    install_tsu()

    # Install required dependencies
    install_dependencies()

    # Configure the shell with a professional and aesthetic modern UI
    configure_fish_with_powerline()

    # Set fish as the default shell
    set_fish_as_default()

    print("Setup complete. Please restart your terminal to apply changes and enjoy your epic root shell experience!")

if __name__ == "__main__":
    main()
