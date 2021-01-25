# Created by pyp2rpm-3.3.1
%global pypi_name backcall

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        1
Summary:        Specifications for callback functions passed in to an API
Group:          Development/Python
License:        BSD
URL:            https://github.com/takluyver/backcall
Source0:        https://files.pythonhosted.org/packages/a2/40/764a663805d84deee23043e1426a9175567db89c8b3287b5c2ad9f71aa93/backcall-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
backcallSpecifications for callback functions passed in to an APIIf your code
lets other people supply callback functions, it's important to specify the
function signature you expect, and check that functions support that. Adding
extra parameters later would break other peoples code unless you're
careful.backcall provides a way of specifying the callback signature using a
prototype function::...

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py_build

%install
%py_install


%files
%doc README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
