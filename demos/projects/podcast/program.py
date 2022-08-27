import service


def main():
    print_header()
    service.download_info()
    show_titles()


def print_header():
    print("-" * 60)
    print("       Testing new things Podcast downloader")
    print("-" * 60)


def show_titles():
    start = service.get_min_episode_id()
    end = service.get_max_episode_id()

    for episode_id in range(start, end + 1):
        show_episode_details(episode_id)


def show_episode_details(episode_id: int):
    episode = service.get_details(episode_id)
    print(f'#{episode.id} ⟶ {episode.title}')


# This means this is directly invoked and not imported
# pycharm these are live templates
if __name__ == '__main__':
    main()
