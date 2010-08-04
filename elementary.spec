# Conditional build:
%bcond_without	static_libs	# don't build static library

%define		snapdate	2010-06-27
%define		svn		-ver-svn-06
Summary:	Basic widget set
Summary(pl.UTF-8):	Zestaw prostych widżetów
Name:		elementary
Version:	0.7.0.49898
Release:	0.1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://download.enlightenment.org/snapshots/%{snapdate}/%{name}-%{version}.tar.bz2
# Source0-md5:	e388b8bfb1e09982dd881a075870b914
URL:		http://enlightenment.org/p.php?p=about/libs/eina
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elementary - a basic widget set that is easy to use based on EFL for mobile
touch-screen devices.

%description -l pl.UTF-8
Elementary - zestaw prostych, łatwych w użyciu widżetów oparty na EFL
dla urządzeń mobilnych.

%package devel
Summary:	Elementary header files
Summary(pl.UTF-8):	Pliki nagłówkowe Elementary
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Elementary.

%description devel -l pl.UTF-8
Pliki nagłówkowe Elementary.

%package libs
Summary:	Elementary library
Summary(pl.UTF-8):	Bilblioteka Elementary
Group:		Libraries

%description libs
Elementary library files.

%description libs -l pl.UTF-8
Biblioteka Elementary.

%package static
Summary:	Static Elementary library
Summary(pl.UTF-8):	Statyczna biblioteka Elementary
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Elementary library.

%description static -l pl.UTF-8
Statyczna biblioteka Elementary.

%prep
%setup -q

%build
rm -rf autom4te.cache
rm -f aclocal.m4 ltmain.sh
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}

%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/elementary_config
%attr(755,root,root) %{_bindir}/elementary_quicklaunch
%attr(755,root,root) %{_bindir}/elementary_run
%attr(755,root,root) %{_bindir}/elementary_test
%attr(755,root,root) %{_bindir}/elementary_testql
%{_datadir}/applications/elementary_config.desktop
%{_datadir}/applications/elementary_test.desktop
%{_datadir}/elementary
%{_iconsdir}/elementary.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/Elementary.h
%dir %{_includedir}/elementary
%{_includedir}/elementary/elementary_config.h
%{_libdir}/edje/elm.la
%{_libdir}/elementary/modules/test_entry/linux-gnu-i686-ver-svn-06/module.la
%{_libdir}/elementary_testql.la
%{_libdir}/libelementary.la
%{_libdir}/libelementary.so
%{_pkgconfigdir}/elementary.pc

%files libs
%defattr(644,root,root,755)
%attr(755,root,roo) %{_libdir}/edje/elm.so
%dir %{_libdir}/elementary
%dir %{_libdir}/elementary/modules
%dir %{_libdir}/elementary/modules/test_entry
%dir %{_libdir}/elementary/modules/test_entry/linux-gnu-*
%attr(755,root,root) %{_libdir}/elementary/modules/test_entry/linux-gnu-*%{svn}/module.so
%attr(755,root,root) %{_libdir}/elementary_testql.so
%attr(755,root,root) %{_libdir}/libelementary%{svn}.so.0.7.0
%attr(755,root,root) %ghost %{_libdir}/libelementary%{svn}.so.0

%if %{with static_libs}
%files static
%{_libdir}/elementary_testql.a
%{_libdir}/libelementary.a
%defattr(644,root,root,755)
%endif
