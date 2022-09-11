#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	unittest subTest() support and subtests fixture
Summary(pl.UTF-8):	Obsługa subTest() i wyposażenie subtests dla szkieletu unittest
Name:		python3-pytest-subtests
# note: 0.7+ require pytest 7
Version:	0.6.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-subtests/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-subtests/pytest-subtests-%{version}.tar.gz
# Source0-md5:	5feacd1c1316a03968a358940a114e04
URL:		https://pypi.org/project/pytest-subtests/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:40.0
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest >= 6.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unittest subTest() support and subtests fixture.

%description -l pl.UTF-8
Obsługa subTest() i wyposażenie subtests dla szkieletu unittest.

%prep
%setup -q -n pytest-subtests-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_subtests \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_subtests.py
%{py3_sitescriptdir}/__pycache__/pytest_subtests.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_subtests-%{version}-py*.egg-info
