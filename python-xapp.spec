%global sum Python bindings for xapps

Name:		python-xapp
Version:	3.0.1
Release:	1
Summary:	%{sum}
License:	GPLv2
Group:		Development/Python
URL:		https://github.com/linuxmint/%{name}
Source0:	https://github.com/linuxmint/python3-xapp/archive/%{version}/python3-xapp-%{version}.tar.gz
BuildArch:	noarch

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

%prep
%autosetup -n python3-xapp-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc README
%license COPYING
%{python_sitelib}/xapp/
