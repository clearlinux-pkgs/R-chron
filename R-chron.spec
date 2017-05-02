#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-chron
Version  : 2.3.50
Release  : 24
URL      : http://cran.r-project.org/src/contrib/chron_2.3-50.tar.gz
Source0  : http://cran.r-project.org/src/contrib/chron_2.3-50.tar.gz
Summary  : Chronological Objects which can Handle Dates and Times
Group    : Development/Tools
License  : GPL-2.0
Requires: R-chron-lib
Requires: R-ggplot2
Requires: R-zoo
BuildRequires : R-ggplot2
BuildRequires : R-zoo
BuildRequires : clr-R-helpers

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
export LANG=C
export SOURCE_DATE_EPOCH=1492795525

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492795525
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library chron
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library chron


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
/usr/lib64/R/library/chron/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/chron/libs/chron.so
