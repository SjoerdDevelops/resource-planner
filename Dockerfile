from ubuntu:22.04

# Install python (version 3.10 on ubuntu 22.04)
# From Qt 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    qt6-base-dev \
    qt6-tools-dev-tools \
    build-essential \
    libxcb-cursor0 \ 
    && rm -rf /var/lib/apt/lists/*

WORKDIR /user/resource-planner

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src/

CMD ["python3", "src/main.py"]

