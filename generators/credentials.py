#!/usr/bin/env python3
"""
Credentials Generator
Creates comprehensive credential files for all applications and services
"""

from datetime import datetime
from pathlib import Path

from config import (
    USER_NAME, USER_EMAIL, USER_USERNAME, COMPANY_NAME,
    FAKE_CREDENTIALS, INSTALLED_APPLICATIONS, USER_PHONE
)
from utils.helpers import ensure_directory, random_string


class CredentialsGenerator:
    """Generates realistic credential files"""
    
    def __init__(self, base_path):
        self.base_path = Path(base_path)
    
    def generate_master_credentials_file(self):
        """Generate master credentials document"""
        
        content = f"""MASTER CREDENTIALS DOCUMENT
CONFIDENTIAL - FOR PERSONAL USE ONLY

═══════════════════════════════════════════════════════════════════════════

Owner: {USER_NAME}
Email: {USER_EMAIL}
Last Updated: {datetime.now().strftime('%B %d, %Y')}

WARNING: This file contains sensitive login information. Keep secure!

═══════════════════════════════════════════════════════════════════════════

WEB SERVICES & APPLICATIONS

"""
        
        for site, creds in sorted(FAKE_CREDENTIALS.items()):
            content += f"\n{'─'*70}\n"
            content += f"SERVICE: {site}\n"
            content += f"{'─'*70}\n"
            
            if 'username' in creds:
                content += f"Username: {creds['username']}\n"
            if 'email' in creds:
                content += f"Email: {creds['email']}\n"
            
            content += f"Password: {creds['password']}\n"
            content += f"Last Login: {datetime.now().strftime('%B %d, %Y')}\n"
            
            # Add extra details for some services
            if 'github' in site or 'gitlab' in site:
                content += f"2FA Enabled: Yes\n"
                content += f"SSH Key: ~/.ssh/id_rsa\n"
            elif 'aws' in site:
                content += f"Access Key ID: AKIA{random_string(16).upper()}\n"
                content += f"Region: us-west-2\n"
            elif 'bank' in site or 'chase' in site or 'fidelity' in site:
                content += f"Security Question 1: Mother's maiden name -> Johnson\n"
                content += f"Security Question 2: First pet's name -> Max\n"
                content += f"2FA: SMS to {USER_PHONE}\n"
            
            content += "\n"
        
        content += """
═══════════════════════════════════════════════════════════════════════════

WIFI NETWORKS

Home Network:
  SSID: HOME_NETWORK_5G
  Password: SecureHome2024!
  Security: WPA3

Work Network:
  SSID: BeingMalicious_Corp
  Password: [Auto-connect via certificate]
  Security: WPA2-Enterprise

═══════════════════════════════════════════════════════════════════════════

NOTES

• All passwords should be updated every 90 days
• Enable 2FA wherever possible
• Never share these credentials
• Backup this file in encrypted storage
• Use password manager for new accounts

═══════════════════════════════════════════════════════════════════════════
"""
        
        return content
    
    def generate_git_config(self):
        """Generate .gitconfig file content"""
        
        content = f"""# Git Configuration File
# User: {USER_NAME}

[user]
    name = {USER_NAME}
    email = {USER_EMAIL}
    signingkey = GPG_KEY_HERE

[core]
    editor = code --wait
    autocrlf = input
    excludesfile = ~/.gitignore_global

[init]
    defaultBranch = main

[pull]
    rebase = false

[push]
    default = simple
    followTags = true

[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --decorate --all
    last = log -1 HEAD
    unstage = reset HEAD --

[color]
    ui = auto
    branch = auto
    diff = auto
    status = auto

[diff]
    tool = vscode

[merge]
    tool = vscode
    conflictstyle = diff3

[credential]
    helper = store

[url "git@github.com:"]
    insteadOf = https://github.com/

[filter "lfs"]
    clean = git-lfs clean -- %f
    smudge = git-lfs smudge -- %f
    process = git-lfs filter-process
    required = true
"""
        
        return content
    
    def generate_git_credentials(self):
        """Generate git credentials file"""
        
        content = f"""# Git Credentials
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

https://{USER_USERNAME}:{FAKE_CREDENTIALS['github.com']['password']}@github.com
https://{USER_USERNAME}:{FAKE_CREDENTIALS['gitlab.com']['password']}@gitlab.com
"""
        
        return content
    
    def generate_ssh_config(self):
        """Generate SSH config file"""
        
        content = f"""# SSH Configuration
# User: {USER_NAME}

# GitHub
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_github
    IdentitiesOnly yes

# GitLab
Host gitlab.com
    HostName gitlab.com
    User git
    IdentityFile ~/.ssh/id_rsa_gitlab
    IdentitiesOnly yes

# Work Server
Host work-server
    HostName server.beingmalicious.com
    User {USER_USERNAME}
    Port 22
    IdentityFile ~/.ssh/id_rsa_work
    ForwardAgent yes

# AWS EC2
Host aws-ec2
    HostName ec2-54-123-45-67.compute-1.amazonaws.com
    User ec2-user
    IdentityFile ~/.ssh/aws-key.pem
    
# Default settings
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 10
    Compression yes
"""
        
        return content
    
    def generate_docker_config(self):
        """Generate Docker credentials"""
        
        content = f"""# Docker Hub Credentials
# User: {USER_USERNAME}

Docker Hub:
  Username: {USER_USERNAME}
  Password: {FAKE_CREDENTIALS['docker.com']['password']}
  Email: {USER_EMAIL}

Registry: https://index.docker.io/v1/

Repositories:
  - {USER_USERNAME}/web-app:latest
  - {USER_USERNAME}/api-server:v1.2
  - {USER_USERNAME}/database:postgres-14

Last Login: {datetime.now().strftime('%B %d, %Y')}
"""
        
        return content
    
    def generate_aws_credentials(self):
        """Generate AWS credentials file"""
        
        content = f"""# AWS Credentials
# Generated: {datetime.now().strftime('%Y-%m-%d')}

[default]
aws_access_key_id = AKIA{random_string(16).upper()}
aws_secret_access_key = {random_string(40)}
region = us-west-2
output = json

[production]
aws_access_key_id = AKIA{random_string(16).upper()}
aws_secret_access_key = {random_string(40)}
region = us-east-1
output = json

[staging]
aws_access_key_id = AKIA{random_string(16).upper()}
aws_secret_access_key = {random_string(40)}
region = us-west-1
output = json
"""
        
        return content
    
    def generate_npm_credentials(self):
        """Generate NPM credentials"""
        
        content = f"""# NPM Configuration
# User: {USER_USERNAME}

//registry.npmjs.org/:_authToken={random_string(36)}-{random_string(4)}-{random_string(4)}-{random_string(4)}-{random_string(12)}
email={USER_EMAIL}
init-author-name={USER_NAME}
init-author-email={USER_EMAIL}
init-author-url=https://github.com/{USER_USERNAME}
init-license=MIT
"""
        
        return content
    
    def generate_all_credentials(self):
        """Generate all credential files"""
        created_files = []
        
        print("\n[*] Generating credential files...")
        
        creds_folder = self.base_path / "Documents" / "Credentials"
        ensure_directory(creds_folder)
        
        # Master credentials
        master_creds = self.generate_master_credentials_file()
        master_file = creds_folder / "Master_Credentials.txt"
        master_file.write_text(master_creds, encoding='utf-8')
        created_files.append(master_file)
        print(f"    ✓ Master credentials")
        
        # Git config
        git_config = self.generate_git_config()
        git_file = creds_folder / "gitconfig.txt"
        git_file.write_text(git_config, encoding='utf-8')
        created_files.append(git_file)
        print(f"    ✓ Git configuration")
        
        # Git credentials
        git_creds = self.generate_git_credentials()
        git_creds_file = creds_folder / "git_credentials.txt"
        git_creds_file.write_text(git_creds, encoding='utf-8')
        created_files.append(git_creds_file)
        print(f"    ✓ Git credentials")
        
        # SSH config
        ssh_config = self.generate_ssh_config()
        ssh_file = creds_folder / "ssh_config.txt"
        ssh_file.write_text(ssh_config, encoding='utf-8')
        created_files.append(ssh_file)
        print(f"    ✓ SSH configuration")
        
        # Docker config
        docker_config = self.generate_docker_config()
        docker_file = creds_folder / "docker_credentials.txt"
        docker_file.write_text(docker_config, encoding='utf-8')
        created_files.append(docker_file)
        print(f"    ✓ Docker credentials")
        
        # AWS credentials
        aws_creds = self.generate_aws_credentials()
        aws_file = creds_folder / "aws_credentials.txt"
        aws_file.write_text(aws_creds, encoding='utf-8')
        created_files.append(aws_file)
        print(f"    ✓ AWS credentials")
        
        # NPM credentials
        npm_creds = self.generate_npm_credentials()
        npm_file = creds_folder / "npm_config.txt"
        npm_file.write_text(npm_creds, encoding='utf-8')
        created_files.append(npm_file)
        print(f"    ✓ NPM credentials")
        
        return created_files
