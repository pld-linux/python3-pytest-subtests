#
# Conditional build:
%bcond_with	tests	# unit tests

Summary:	unittest subTest() support and subtests fixture
Summary(pl.UTF-8):	Obsługa subTest() i wyposażenie subtests dla szkieletu unittest
Name:		python3-pytest-subtests
# note: 0.7+ require pytest 7
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-subtests/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-subtests/pytest_subtests-%{version}.tar.gz
# Source0-md5:	f4dadd94661e81b47fdad3ddedc51038
URL:		https://pypi.org/project/pytest-subtests/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-build
BuildRequires:	python3-installer
%if %{with tests}
BuildRequires:	python3-pytest >= 6.0
BuildRequires:	python3-pytest-xdist
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
%setup -q -n pytest_subtests-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_subtests \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_subtests
%{py3_sitescriptdir}/pytest_subtests-%{version}.dist-info
