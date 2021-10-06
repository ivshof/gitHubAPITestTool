# Test tool to check git hub commit changes

import sys
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s')

def main():

    # Ensure correct usage of input parameters
    if len(sys.argv) < 4 or len(sys.argv) > 6:
        logging.info("Input parameters ERROR")
        sys.exit("Usage: python git-test.py repo apiToken environment {commitHash}")

    elif len(sys.argv) == 4:
        commitHash = "none"

    elif len(sys.argv) == 5:
        commitHash = str(sys.argv[4])

    repo = str(sys.argv[1])
    apiToken = str(sys.argv[2])
    environment = str(sys.argv[3])

    logging.info(f"Entered input parameters. repo = {repo}, apiToken = {apiToken}, environment = {environment}, commitHash = {commitHash}")


if __name__ == "__main__":
    main()