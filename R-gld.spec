#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gld
Version  : 2.6.6
Release  : 28
URL      : https://cran.r-project.org/src/contrib/gld_2.6.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gld_2.6.6.tar.gz
Summary  : Estimation and Use of the Generalised (Tukey) Lambda
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-gld-lib = %{version}-%{release}
Requires: R-e1071
Requires: R-lmom
BuildRequires : R-e1071
BuildRequires : R-lmom
BuildRequires : buildreq-R

%description
provides a wide variety of shapes with one functional form.   
  This package provides random numbers, quantiles, probabilities, 
  densities and density quantiles for four different types of the distribution,
  the FKML (Freimer et al 1988), RS (Ramberg and Schmeiser 1974), GPD (van Staden
  and Loots 2009) and FM5 - see documentation for details.
  It provides the density function, distribution function, and Quantile-Quantile 
  plots.  
  It implements a variety of estimation methods for the distribution, 
  including diagnostic plots. 
  Estimation methods include the starship (all 4 types), 
  method of L-Moments for the GPD and FKML types, and a 
  number of methods for only the FKML type.  
  These include maximum likelihood, maximum product of spacings, 
  Titterington's method, Moments, Trimmed L-Moments and 
  Distributional Least Absolutes.

%package lib
Summary: lib components for the R-gld package.
Group: Libraries

%description lib
lib components for the R-gld package.


%prep
%setup -q -n gld
cd %{_builddir}/gld

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666635341

%install
export SOURCE_DATE_EPOCH=1666635341
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gld/DESCRIPTION
/usr/lib64/R/library/gld/INDEX
/usr/lib64/R/library/gld/Meta/Rd.rds
/usr/lib64/R/library/gld/Meta/features.rds
/usr/lib64/R/library/gld/Meta/hsearch.rds
/usr/lib64/R/library/gld/Meta/links.rds
/usr/lib64/R/library/gld/Meta/nsInfo.rds
/usr/lib64/R/library/gld/Meta/package.rds
/usr/lib64/R/library/gld/NAMESPACE
/usr/lib64/R/library/gld/NEWS
/usr/lib64/R/library/gld/R/gld
/usr/lib64/R/library/gld/R/gld.rdb
/usr/lib64/R/library/gld/R/gld.rdx
/usr/lib64/R/library/gld/help/AnIndex
/usr/lib64/R/library/gld/help/aliases.rds
/usr/lib64/R/library/gld/help/gld.rdb
/usr/lib64/R/library/gld/help/gld.rdx
/usr/lib64/R/library/gld/help/paths.rds
/usr/lib64/R/library/gld/html/00Index.html
/usr/lib64/R/library/gld/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gld/libs/gld.so
/usr/lib64/R/library/gld/libs/gld.so.avx2
/usr/lib64/R/library/gld/libs/gld.so.avx512
