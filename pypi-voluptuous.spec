#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-voluptuous
Version  : 0.12.2
Release  : 49
URL      : https://files.pythonhosted.org/packages/c0/2c/ccbeb25364e3e0c5e4522f13d66e2fc639bb4d4ecdf73be0959552cbecb4/voluptuous-0.12.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/2c/ccbeb25364e3e0c5e4522f13d66e2fc639bb4d4ecdf73be0959552cbecb4/voluptuous-0.12.2.tar.gz
Summary  : UNKNOWN
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-voluptuous-license = %{version}-%{release}
Requires: pypi-voluptuous-python = %{version}-%{release}
Requires: pypi-voluptuous-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# CONTRIBUTIONS ONLY
        
        **What does this mean?** I do not have time to fix issues myself. The only way fixes or new features will be added is by people submitting PRs.

%package license
Summary: license components for the pypi-voluptuous package.
Group: Default

%description license
license components for the pypi-voluptuous package.


%package python
Summary: python components for the pypi-voluptuous package.
Group: Default
Requires: pypi-voluptuous-python3 = %{version}-%{release}

%description python
python components for the pypi-voluptuous package.


%package python3
Summary: python3 components for the pypi-voluptuous package.
Group: Default
Requires: python3-core
Provides: pypi(voluptuous)

%description python3
python3 components for the pypi-voluptuous package.


%prep
%setup -q -n voluptuous-0.12.2
cd %{_builddir}/voluptuous-0.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641945717
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-voluptuous
cp %{_builddir}/voluptuous-0.12.2/COPYING %{buildroot}/usr/share/package-licenses/pypi-voluptuous/2b280b388697926832dc180bb05b9bba2086b783
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-voluptuous/2b280b388697926832dc180bb05b9bba2086b783

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
