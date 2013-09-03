Summary: X.Org X11 applications
Name: xeyes
# NOTE: The package version should be set to the X11 major release from which
# the OS release is based upon.
Version: 1.1.1
Release: 1
License: MIT
Group: User Interface/X
URL: http://www.x.org

Source: %{name}-%{version}.tar.gz

#Source11: ftp://ftp.x.org/pub/individual/app/xeyes-1.1.1.tar.bz2

BuildRequires: autoconf automake

#BuildRequires: xorg-x11-xutils-dev
# xfd needs gettext
BuildRequires: gettext
BuildRequires: zlib-devel
BuildRequires: libfontenc-devel
BuildRequires: libX11-devel
BuildRequires: libXmu-devel
BuildRequires: libXext-devel
BuildRequires: libXt-devel
BuildRequires: libXaw-devel
BuildRequires: libXpm-devel
BuildRequires: libXft-devel
BuildRequires: libXrender-devel
BuildRequires: libxkbfile-devel
BuildRequires: libXcursor-devel
BuildRequires: libpng-devel
BuildRequires: libXfixes-devel
BuildRequires: libXi-devel >= 1.2
BuildRequires: libXxf86vm-devel
#BuildRequires: xorg-x11-xbitmaps

Provides: xeyes

%description
A collection of common X Window System applications.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}

{
	make install DESTDIR=$RPM_BUILD_ROOT
}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
/usr/share/license/%{name}
