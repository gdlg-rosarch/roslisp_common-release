Name:           ros-kinetic-roslisp-common
Version:        0.2.6
Release:        1%{?dist}
Summary:        ROS roslisp_common package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roslisp_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-actionlib-lisp
Requires:       ros-kinetic-cl-tf
Requires:       ros-kinetic-cl-tf2
Requires:       ros-kinetic-cl-transforms
Requires:       ros-kinetic-cl-transforms-stamped
Requires:       ros-kinetic-cl-urdf
Requires:       ros-kinetic-cl-utils
Requires:       ros-kinetic-roslisp-utilities
BuildRequires:  ros-kinetic-catkin

%description
Common libraries to control ROS based robots. This stack contains an
implementation of actionlib (client and server) in Common Lisp, a transformation
library and an implementation of tf in Common Lisp.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 14 2016 Lorenz Moesenlechner <moesenle@cs.tum.edu> - 0.2.6-1
- Autogenerated by Bloom

* Thu Apr 14 2016 Lorenz Moesenlechner <moesenle@cs.tum.edu> - 0.2.6-0
- Autogenerated by Bloom

