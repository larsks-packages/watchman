Name:           watchman
Version:        4.9.0
Release:        1%{?dist}
Summary:        A file watching service

License:        ASL 2.0
URL:            https://facebook.github.io/watchman/
Source0:        https://github.com/facebook/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        watchman-tmpfiles.conf

BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  systemd

%description
Watchman exists to watch files and record when they change. It can also trigger
actions (such as rebuilding assets) when matching files change.

%package python3
Summary: Python bindings for Watchman, a file monitoring service

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description python3
Watchman exists to watch files and record when they change. It can also trigger
actions (such as rebuilding assets) when matching files change.

This package provides Python bindings for Watchman.

%prep
%autosetup -S git

./autogen.sh


%build
%configure \
	--with-python=%{_bindir}/python3 \
    --enable-statedir=/run/%{name}
make %{?_smp_mflags} \
    CXXFLAGS="-Wno-error=format-truncation -fPIC"


%install
%make_install
install -m 755 -d %{buildroot}%{_tmpfilesdir}
install -m 644 %{S:1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

rm -rf %{buildroot}%{_docdir}/%{name}-%{version}


%files
%doc README.markdown
%license LICENSE
%{_bindir}/watchman
%{_bindir}/watchman-make
%{_bindir}/watchman-wait
%{_tmpfilesdir}/watchman.conf
/run/%{name}


%files python3
%{python3_sitearch}/pywatchman-1.4.0-py%{python3_version}.egg-info/
%{python3_sitearch}/pywatchman/


%changelog
* Fri Apr 06 2018 Lars Kellogg-Stedman <lars@oddbit.com> - 4.9.0-1
- submit package for review
