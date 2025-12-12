%global srcname parameterized

Name:           python-%{srcname}
Version:        0.8.1
Release:        3
Summary:        Parameterized testing with any Python test framework
Group:		Development/Python

License:        BSD
URL:            https://pypi.python.org/pypi/parameterized
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz

# Python 3.8
#Patch0:         https://github.com/wolever/parameterized/pull/75/commits/1842e2038ae123e16601e083a553fe931f34fbd0.patch

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose

%description
%{summary}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE.txt
%doc CHANGELOG.txt README.rst
%{python_sitelib}/%{srcname}-*.egg-info/
%{python_sitelib}/%{srcname}/
