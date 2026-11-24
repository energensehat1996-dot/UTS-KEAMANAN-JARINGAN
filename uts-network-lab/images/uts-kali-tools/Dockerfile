FROM kalilinux/kali-rolling
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap net-tools iputils-ping curl dnsutils tcpdump whois \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
