Summary:	Gives a fake root environment
Name:		fakeroot
Version:	1.30.1
Release:	1
License:	GPLv2
Group:		Development/Other
Url:		http://fakeroot.alioth.debian.org/
Source0:	http://http.debian.net/debian/pool/main/f/fakeroot/%{name}_%{version}.orig.tar.gz
# Debian package patches, from debian.tar.xz
#Patch0: debian_eglibc-fts-without-LFS.patch
Patch1: debian_glibc-xattr-types.patch
Patch2: debian_fix-shell-in-fakeroot.patch
#Patch3: debian_hide-dlsym-error.patch
# Address some POSIX-types related problems.
Patch4: fakeroot-inttypes.patch
# Fix LD_LIBRARY_PATH for multilib: https://bugzilla.redhat.com/show_bug.cgi?id=1241527
#Patch5: fakeroot-multilib.patch
# skip t.tar test for now: https://bugzilla.redhat.com/show_bug.cgi?id=1601392
Patch6: fakeroot-tests.patch

BuildRequires:	libstdc++-devel
BuildRequires:  sharutils
BuildRequires:  util-linux
BuildRequires:  pkgconfig(libcap)

%description
This package is intended to enable something like: fakeroot rpm
--rebuild i.e. to remove the need to become root for a package
build. This is done by setting LD_PRELOAD to a "libfakeroot.so.0.0",
that provides wrappers around chown, chmod, mknod, stat, etc.

If you don't understand any of this, you do not need this!

%prep
%autosetup -p1
for file in ./doc/*/*.1; do
	%{_bindir}/iconv -f latin1 -t utf8 < $file > $file.new
	mv -f $file.new $file
done

# anti version hack
sed -i -e "s|-release 0|-avoid-version|g" Makefile*

%build
%configure \
	--libdir=%{_libdir}/libfakeroot \
	--with-ipc=tcp
%make_build

%install
%make_install libdir=%{_libdir}/libfakeroot

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
%lang(pt) %{_mandir}/pt/man*/*
%lang(sv) %{_mandir}/sv/man*/*
