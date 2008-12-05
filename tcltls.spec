Summary: 	SSL2, SSL3, and TLS1 encryption extensions for TCL
Name: 		tcltls
Version: 	1.6
Release: 	%{mkrel 1}
License: 	BSD
Group: 		System/Libraries
URL: 		http://tls.sourceforge.net/
Source0:	http://downloads.sourceforge.net/tls/tls%{version}-src.tar.gz
Patch0:		tcltls-1.6-simpleclient.patch
Patch1:		tcltls-1.6-openssl.patch
Patch2:		tcltls-1.6-no-rpath.patch
BuildRequires:	tcl-devel
BuildRequires:	openssl-devel
Requires:	tcl >= 8.4.11
Requires:	openssl
Obsoletes:	%{mklibname tcltls 1.50}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%build
autoreconf
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
%makeinstall_std libdir=%{tcl_sitearch} includedir=%{_includedir}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README.txt license.terms tls.htm
%{tcl_sitearch}/tls%{version}

%files devel
%defattr(-,root,root)
%{_includedir}/tls.h


