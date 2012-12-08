Summary:	Gives a fake root environment
Name:		fakeroot
Version:	1.14.4
Release:	%mkrel 3
License:	GPL
Group:		Development/Other
URL:		http://fakechroot.alioth.debian.org/
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/fakeroot_%{version}.tar.bz2
BuildRequires:	libstdc++-devel
BuildRequires:  sharutils
BuildRequires:  util-linux-ng
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
%doc AUTHORS BUGS COPYING ChangeLog DEBUG INSTALL NEWS README 
%{_bindir}/*
%{_libdir}/libfakeroot
%{_mandir}/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(nl) %{_mandir}/nl/man*/*
%lang(sv) %{_mandir}/sv/man*/*


%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 1.14.4-2mdv2011.0
+ Revision: 672343
- po4a not nteeded

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Wed Oct 13 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.14.4-1mdv2011.0
+ Revision: 585379
- update to 1.14.4
- use right archive
- fix file list

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1.14.3-1mdv2010.1
+ Revision: 462322
- update to new version 1.14.3

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.11.4-3mdv2010.0
+ Revision: 437523
- rebuild

* Sat Feb 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.4-2mdv2009.1
+ Revision: 345997
- rebuild

* Sat Dec 20 2008 Funda Wang <fwang@mandriva.org> 1.11.4-1mdv2009.1
+ Revision: 316519
- New version 1.11.4

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.9.2-3mdv2009.0
+ Revision: 245045
- rebuild

* Tue Feb 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.9.2-1mdv2008.1
+ Revision: 162573
- 1.9.2
- use TCP instead of SysV IPC

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 David Walluck <walluck@mandriva.org> 1.8.2-1mdv2008.1
+ Revision: 98433
- 1.8.2
- 1.6.4
- move libdir to %%{_libdir}/libfakeroot to match Debian and Fedora

* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.9-2mdv2008.0
+ Revision: 54683
- Import fakeroot



* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.9-2mdv2008.0
- nuke libifiction (fixes #26724)

* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5.9-1mdv2007.0
- 1.5.9

* Thu Jun 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.9-3mdk
- fix #16454

* Wed Jun 08 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.9-2mdk
- fix deps (Olivier Thauvin)

* Fri Apr 08 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.9-1mdk
- initial package, PLD import
