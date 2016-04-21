Name:           ros-indigo-roslisp-common
Version:        0.2.8
Release:        0%{?dist}
Summary:        ROS roslisp_common package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roslisp_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-actionlib-lisp
Requires:       ros-indigo-cl-tf
Requires:       ros-indigo-cl-tf2
Requires:       ros-indigo-cl-transforms
Requires:       ros-indigo-cl-transforms-stamped
Requires:       ros-indigo-cl-urdf
Requires:       ros-indigo-cl-utils
Requires:       ros-indigo-roslisp-utilities
BuildRequires:  ros-indigo-catkin

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
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Apr 21 2016 Lorenz Moesenlechner <moesenle@cs.tum.edu> - 0.2.8-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Lorenz Moesenlechner <moesenle@cs.tum.edu> - 0.2.7-0
- Autogenerated by Bloom

* Thu Apr 14 2016 Lorenz Moesenlechner <moesenle@cs.tum.edu> - 0.2.6-0
- Autogenerated by Bloom

* Mon Dec 01 2014 Lorenz Moesenlechner <moesenle@cs.tum.edu> - 0.2.3-0
- Autogenerated by Bloom

