Name:           ros-jade-cl-tf2
Version:        0.2.7
Release:        0%{?dist}
Summary:        ROS cl_tf2 package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib-lisp
Requires:       ros-jade-cl-transforms-stamped
Requires:       ros-jade-cl-utils
Requires:       ros-jade-roslisp
Requires:       ros-jade-tf2-msgs
Requires:       sbcl
BuildRequires:  ros-jade-actionlib-lisp
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cl-transforms-stamped
BuildRequires:  ros-jade-cl-utils
BuildRequires:  ros-jade-roslisp
BuildRequires:  ros-jade-tf2-msgs
BuildRequires:  sbcl

%description
Client implementation to use TF2 from Common Lisp

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Apr 19 2016 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.2.7-0
- Autogenerated by Bloom

* Thu Apr 14 2016 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.2.6-0
- Autogenerated by Bloom

