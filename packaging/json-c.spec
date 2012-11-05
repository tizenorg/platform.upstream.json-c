%define libname libjson
%define libsoname %{libname}

Name:           json-c
Version:        0.9
Release:        0
License:        MIT
Summary:        JSON implementation in C
Url:            http://oss.metaparadigm.com/%{name}
Group:          System/Libraries
Source0:        http://oss.metaparadigm.com/json-c/json-c-0.9.tar.gz
Source1:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

%package -n %{libsoname}
Summary:        JSON shared lib
Group:          System/Libraries

%description -n %{libsoname}
This package includes the JSON library.

%package -n %{libname}-devel
Summary:        Development headers and libraries for json-c
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}

%description -n %{libname}-devel
This package includes header files and scripts needed for developers
using the json-c library

%prep
%setup -q

%build
autoreconf -fiv
%configure --disable-static --with-pic
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install

%post -n %{libsoname} -p /sbin/ldconfig

%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%defattr(-,root,root)
%{_libdir}/%{libname}.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/%{libname}.so
%{_includedir}/json
%{_libdir}/pkgconfig/*.pc

%changelog
