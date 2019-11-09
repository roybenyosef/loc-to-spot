from pyfiglet import Figlet


def print_banner():
    f = Figlet('larry3d', 'auto', 'auto', 160)
    print(f.renderText('Local music to Spotify!'))