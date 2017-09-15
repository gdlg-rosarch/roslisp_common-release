Name:           ros-indigo-cl-tf2
Version:        0.2.10
Release:        0%{?dist}
Summary:        ROS cl_tf2 package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib-lisp
Requires:       ros-indigo-cl-transforms-stamped
Requires:       ros-indigo-cl-utils
Requires:       ros-indigo-roslisp
Requires:       ros-indigo-tf2-msgs
BuildRequires:  ros-indigo-catkin

%description
Client implementation to use TF2 from Common Lisp

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
* Fri Sep 15 2017 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.2.10-0
- Autogenerated by Bloom

* Wed Jun 21 2017 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.2.9-0
- Autogenerated by Bloom

* Thu Apr 21 2016 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.2.8-1
- Autogenerated by Bloom

* Thu Apr 21 2016 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.2.8-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.2.7-0
- Autogenerated by Bloom

* Thu Apr 14 2016 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.2.6-0
- Autogenerated by Bloom

* Mon Dec 01 2014 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.2.3-0
- Autogenerated by Bloom

