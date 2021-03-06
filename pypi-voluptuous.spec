#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-voluptuous
Version  : 0.13.1
Release  : 54
URL      : https://files.pythonhosted.org/packages/72/0c/0ed7352eeb7bd3d53d2c0ae87fa1e222170f53815b8df7d9cdce7ffedec0/voluptuous-0.13.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/72/0c/0ed7352eeb7bd3d53d2c0ae87fa1e222170f53815b8df7d9cdce7ffedec0/voluptuous-0.13.1.tar.gz
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
%setup -q -n voluptuous-0.13.1
cd %{_builddir}/voluptuous-0.13.1
pushd ..
cp -a voluptuous-0.13.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656362967
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-voluptuous
cp %{_builddir}/voluptuous-0.13.1/COPYING %{buildroot}/usr/share/package-licenses/pypi-voluptuous/2b280b388697926832dc180bb05b9bba2086b783
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
