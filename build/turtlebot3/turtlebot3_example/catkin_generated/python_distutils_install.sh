#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/guilherme/turtlebot-gazebo/src/turtlebot3/turtlebot3_example"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/guilherme/turtlebot-gazebo/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/guilherme/turtlebot-gazebo/install/lib/python3/dist-packages:/home/guilherme/turtlebot-gazebo/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/guilherme/turtlebot-gazebo/build" \
    "/usr/bin/python3" \
    "/home/guilherme/turtlebot-gazebo/src/turtlebot3/turtlebot3_example/setup.py" \
     \
    build --build-base "/home/guilherme/turtlebot-gazebo/build/turtlebot3/turtlebot3_example" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/guilherme/turtlebot-gazebo/install" --install-scripts="/home/guilherme/turtlebot-gazebo/install/bin"
