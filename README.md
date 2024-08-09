# GitHub Follow/Unfollow Automation Scripts

## Overview

This repository contains two Python scripts designed to help you manage your GitHub followers by automating the process of following and unfollowing users. The scripts are:

1. `follow.py`: This script automatically follows the followers of a specified GitHub user.
2. `unfollow.py`: This script automatically unfollows users you are currently following, except for those you specify as special users.

## Prerequisites

Before using these scripts, ensure you have:

1. **Python** installed on your machine.
2. **GitHub Personal Access Token**: This token is required to authenticate requests to the GitHub API.

## Setup

1. **Clone the repository** to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required Python packages**:

   ```bash
   pip install requests
   ```

3. **Update the scripts** with your GitHub credentials:
   - For `follow.py`, replace `USERNAME` with your GitHub username, `TOKEN` with your GitHub token, and `TARGET_USER` with the username whose followers you want to follow.
   - For `unfollow.py`, replace `token` with your GitHub token and update the `special_users` list with the usernames of people you do not want to unfollow.

## Usage

### 1. Follow Followers of a Specific User

- To follow the followers of a specific GitHub user, run the `follow.py` script:

  ```bash
  python follow.py
  ```

- This script will follow all the followers of the `TARGET_USER` specified in the script. It handles rate limiting by waiting for 60 seconds if the limit is exceeded.

### 2. Unfollow Users

- To unfollow users who are not in your `special_users` list, run the `unfollow.py` script:

  ```bash
  python unfollow.py
  ```

- This script will unfollow all users you currently follow except for those specified in the `special_users` list.

## Disclaimer

Use these scripts at your own risk. Automating interactions on GitHub can have unintended consequences, including the potential to be rate-limited or blocked. Always test scripts in a controlled environment before using them extensively.
