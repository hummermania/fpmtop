%{?scl:%scl package fpmtop}
Name: %{?scl prefix}fpmtop		
Version:	0.0.1
Release:	1%{?dist}
Summary:	fpmtop - is a tool to explore php-fpm workers internal info

Group:		DevTools
License:	GPLv2
URL:		https://github.com/hummermania/fpmtop.git
Source0:    %{name}-%{version}.tar.gz	

BuildRequires:	ncurses-devel, libcurl-devel, pugixml-devel, openssl-devel, cmake, make
%{?scl:Requires: %scl runtime}
#Requires:	

%description
fpmtop - is a tool to explore php-fpm workers internal information: request, worker metrics etc.


%prep
SCRIPT=$(readlink -f $0)
SCRIPTPATH=`dirname $SCRIPT`
cd $SCRIPTPATH
mkdir build
cd build
%setup -q %{?scl:-n %{pkg name}-%{version}}


%build
%cmake ..
make %{?_smp_mflags} CFLAGS="-std=c++11 -pthread" BINDIR=%{_bindir}

%install
%make_install


%files
%doc



%changelog

