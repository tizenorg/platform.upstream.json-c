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
Patch0:         %{name}-0.9-base.patch
Patch1:         %{name}-0.9-json_object_from_file.patch
Patch2:         %{name}-0.9-json_tokener.patch
Patch3:         %{name}-0.9-linkhash.patch
Patch4:         jsonc-lfs.patch
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoreconf -fiv
%configure --disable-static --with-pic
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check
rm -rf %{buildroot}%{_libdir}/*.la

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
