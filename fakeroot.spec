Summary:	Gives a fake root environment
Name:		fakeroot
Version:	1.18.4
Release:	2
License:	GPLv2
Group:		Development/Other
Url:		http://fakechroot.alioth.debian.org/
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/fakeroot_%{version}.orig.tar.bz2
BuildRequires:	libstdc++-devel
BuildRequires:  sharutils
BuildRequires:  util-linux-ng

%description
This package is intended to enable something like: fakeroot rpm
--rebuild i.e. to remove the need to become root for a package
build. This is done by setting LD_PRELOAD to a "libfakeroot.so.0.0",
that provides wrappers around chown, chmod, mknod, stat, etc.

If you don't understand any of this, you do not need this!

%prep
%setup -q
for file in ./doc/*/*.1; do
	%{_bindir}/iconv -f latin1 -t utf8 < $file > $file.new
	mv -f $file.new $file
done

# anti version hack
sed -i -e "s|-release 0|-avoid-version|g" Makefile*

%build
%configure2_5x \
	--disable-static \
	--libdir=%{_libdir}/libfakeroot \
	--with-ipc=tcp
%make

%install
%makeinstall_std libdir=%{_libdir}/libfakeroot

# the french man page is in man-pages-fr-1.58.0-18mdk, nuke this one to prevent file clash
rm -r %{buildroot}%{_mandir}/fr/man*

%files
%doc AUTHORS BUGS COPYING DEBUG README 
%{_bindir}/*
%{_libdir}/libfakeroot
%{_mandir}/man*/*
%lang(de) %{_mandir}/de/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(nl) %{_mandir}/nl/man*/*
%lang(sv) %{_mandir}/sv/man*/*

