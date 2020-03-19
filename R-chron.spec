#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-chron
Version  : 2.3.55
Release  : 63
URL      : https://cran.r-project.org/src/contrib/chron_2.3-55.tar.gz
Source0  : https://cran.r-project.org/src/contrib/chron_2.3-55.tar.gz
Summary  : Chronological Objects which can Handle Dates and Times
Group    : Development/Tools
License  : GPL-2.0
Requires: R-chron-lib = %{version}-%{release}
Requires: R-ggplot2
Requires: R-zoo
BuildRequires : R-ggplot2
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
This directory contains code and help for an R port of CHRON, an S-PLUS
package for working with chronological objects (times and dates).

%package lib
Summary: lib components for the R-chron package.
Group: Libraries

%description lib
lib components for the R-chron package.


%prep
%setup -q -c -n chron

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580749527

%install
export SOURCE_DATE_EPOCH=1580749527
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library chron
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library chron
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library chron
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc chron || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/chron/CITATION
/usr/lib64/R/library/chron/DESCRIPTION
/usr/lib64/R/library/chron/INDEX
/usr/lib64/R/library/chron/Meta/Rd.rds
/usr/lib64/R/library/chron/Meta/features.rds
/usr/lib64/R/library/chron/Meta/hsearch.rds
/usr/lib64/R/library/chron/Meta/links.rds
/usr/lib64/R/library/chron/Meta/nsInfo.rds
/usr/lib64/R/library/chron/Meta/package.rds
/usr/lib64/R/library/chron/NAMESPACE
/usr/lib64/R/library/chron/R/chron
/usr/lib64/R/library/chron/R/chron.rdb
/usr/lib64/R/library/chron/R/chron.rdx
/usr/lib64/R/library/chron/help/AnIndex
/usr/lib64/R/library/chron/help/aliases.rds
/usr/lib64/R/library/chron/help/chron.rdb
/usr/lib64/R/library/chron/help/chron.rdx
/usr/lib64/R/library/chron/help/paths.rds
/usr/lib64/R/library/chron/html/00Index.html
/usr/lib64/R/library/chron/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/chron/libs/chron.so
