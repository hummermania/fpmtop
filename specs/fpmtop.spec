Name: fpmtop		
Version:	0.0.1
Release:	1%{?dist}
Summary:	fpmtop - is a tool to explore php-fpm workers internal info

Group:		DevTools
License:	GPLv2
URL:		https://github.com/hummermania/fpmtop.git
Source0:    %{name}-%{version}.tar.gz	

BuildRequires:	ncurses-devel, libcurl-devel, pugixml-devel, openssl-devel, cmake, make


%description
fpmtop - is a tool to explore php-fpm workers internal information: request, worker metrics etc.


%prep
echo TARGET is %{name}-%{version}
%setup -q -c


%build
rm -rf build
mkdir build
cd build
%cmake ..
make %{?_smp_mflags} CFLAGS="-std=c++11 -pthread" 

%install
echo RPM_BUILD_ROOT=$RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT


%files
fpmtop
%doc



%changelog

