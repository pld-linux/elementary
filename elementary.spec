#
# TODO: - elementary_testql searches for modules in ../lib not _libdir
#	- plugins in separate packages
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#

%define		svn		-ver-pre-svn-09
%define		ecore_ver	1.0.0
%define		edje_ver	1.0.0
%define		eet_ver 	1.4.0
%define		eina_ver	1.0.0
%define		evas_ver	1.0.0

Summary:	Basic widget set
Summary(pl.UTF-8):	Zestaw prostych widżetów
Name:		elementary
Version:	0.7.0.55225
Release:	0.3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
# Source0-md5:	0c4460fe656c8dafc42abee76c33975c
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-evas-devel >= %{ecore_ver}
BuildRequires:	edje >= %{edje_ver}
BuildRequires:	edje-devel >= %{edje_ver}
BuildRequires:	eet-devel >= %{eet_ver}
BuildRequires:	eina-devel >= %{eina_ver}
BuildRequires:	evas-devel >= %{evas_ver}
BuildRequires:	evas-loader-jpeg >= %{evas_ver}
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elementary - a basic widget set that is easy to use based on EFL for
mobile touch-screen devices.

%description -l pl.UTF-8
Elementary - zestaw prostych, łatwych w użyciu widżetów, oparty na EFL
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
%{_desktopdir}/elementary_config.desktop
%{_desktopdir}/elementary_test.desktop
%{_datadir}/elementary
%{_iconsdir}/elementary.png

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/elementary-0
%{_includedir}/elementary-0/Elementary.h
%{_includedir}/elementary-0/Elementary_Cursor.h
%{_includedir}/elementary-0/elm_widget.h
%{_libdir}/edje/modules/elm/linux-gnu-%{_target_cpu}-1.0.0/module.la
%{_libdir}/elementary/modules/test_entry/linux-gnu-%{_target_cpu}-0.7.0/module.la
%{_libdir}/elementary_testql.la
%{_libdir}/libelementary.la
%{_libdir}/libelementary.so
%{_pkgconfigdir}/elementary.pc

%files libs
%defattr(644,root,root,755)
#%%attr(755,root,roo) %{_libdir}/edje/elm.so
%dir %{_libdir}/elementary
%dir %{_libdir}/elementary/modules
%dir %{_libdir}/elementary/modules/test_entry
%dir %{_libdir}/elementary/modules/test_entry/linux-gnu-*
%dir %{_libdir}/edje/modules
%dir %{_libdir}/edje/modules/elm
%dir %{_libdir}/edje/modules/elm/linux-gnu-%{_target_cpu}-1.0.0
%{_libdir}/edje/modules/elm/linux-gnu-%{_target_cpu}-1.0.0/module.so
%{_libdir}/elementary/modules/test_entry/linux-gnu-%{_target_cpu}-0.7.0/module.so
%attr(755,root,root) %{_libdir}/elementary_testql.so
%attr(755,root,root) %{_libdir}/libelementary%{svn}.so.0.7.0
%attr(755,root,root) %ghost %{_libdir}/libelementary%{svn}.so.0

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/elementary_testql.a
%{_libdir}/libelementary.a
%defattr(644,root,root,755)
%endif
