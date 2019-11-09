from src.common.banner import print_banner
from src.config.config_loader import read_config


def main():
    print_banner()
    config = read_config()
    print('Configuration: ')
    print(config)

if __name__ == "__main__":
    main()

