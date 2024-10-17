#define debug_package %{nil}

Summary: 	SSL2, SSL3, and TLS1 encryption extensions for TCL
Name: 		tcltls
Version: 	1.6
Release: 	4
License: 	BSD
Group: 		System/Libraries
URL: 		https://tls.sourceforge.net/
Source0:		http://downloads.sourceforge.net/tls/tls%{version}-src.tar.gz
Patch0:		tcltls-1.6-simpleclient.patch
Patch1:		tcltls-1.6-openssl.patch
Patch2:		tcltls-1.6-no-rpath.patch
Patch3:		tcltls-1.6-ciphers.patch
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(openssl)
Requires:	tcl >= 8.4.11
Requires:	openssl
Obsoletes:	%{mklibname tcltls 1.50}

%description 
Provides SSL2, SSL3, and TLS1 socket encryption functionality
to the TCL interpreted language.
Needed for Sguild

%package	devel
Summary:	SSL2, SSL3, and TLS1 encryption extensions for TCL
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{mklibname tcltls 1.50 -d}

%description	devel
Provides SSL2, SSL3, and TLS1 socket encryption functionality
to the TCL interpreted language. Development headers.

%prep
%setup -q -n tls%{version}
%patch0 -p1 -b .simpleclient
%patch1 -p1 -b .openssl098a
%patch2 -p1 -b .rpath
%patch3 -p0

%build

#autoreconf
%configure2_5x \
    --enable-shared \
    --with-gcclib \
    --with-ssl-dir=%{_prefix} \
    --with-tcl=%{_libdir}
    
%make 

%check
make test

%install
%makeinstall_std libdir=%{tcl_sitearch} includedir=%{_includedir}


%files
%doc ChangeLog README.txt license.terms tls.htm
%{tcl_sitearch}/tls%{version}

%files devel
%{_includedir}/tls.h




%changelog
* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 1.6-3mdv2010.1
+ Revision: 533637
- rebuild

* Sun Feb 21 2010 Funda Wang <fwang@mandriva.org> 1.6-2mdv2010.1
+ Revision: 509185
- clean spec
- rediff openssl patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 05 2008 Adam Williamson <awilliamson@mandriva.org> 1.6-1mdv2009.1
+ Revision: 310130
- move to new location per policy
- sync patches with fedora
- dump the whole libification, tcl modules are not shared libraries
- new release 1.6

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-6mdv2009.0
+ Revision: 261432
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-5mdv2009.0
+ Revision: 254233
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.5.0-3mdv2008.1
+ Revision: 140918
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jun 12 2007 Adam Williamson <awilliamson@mandriva.org> 1.5.0-3mdv2008.0
+ Revision: 38329
- correct pkgIndex.tcl (fixes amsn with TCL 8.5)


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-2mdv2007.0
+ Revision: 113894
- Import tcltls

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-2mdv2007.1
- rebuild

* Fri Dec 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-1mdk
- initial Mandriva package
- added P0 from debian

* Sat Nov 26 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 
- First release

