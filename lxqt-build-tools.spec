#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE793007AD22DF7E (tsujan2000@gmail.com)
#
Name     : lxqt-build-tools
Version  : 0.12.0
Release  : 10
URL      : https://github.com/lxqt/lxqt-build-tools/releases/download/0.12.0/lxqt-build-tools-0.12.0.tar.xz
Source0  : https://github.com/lxqt/lxqt-build-tools/releases/download/0.12.0/lxqt-build-tools-0.12.0.tar.xz
Source1  : https://github.com/lxqt/lxqt-build-tools/releases/download/0.12.0/lxqt-build-tools-0.12.0.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: lxqt-build-tools-bin = %{version}-%{release}
Requires: lxqt-build-tools-data = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libexif)
BuildRequires : pkgconfig(libmenu-cache)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(xcb)
BuildRequires : qtbase-dev

%description
# lxqt-build-tools
## Introduction
This repository is providing several tools needed to build LXQt itself as well
as other components maintained by the LXQt project.

%package bin
Summary: bin components for the lxqt-build-tools package.
Group: Binaries
Requires: lxqt-build-tools-data = %{version}-%{release}

%description bin
bin components for the lxqt-build-tools package.


%package data
Summary: data components for the lxqt-build-tools package.
Group: Data

%description data
data components for the lxqt-build-tools package.


%prep
%setup -q -n lxqt-build-tools-0.12.0
cd %{_builddir}/lxqt-build-tools-0.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667835378
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1667835378
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-transupdate

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*
