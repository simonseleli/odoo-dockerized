FROM odoo:16.0

# Root section: install dependencies
USER root

# Install sudo, git, zsh, curl
RUN apt-get update && apt-get install -y \
    sudo \
    git \
    zsh \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create vscode user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && usermod -s /bin/bash $USERNAME

# Make Odoo directories writable
RUN mkdir -p /var/lib/odoo/sessions \
    && chown -R $USERNAME:$USERNAME /var/lib/odoo

# Switch to vscode user
USER $USERNAME

# Custom bash prompt: user (green) ➜ dir (blue) (branch in red) $
RUN echo 'parse_git_branch() {' >> ~/.bashrc \
    && echo '    git branch 2> /dev/null | sed -e "/^[^*]/d" -e "s/* \(.*\)/ (\1)/"' >> ~/.bashrc \
    && echo '}' >> ~/.bashrc \
    && echo 'export PS1="\[\033[32m\]\u ➜ \[\033[34m\]\w\[\033[31m\]\$(parse_git_branch)\[\033[00m\] $ "' >> ~/.bashrc

WORKDIR /workspace
