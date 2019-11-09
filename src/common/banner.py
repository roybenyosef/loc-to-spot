from pyfiglet import Figlet


def print_banner():
    f = Figlet('slant')
    print(f.renderText('Location to Spotify!'))