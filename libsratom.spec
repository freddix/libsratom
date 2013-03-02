Summary:	Library for serialising LV2 atoms to/from RDF
Name:		libsratom
Version:	0.4.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.drobilla.net/sratom-%{version}.tar.bz2
# Source0-md5:	5bb7e4bc4198e19f388ac51239007f25
BuildRequires:	libserd-devel >= 0.18.0
BuildRequires:	libsord-devel >= 0.12.0
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sratom is a library for serialising LV2 atoms to/from RDF,
particularly the Turtle syntax.

%package devel
Summary:	Header files for sratom library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for sratom library.

%prep
%setup -qn sratom-%{version}

sed -i "s|bld.add_post_fun(autowaf.run_ldconfig)||" wscript

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./waf configure \
	--prefix=%{_prefix}	\
	--mandir=%{_mandir}	\
	--libdir=%{_libdir}	\
	--nocache
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install	\
	--destdir=$RPM_BUILD_ROOT

chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %ghost %{_libdir}/libsratom-0.so.?
%attr(755,root,root) %{_libdir}/libsratom-0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsratom-0.so
%{_includedir}/sratom-0
%{_pkgconfigdir}/sratom-0.pc

