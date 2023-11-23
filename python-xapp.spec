%global sum Python bindings for xapps

Name:           python-xapp
Version:	2.4.1
Release:	2
Summary:        %{sum}

License:        GPLv2
URL:            https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/python3-xapp/archive/%{version}/python3-xapp-%{version}.tar.gz
Group:          Development/Python

BuildArch:      noarch
BuildRequires: meson
BuildRequires: pkgconfig(python3)
BuildRequires: python3egg(setuptools)

Requires:      python3dist(psutil)


%description
%{sum}.

%prep
%autosetup -n python3-xapp-%{version}
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install


%files
%doc COPYING README TODO AUTHORS
%{python3_sitelib}/xapp/
