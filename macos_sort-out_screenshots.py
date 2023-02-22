import glob
import os
import re
import shutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

MACOS_SCREENSHOT_DEFAULT_NAME_PATTERN = \
    r'スクリーンショット (\d{4})-(\d{2})-(\d{2}) (\d{1,2})\.(\d{2})\.(\d{2})\.(?:png|jpg)'


def parse_datetime(string):
    result = re.fullmatch(MACOS_SCREENSHOT_DEFAULT_NAME_PATTERN, string)
    return result


def main():
    file_paths = glob.glob('./*')
    file_paths.sort()  # 出力を見やすくするためのソート 処理には必要ない

    for file_path in file_paths:
        file_name = os.path.split(file_path)[1]
        result = parse_datetime(file_name)
        if result is None:
            continue

        years, month, days, hours, minutes, seconds = map(int, result.groups())
        destination_directory = f"""./{years:0>4}/{years:0>4}-{month:0>2}"""
        print(f'"{file_name}" => "{destination_directory}"')

        os.makedirs(destination_directory, exist_ok=True)
        shutil.move(file_name, destination_directory)


if __name__ == "__main__":
    main()
