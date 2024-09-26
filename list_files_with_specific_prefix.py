import os
from typing import List


def func() -> None:
    directory_path = "D:\\Library\\vcpkg\\packages"
    contents = os.listdir(directory_path)
    # print(contents)
    boost_include_paths: List[str] = []
    for content in contents:
        if content.startswith("boost"):
            content_include_path = os.path.join(directory_path, content, "include")
            if os.path.exists(content_include_path):
                boost_include_paths.append(content_include_path)
    # print(boost_include_paths)
    for boost_include_path in boost_include_paths:
        boost_include_path = boost_include_path.replace("\\", "\\\\")
        # print(boost_include_path)
        # print("\"", boost_include_path, "\"")
        # print('"', boost_include_path)
        print(f"\"{boost_include_path}\",")


if __name__ == "__main__":
    func()
