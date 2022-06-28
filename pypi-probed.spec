#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-probed
Version  : 0.0.9
Release  : 5
URL      : https://files.pythonhosted.org/packages/c3/18/be9761540de35b122efd4e15038d1efeec632305bd57d82cef13c9c66dda/probed-0.0.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/c3/18/be9761540de35b122efd4e15038d1efeec632305bd57d82cef13c9c66dda/probed-0.0.9.tar.gz
Summary  : Probed collections
Group    : Development/Tools
License  : MIT
Requires: pypi-probed-bin = %{version}-%{release}
Requires: pypi-probed-license = %{version}-%{release}
Requires: pypi-probed-python = %{version}-%{release}
Requires: pypi-probed-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
# Probed collections
This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).
> [Installation](#installation) . [Latest](https://github.com/pyrustic/probed/tags) . [Documentation](https://github.com/pyrustic/probed/tree/master/docs/modules#readme)

%package bin
Summary: bin components for the pypi-probed package.
Group: Binaries
Requires: pypi-probed-license = %{version}-%{release}

%description bin
bin components for the pypi-probed package.


%package license
Summary: license components for the pypi-probed package.
Group: Default

%description license
license components for the pypi-probed package.


%package python
Summary: python components for the pypi-probed package.
Group: Default
Requires: pypi-probed-python3 = %{version}-%{release}

%description python
python components for the pypi-probed package.


%package python3
Summary: python3 components for the pypi-probed package.
Group: Default
Requires: python3-core
Provides: pypi(probed)

%description python3
python3 components for the pypi-probed package.


%prep
%setup -q -n probed-0.0.9
cd %{_builddir}/probed-0.0.9
pushd ..
cp -a probed-0.0.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656395540
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-probed
cp %{_builddir}/probed-0.0.9/LICENSE %{buildroot}/usr/share/package-licenses/pypi-probed/4bf523651dbfe0fa3a55d23d58726a25299355ac
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/tests/__init__.py
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/tests/__pycache__/__init__.cpython-*.pyc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/probed

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-probed/4bf523651dbfe0fa3a55d23d58726a25299355ac

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
