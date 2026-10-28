def format_channel_label(channel):
    return f"Release channel: {channel.upper()}"


if __name__ == "__main__":
    print(format_channel_label("development"))
