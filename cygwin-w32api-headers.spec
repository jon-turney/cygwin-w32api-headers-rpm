#%%global snapshot_rev 5747
#%%global branch trunk

Name:           cygwin-w32api-headers
Version:        7.0.0
Release:        1%{?dist}
Summary:        Win32 header files for Cygwin toolchain

License:        Public Domain and LGPLv2+ and ZPLv2.1
Group:          Development/Libraries
URL:            http://mingw-w64.sourceforge.net/
BuildArch:      noarch

%if 0%{?snapshot_rev}
# To regenerate a snapshot:
# First, in any browser (need not be on the same machine), go to:
# http://sourceforge.net/p/mingw-w64/code/%{snapshot_rev}/tarball?path=/trunk
# Once the download is ready, then run:
# wget http://sourceforge.net/code-snapshots/svn/m/mi/mingw-w64/code/mingw-w64-code-%{snapshot_rev}-%{branch}.zip
Source0:        mingw-w64-code-%{snapshot_rev}-%{branch}.zip
%else
Source0:        http://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}.tar.bz2
%endif

BuildRequires:  cygwin32-filesystem
BuildRequires:  cygwin64-filesystem

%description
Cygwin cross-compiler Win32 header files.

%package -n cygwin32-w32api-headers
Summary:   Win32 header files for Cygwin32 toolchain
Requires:  cygwin32-filesystem
Provides:  %{name} = %{version}-%{release}
Obsoletes: %{name} < %{version}-%{release}

%description -n cygwin32-w32api-headers
Cygwin i686 cross-compiler Win32 header files.

%package -n cygwin64-w32api-headers
Summary:   Win32 header files for Cygwin64 toolchain
Requires:  cygwin64-filesystem

%description -n cygwin64-w32api-headers
Cygwin x86_64 cross-compiler Win32 header files.


%prep
%if 0%{?snapshot_rev}
%setup -q -n mingw-w64-code-%{snapshot_rev}-%{branch}
%else
%setup -q -n mingw-w64-v%{version}
%endif

%build
pushd mingw-w64-headers
    CYGWIN32_CONFIGURE_ARGS="--includedir=%{cygwin32_includedir}/w32api"
    CYGWIN64_CONFIGURE_ARGS="--includedir=%{cygwin64_includedir}/w32api"
    %cygwin_configure --enable-w32api
popd


%install
pushd mingw-w64-headers
    %cygwin_make_install DESTDIR=$RPM_BUILD_ROOT
popd


%files -n cygwin32-w32api-headers
%doc COPYING DISCLAIMER DISCLAIMER.PD mingw-w64-headers/direct-x/COPYING.LIB
%{cygwin32_includedir}/w32api/

%files -n cygwin64-w32api-headers
%doc COPYING DISCLAIMER DISCLAIMER.PD mingw-w64-headers/direct-x/COPYING.LIB
%{cygwin64_includedir}/w32api/


%changelog
* Thu Dec 20 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 5.0.4-1
- new version

* Wed Nov 15 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 5.0.3-1
- new version

* Wed Mar 30 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 4.0.5-1
- new version

* Sun Feb 21 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 4.0.4-1
- new version

* Wed Mar 04 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.3.0-1
- new version

* Mon Sep 01 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.2.0-1
- Version bump

* Sun Jan 19 2014 Yaakov Selkowitz <cygwin-ports-general@lists.sourceforge.net> - 3.1.0-2
- Backport upstream r6328-r6329 for Cygwin64.

* Thu Jan 16 2014 Yaakov Selkowitz <cygwin-ports-general@lists.sourceforge.net> - 3.1.0-1
- Update to latest stable release.

* Thu Jun 27 2013 Yaakov Selkowitz <cygwin-ports-general@lists.sourceforge.net> - 2.0.999-4.trunk.svn5747
- Update to match current Cygwin package.
- Update to new Cygwin packaging scheme.

* Mon Jan 21 2013 Yaakov Selkowitz <cygwin-ports-general@lists.sourceforge.net> - 2.0.999-1.trunk.20121215
- Update to match current Cygwin package.

* Tue Oct 16 2012 Yaakov Selkowitz <cygwin-ports-general@lists.sourceforge.net> - 2.0.999-1.trunk.20121016
- Replace mingw.org w32api with mingw-w64 to match Cygwin distribution.
