Name:           mraa
Version:        0.5.4
Release:        0
License:        MIT
Summary:        Low Level Skeleton Library for Communication
Url:            https://github.com/intel-iot-devkit/mraa
# X-Vc-Url:     https://github.com/intel-iot-devkit/mraa
Group:          Contrib
Source:         %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fdupes

%description
C/C++ library with bindings to javascript & python to interface
with the IO on Galileo, Edison & other platforms, with a structured and sane
API where port names/numbering matches the board that you are on.


%package devel
Summary:    Low Level Skeleton Library for Communication -- developer files
Group:      Contrib
Requires:   %{name} = %{version}-%{release}

%description devel
C/C++ library with bindings to javascript & python to interface
with the IO on Galileo, Edison & other platforms, with a structured and sane
API where port names/numbering matches the board that you are on.
Developer files.


%prep
%setup -q


%build

%cmake . \
 -DCMAKE_INSTALL_PREFIX:PATH=/usr

%__make %{?_smp_mflags}


%install
%make_install
%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}.h*
%{_includedir}/%{name}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%exclude %{_datadir}/%{name}/examples/