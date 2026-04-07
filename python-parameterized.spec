%define module parameterized

Name:		python-parameterized
Version:	0.9.0
Release:	1
Summary:	Parameterized testing with any Python test framework
Group:		Development/Python
License:	BSD-2-Clause
URL:		https://github.com/wolever/parameterized
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Parameterized testing with any Python test framework.

%files
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
