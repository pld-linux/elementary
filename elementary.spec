#
# TODO: - elementary_testql searches for modules in ../lib not _libdir
#	- plugins in separate packages
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_without	ewebkit		# Web (WebKit) support
#

%define		ecore_ver	1.7.6
%define		edbus_ver	1.7.6
%define		edje_ver	1.7.6
%define		eet_ver 	1.7.6
%define		efreet_ver 	1.7.6
%define		eina_ver	1.7.6
%define		evas_ver	1.7.6

Summary:	Basic widget set
Summary(pl.UTF-8):	Zestaw prostych widżetów
Name:		elementary
Version:	1.7.6
Release:	2
License:	LGPL v2.1
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	b9916d954ba71aa3a8735d5f37fa88c0
URL:		http://trac.enlightenment.org/e/wiki/Elementary
BuildRequires:	e_dbus-devel >= %{edbus_ver}
BuildRequires:	ecore-con-devel >= %{ecore_ver}
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	ecore-evas-devel >= %{ecore_ver}
BuildRequires:	ecore-fb-devel >= %{ecore_ver}
BuildRequires:	ecore-file-devel >= %{ecore_ver}
BuildRequires:	ecore-imf-devel >= %{ecore_ver}
BuildRequires:	ecore-sdl-devel >= %{ecore_ver}
BuildRequires:	ecore-wayland-devel >= %{ecore_ver}
BuildRequires:	ecore-x-devel >= %{ecore_ver}
BuildRequires:	edje >= %{edje_ver}
BuildRequires:	edje-devel >= %{edje_ver}
BuildRequires:	eet-devel >= %{eet_ver}
BuildRequires:	efreet-devel >= %{efreet_ver}
BuildRequires:	eina-devel >= %{eina_ver}
BuildRequires:	eio-devel
BuildRequires:	emotion-devel
BuildRequires:	ethumb-devel
BuildRequires:	evas-devel >= %{evas_ver}
BuildRequires:	evas-loader-jpeg >= %{evas_ver}
%{?with_webkit:BuildRequires:	ewebkit-devel >= 0-0.r127150.1}
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	pkgconfig >= 1:0.22
# TODO: eweather, emap
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elementary - a basic widget set that is easy to use based on EFL for
mobile touch-screen devices.

%description -l pl.UTF-8
Elementary - zestaw prostych, łatwych w użyciu widżetów, oparty na EFL
dla urządzeń mobilnych.

%package libs
Summary:	Elementary library
Summary(pl.UTF-8):	Bilblioteka Elementary
Group:		Libraries
Requires:	e_dbus >= %{edbus_ver}
Requires:	ecore >= %{ecore_ver}
Requires:	ecore-con >= %{ecore_ver}
Requires:	ecore-evas >= %{ecore_ver}
Requires:	ecore-fb >= %{ecore_ver}
Requires:	ecore-file >= %{ecore_ver}
Requires:	ecore-imf >= %{ecore_ver}
Requires:	ecore-sdl >= %{ecore_ver}
Requires:	ecore-wayland >= %{ecore_ver}
Requires:	ecore-x >= %{ecore_ver}
Requires:	edje-libs >= %{edje_ver}
Requires:	eet >= %{eet_ver}
Requires:	efreet >= %{efreet_ver}
Requires:	eina >= %{eina_ver}
Requires:	evas >= %{evas_ver}

%description libs
Elementary library files.

%description libs -l pl.UTF-8
Biblioteka Elementary.

%package devel
Summary:	Elementary header files
Summary(pl.UTF-8):	Pliki nagłówkowe Elementary
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	ecore-con-devel >= %{ecore_ver}
Requires:	ecore-devel >= %{ecore_ver}
Requires:	ecore-evas-devel >= %{ecore_ver}
Requires:	ecore-file-devel >= %{ecore_ver}
Requires:	ecore-imf-devel >= %{ecore_ver}
Requires:	ecore-sdl-devel >= %{ecore_ver}
Requires:	ecore-wayland-devel >= %{ecore_ver}
Requires:	ecore-x-devel >= %{ecore_ver}
Requires:	edje-devel >= %{edje_ver}
Requires:	eet-devel >= %{eet_ver}
Requires:	eina-devel >= %{eina_ver}
Requires:	evas-devel >= %{evas_ver}

%description devel
Header files for Elementary.

%description devel -l pl.UTF-8
Pliki nagłówkowe Elementary.

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
%configure \
	--disable-silent-rules \
	%{!?with_ewebkit:--disable-web} \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# icon is non-themed, so install in %{_pixmapsdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	icondir=%{_pixmapsdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/edje/modules/elm/linux-gnu-*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/elementary/modules/*/linux-gnu-*/*.la

mv $RPM_BUILD_ROOT%{_localedir}/az{_IR,}
mv $RPM_BUILD_ROOT%{_localedir}/ko{_KR,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/elementary_config
%attr(755,root,root) %{_bindir}/elementary_quicklaunch
%attr(755,root,root) %{_bindir}/elementary_run
%attr(755,root,root) %{_bindir}/elementary_test
%attr(755,root,root) %{_bindir}/elementary_testql
%{_desktopdir}/elementary_config.desktop
%{_desktopdir}/elementary_test.desktop
%{_datadir}/elementary
%{_pixmapsdir}/elementary.png

%files libs -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libelementary.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libelementary.so.1
%attr(755,root,root) %{_libdir}/elementary_testql.so
%dir %{_libdir}/edje/modules/elm
%dir %{_libdir}/edje/modules/elm/linux-gnu-*
%attr(755,root,root) %{_libdir}/edje/modules/elm/linux-gnu-*/module.so
%dir %{_libdir}/elementary
%dir %{_libdir}/elementary/modules
%dir %{_libdir}/elementary/modules/access_output
%dir %{_libdir}/elementary/modules/access_output/linux-gnu-*
%attr(755,root,root) %{_libdir}/elementary/modules/access_output/linux-gnu-*/module.so
%dir %{_libdir}/elementary/modules/datetime_input_ctxpopup
%dir %{_libdir}/elementary/modules/datetime_input_ctxpopup/linux-gnu-*
%attr(755,root,root) %{_libdir}/elementary/modules/datetime_input_ctxpopup/linux-gnu-*/module.so
%dir %{_libdir}/elementary/modules/test_entry
%dir %{_libdir}/elementary/modules/test_entry/linux-gnu-*
%attr(755,root,root) %{_libdir}/elementary/modules/test_entry/linux-gnu-*/module.so
%dir %{_libdir}/elementary/modules/test_map
%dir %{_libdir}/elementary/modules/test_map/linux-gnu-*
%attr(755,root,root) %{_libdir}/elementary/modules/test_map/linux-gnu-*/module.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libelementary.so
%{_libdir}/libelementary.la
%{_libdir}/elementary_testql.la
%{_includedir}/elementary-1
%{_pkgconfigdir}/elementary.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libelementary.a
%{_libdir}/elementary_testql.a
%endif
