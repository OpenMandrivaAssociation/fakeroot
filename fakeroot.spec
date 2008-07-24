Summary:	Gives a fake root environment
Name:		fakeroot
Version:	1.9.2
Release:	%mkrel 3
License:	GPL
Group:		Development/Other
URL:		ftp://ftp.debian.org/debian/pool/main/f/fakeroot/
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/fakeroot_%{version}.tar.gz
BuildRequires:	libstdc++-devel
BuildRequires:  sharutils
BuildRequires:  util-linux-ng
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
for file in ./doc/*/*.1; do
  %{_bindir}/iconv -f latin1 -t utf8 < $file > $file.new
  %{__mv} -f $file.new $file
done

# anti version hack
%{__perl} -pi -e "s|-release 0|-avoid-version|g" Makefile*

%build

%configure2_5x \
    --disable-dependency-tracking \
    --disable-static \
    --libdir=%{_libdir}/libfakeroot \
    --with-ipc=tcp
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std} libdir=%{_libdir}/libfakeroot

%{__rm} %{buildroot}%{_libdir}/libfakeroot/*.la

# the french man page is in man-pages-fr-1.58.0-18mdk, nuke this one to prevent file clash
%{__rm} -r %{buildroot}%{_mandir}/fr/man*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc AUTHORS BUGS COPYING ChangeLog DEBUG INSTALL NEWS README debian/changelog
%{_bindir}/*
%{_libdir}/libfakeroot
%{_mandir}/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(nl) %{_mandir}/nl/man*/*
%lang(sv) %{_mandir}/sv/man*/*
