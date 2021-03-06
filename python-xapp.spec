%global sum Python bindings for xapps

Name:           python-xapp
Version:	2.0.1
Release:	1
Summary:        %{sum}

License:        GPLv2
URL:            https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/python-xapp/archive/%{version}/%{name}-%{version}.tar.gz
Group:          Development/Python

BuildArch:      noarch

BuildRequires: pkgconfig(python3)
BuildRequires: python3egg(setuptools)

Requires:      python3dist(psutil)


%description
%{sum}.

%package -n python2-xapp
Summary:       %{sum}
BuildRequires: pkgconfig(python)
BuildRequires: python2dist(setuptools)
Requires:      python2dist(psutil)

%description -n python2-xapp
%{sum}.

%prep
%autosetup -n python3-xapp-%{version}
%autopatch -p1
sed -i -e 's!1.0.0!%{version}!g' setup.py

%build
python2 setup.py build
python3 setup.py build

%install
python2 setup.py install --root=%{buildroot}
python3 setup.py install --root=%{buildroot}

%files -n python2-xapp
%doc COPYING README TODO AUTHORS
%{python2_sitelib}/xapp/
%{python2_sitelib}/python_xapp-%{version}-py%{python2_version}.egg-info

%files
%doc COPYING README TODO AUTHORS
%{python3_sitelib}/xapp/
%{python3_sitelib}/python_xapp-%{version}-py%{python3_version}.egg-info
