%global pypi_name vitrageclient

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:             python-%{pypi_name}
Version:          XXX
Release:          XXX
Summary:          Python API and CLI for OpenStack Vitrage

License:          ASL 2.0
URL:              http://pypi.python.org/pypi/%{name}
Source0:          http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-pbr

Requires:         python-babel >= 1.3
Requires:         python-cliff >= 1.14.0
Requires:         python-oslo-i18n >= 1.5.0
Requires:         python-oslo-serialization >= 1.4.0
Requires:         python-oslo-utils >= 2.0.0
Requires:         python-keystoneauth1 >= 1.0.0
Requires:         python-six >= 1.9.0
Requires:         python-futurist


%description
This is a client library for Vitrage built on the Vitrage API. It
provides a Python API (the vitrageclient module) and a command-line tool.


%package doc
Summary:          Documentation for OpenStack Vitrage API Client
Group:            Documentation

BuildRequires:    python-sphinx
BuildRequires:    python-oslo-sphinx

%description      doc
This is a client library for Vitrage built on the Vitrage API. It
provides a Python API (the vitrageclient module) and a command-line tool
(vitrage).

This package contains auto-generated documentation.


%prep
%setup -q -n %{pypi_name}-%{upstream_version}

# Remove bundled egg-info
rm -rf vitrageclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo

%files
%doc README.rst
%license LICENSE
%{_bindir}/vitrage
%{python2_sitelib}/vitrageclient
%{python2_sitelib}/*.egg-info
/usr/share/vitrage.bash_completion

%files doc
%doc html

%changelog
