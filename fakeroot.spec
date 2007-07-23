Summary:	Gives a fake root environment
Name:		fakeroot
Version:	1.5.9
Release:	%mkrel 2
License:	GPL
Group:		Development/Other
URL:		ftp://ftp.debian.org/debian/pool/main/f/fakeroot/
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/fakeroot_%{version}.tar.bz2
BuildRequires:	libstdc++-devel
BuildRequires:	po4a
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This package is intended to enable something like: fakeroot rpm
--rebuild i.e. to remove the need to become root for a package
build. This is done by setting LD_PRELOAD to a "libfakeroot.so.0.0",
that provides wrappers around chown, chmod, mknod, stat, etc.

If you don't understand any of this, you do not need this!

%prep

%setup -q

# anti version hack
perl -pi -e "s|-release 0|-avoid-version|g" Makefile*

%build
%define __libtoolize /bin/true

%configure2_5x \
    --enable-static=no

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# the french man page is in man-pages-fr-1.58.0-18mdk, nuke this one to prevent file clash
rm -rf %{buildroot}%{_mandir}/fr/man*

# cleanuo
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc DEBUG AUTHORS README.fake BUGS debian/changelog
%{_bindir}/*
%{_libdir}/libfakeroot.so
%{_mandir}/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(sv) %{_mandir}/sv/man*/*
