import os
import shutil
import sys
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Cope and sort.')
    parser.add_argument('source_dir', type=str, help='Source dir.')
    parser.add_argument('destination_dir', type=str, nargs='?', default='dist', help='Destination dir.')
    return parser.parse_args()

def copy_files_recursively(source_dir, destination_dir):
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            if os.path.isdir(source_item):
                # Рекурсивно проходимо по піддиректорії
                copy_files_recursively(source_item, destination_dir)
            else:
                _, file_extension = os.path.splitext(item)
                extension_dir = os.path.join(destination_dir, file_extension[1:]) 
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                try:
                    shutil.copy2(source_item, extension_dir)
                    print(f'Copy file {source_item} to {extension_dir}')
                except (shutil.Error, IOError) as e:
                    print(f'Can"t copy {source_item}. Error msg: {e}')

    except Exception as e:
        print(f'Can"t enter folder {source_dir}. Error msg: {e}')

def main():
    args = parse_arguments()
    source_dir = args.source_dir
    destination_dir = args.destination_dir

    if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
        print(f'Source dir {source_dir} doesn"t exist.')
        return

    copy_files_recursively(source_dir, destination_dir)

if __name__ == '__main__':
    main()