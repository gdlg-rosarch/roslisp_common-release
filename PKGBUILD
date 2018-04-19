# Script generated with Bloom
pkgdesc="ROS - Common libraries to control ROS based robots. This stack contains an implementation of actionlib (client and server) in Common Lisp, a transformation library and an implementation of tf in Common Lisp."
url='http://ros.org/wiki/roslisp_common'

pkgname='ros-kinetic-roslisp-common'
pkgver='0.2.10_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-actionlib-lisp'
'ros-kinetic-cl-tf'
'ros-kinetic-cl-tf2'
'ros-kinetic-cl-transforms'
'ros-kinetic-cl-transforms-stamped'
'ros-kinetic-cl-urdf'
'ros-kinetic-cl-utils'
'ros-kinetic-roslisp-utilities'
)

conflicts=()
replaces=()

_dir=roslisp_common
source=()
md5sums=()

prepare() {
    cp -R $startdir/roslisp_common $srcdir/roslisp_common
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

