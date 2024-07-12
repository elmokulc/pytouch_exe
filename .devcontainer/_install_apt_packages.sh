# BASIC LIBRARIES
apt-get update && \
    apt-get install -y git wget sudo cmake libncurses5-dev libncursesw5-dev build-essential ffmpeg libsm6 libxext6 libv4l-dev htop && \
    apt-get install -y libxcursor-dev libxcomposite-dev libxdamage-dev libxrandr-dev libxtst-dev libxss-dev libdbus-1-dev libevent-dev libfontconfig1-dev libcap-dev libpulse-dev libudev-dev libpci-dev libnss3-dev libasound2-dev libegl1-mesa-dev gperf bison nodejs x11-apps xauth libxcb-xinerama0-dev libxcb-icccm4-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-render-util0-dev libxcb-xkb-dev libxkbcommon-x11-0 libx11-dev libgles2-mesa-dev mesa-utils-extra && \
    apt-get clean


# ARAVIS INSTALL
echo "** Preparing Machine"
apt-get install -y autoconf intltool libxml2-dev libgtk-3-dev libnotify-dev gtk-doc-tools libgtk2.0-dev pkg-config
apt-get install -y gstreamer1.0-nice gstreamer1.0-tools
apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-0 libgstreamer-plugins-good1.0-0 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
apt-get install -y gobject-introspection libgirepository1.0-dev python-gobject
apt-get install -y libusb-1.0 libusb-1.0.0-dev usbutils apt-utils
apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
