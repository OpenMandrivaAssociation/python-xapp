%global sum Python bindings for xapps

Name:		python-xapp
Version:	3.0.2
Release:	1
Summary:	%{sum}
License:	GPLv2
Group:		Development/Python
URL:		https://github.com/linuxmint/python-xapp
Source0:	https://github.com/linuxmint/python3-xapp/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	meson
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:		python%{pyver}dist(psutil)

%description
%{sum}.

%install -a
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{python_sitelib}/xapp/
