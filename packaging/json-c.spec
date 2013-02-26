Name:           json-c
Version:        0.10
Release:        0
License:        MIT
Summary:        JSON implementation in C
Url:            http://oss.metaparadigm.com/%{name}
Group:          System/Libraries
Source0:        http://oss.metaparadigm.com/json-c/json-c-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C
representation of JSON objects.

%package -n libjson
Summary:        JSON shared lib
Group:          System/Libraries

%description -n libjson
This package includes the JSON library.

%package -n libjson-devel
Summary:        Development headers and libraries for json-c
Group:          Development/Libraries
Requires:       libjson = %{version}

%description -n libjson-devel
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

%post -n libjson -p /sbin/ldconfig

%postun -n libjson -p /sbin/ldconfig

%files -n libjson
%defattr(-,root,root)
%license COPYING
%{_libdir}/libjson.so.*

%files -n libjson-devel
%defattr(-,root,root)
%{_libdir}/libjson.so
%{_includedir}/json
%{_libdir}/pkgconfig/*.pc

%changelog
