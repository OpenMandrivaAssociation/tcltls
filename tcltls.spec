%define name tcltls
%define version 1.5.0
%define release %mkrel 3
%define major 1.50
%define libname %mklibname tcltls %{major}

Summary: 	SSL2, SSL3, and TLS1 encryption extensions for TCL
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		System/Libraries
URL: 		http://tls.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/tls/tls%{version}-src.tar.bz2
Patch0:		tcltls_1.5.0-2.diff
Patch1:		amsn-0.95-tls1.5-1.5.0-engine.diff
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	tcl
BuildRequires:	tcl-devel
BuildRequires:	openssl-devel
Requires:	tcl >= 8.4.11
Requires:	openssl

%description 
Provides SSL2, SSL3, and TLS1 socket encryption functionality
to the TCL interpreted language.
Needed for Sguild

%package -n	%{libname}
Summary:	SSL2, SSL3, and TLS1 encryption extensions for TCL
Group:		System/Libraries
Requires:	tcl >= 8.4.11
Requires:	openssl

%description -n	%{libname}
Provides SSL2, SSL3, and TLS1 socket encryption functionality
to the TCL interpreted language.
Needed for Sguild

%package -n	%{libname}-devel
Summary:	SSL2, SSL3, and TLS1 encryption extensions for TCL
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel %{name}-devel
Obsoletes:	lib%{name}-devel %{name}-devel

%description -n	%{libname}-devel
Provides SSL2, SSL3, and TLS1 socket encryption functionality
to the TCL interpreted language.
Needed for Sguild

%prep

%setup -q -n tls1.5
%patch0 -p1
%patch1 -p1 -b .openssl098a

%build

# Fixes AMSN with TCL/TK 8.5: from http://www.amsn-project.net/wiki/FAQ
# AdamW 2007/06
perl -pi -e 's,1.5,1.50,g' pkgIndex.tcl.in

%configure2_5x \
    --enable-shared \
    --enable-static \
    --enable-gcc \
    --with-gcclib \
    --with-ssl-dir=%{_prefix} \
    --with-tcl=%{_libdir}

%make

make test

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/tls%{major}
install -d %{buildroot}%{_includedir}/tls%{major}

install -m0755 libtls%{major}.so %{buildroot}%{_libdir}/tls%{major}/
ln -snf libtls%{major}.so %{buildroot}%{_libdir}/tls%{major}/libtls.so.0

install -m0644 tls.h %{buildroot}%{_includedir}/tls%{major}/
install -m0644 pkgIndex.tcl %{buildroot}%{_libdir}/tls%{major}/
install -m0644 tls.tcl %{buildroot}%{_libdir}/tls%{major}/

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog README.txt license.terms tls.htm
%dir %{_libdir}/tls%{major}
%{_libdir}/tls%{major}/*tcl
%{_libdir}/tls%{major}/lib*.so.*
%{_libdir}/tls%{major}/lib*.so

%files -n %{libname}-devel
%defattr(-,root,root)
%dir %{_includedir}/tls%{major}
%{_includedir}/tls%{major}/*


