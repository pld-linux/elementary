# TODO: (some) plugins in separate packages?
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_without	fb		# Ecore FB support
%bcond_without	sdl		# Ecore SDL support
%bcond_with	wayland		# Ecore Wayland support
%bcond_without	elocation	# Elocation support
%bcond_with	emap		# Emap support [not available yet in PLD]
%bcond_without	eweather	# Eweather support
%bcond_without	ewebkit		# Web (WebKit) support
#

%define		efl_ver		1.9.1

Summary:	Basic widget set
Summary(pl.UTF-8):	Zestaw prostych widżetów
Name:		elementary
Version:	1.9.2
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://download.enlightenment.org/rel/libs/elementary/%{name}-%{version}.tar.bz2
# Source0-md5:	0709699bd3b92660b946137f45c57add
URL:		http://trac.enlightenment.org/e/wiki/Elementary
BuildRequires:	ecore-con-devel >= %{efl_ver}
BuildRequires:	ecore-devel >= %{efl_ver}
BuildRequires:	ecore-evas-devel >= %{efl_ver}
%{?with_fb:BuildRequires:	ecore-fb-devel >= %{efl_ver}}
BuildRequires:	ecore-file-devel >= %{efl_ver}
BuildRequires:	ecore-imf-devel >= %{efl_ver}
BuildRequires:	ecore-input-devel >= %{efl_ver}
%{?with_sdl:BuildRequires:	ecore-sdl-devel >= %{efl_ver}}
%{?with_wayland:BuildRequires:	ecore-wayland-devel >= %{efl_ver}}
BuildRequires:	ecore-x-devel >= %{efl_ver}
BuildRequires:	edje >= %{efl_ver}
BuildRequires:	edje-devel >= %{efl_ver}
BuildRequires:	eet-devel >= %{efl_ver}
BuildRequires:	efreet-devel >= %{efl_ver}
BuildRequires:	eina-devel >= %{efl_ver}
BuildRequires:	eio-devel >= %{efl_ver}
BuildRequires:	eldbus-devel >= %{efl_ver}
%{?with_elocation:BuildRequires:	elocation-devel >= 0.1.0}
%{?with_emap:BuildRequires:	emap-devel}
BuildRequires:	emotion-devel >= %{efl_ver}
BuildRequires:	eo-devel >= %{efl_ver}
BuildRequires:	ethumb-devel >= %{efl_ver}
BuildRequires:	evas-devel >= %{efl_ver}
BuildRequires:	evas-loader-jpeg >= %{evas_ver}
%{?with_webkit:BuildRequires:	ewebkit-devel >= 0-0.r127150.1}
BuildRequires:	gettext-devel >= 0.17
%{?with_eweather:BuildRequires:	libeweather-devel}
BuildRequires:	pkgconfig >= 1:0.22
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		efl_arch_tag	v-1.9
%define		elm_arch_tag	v-%{version}

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
Requires:	ecore-con >= %{efl_ver}
Requires:	ecore >= %{efl_ver}
Requires:	ecore-evas >= %{efl_ver}
%{?with_fb:Requires:	ecore-fb >= %{efl_ver}}
Requires:	ecore-file >= %{efl_ver}
Requires:	ecore-imf >= %{efl_ver}
Requires:	ecore-input >= %{efl_ver}
%{?with_sdl:Requires:	ecore-sdl >= %{efl_ver}}
%{?with_wayland:Requires:	ecore-wayland >= %{efl_ver}}
Requires:	ecore-x >= %{efl_ver}
Requires:	edje-libs >= %{efl_ver}
Requires:	eet >= %{efl_ver}
Requires:	efreet-libs >= %{efl_ver}
Requires:	eina >= %{efl_ver}
Requires:	eio >= %{efl_ver}
Requires:	eldbus >= %{efl_ver}
%{?with_elocation:Requires:	elocation >= 0.1.0}
Requires:	emotion >= %{efl_ver}
Requires:	eo >= %{efl_ver}
Requires:	ethumb-libs >= %{efl_ver}
Requires:	evas >= %{efl_ver}
%{?with_webkit:Requires:	ewebkit >= 0-0.r127150.1}

%description libs
Elementary library files.

%description libs -l pl.UTF-8
Biblioteka Elementary.

%package devel
Summary:	Elementary header files
Summary(pl.UTF-8):	Pliki nagłówkowe Elementary
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	ecore-con-devel >= %{efl_ver}
Requires:	ecore-devel >= %{efl_ver}
Requires:	ecore-evas-devel >= %{efl_ver}
%{?with_fb:Requires:	ecore-fb-devel >= %{efl_ver}}
Requires:	ecore-file-devel >= %{efl_ver}
Requires:	ecore-imf-devel >= %{efl_ver}
Requires:	ecore-input-devel >= %{efl_ver}
%{?with_sdl:Requires:	ecore-sdl-devel >= %{efl_ver}}
%{?with_wayland:Requires:	ecore-wayland-devel >= %{efl_ver}}
Requires:	ecore-x-devel >= %{efl_ver}
Requires:	edje-devel >= %{efl_ver}
Requires:	eet-devel >= %{efl_ver}
Requires:	efreet-devel >= %{efl_ver}
Requires:	eina-devel >= %{efl_ver}
Requires:	eio-devel >= %{efl_ver}
Requires:	eldbus-devel >= %{efl_ver}
%{?with_elocation:Requires:	elocation-devel >= 0.1.0}
%{?with_emap:Requires:	emap-devel}
Requires:	emotion-devel >= %{efl_ver}
Requires:	eo-devel >= %{efl_ver}
Requires:	ethumb-devel >= %{efl_ver}
Requires:	evas-devel >= %{efl_ver}
Requires:	evas-loader-jpeg >= %{evas_ver}
%{?with_webkit:Requires:	ewebkit-devel >= 0-0.r127150.1}
%{?with_eweather:Requires:	libeweather-devel}

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
	--disable-ecore-cocoa \
	%{!?with_fb:--disable-ecore-fb} \
	--disable-ecore-psl1ght \
	%{!?with_sdl:--disable-ecore-sdl} \
	%{!?with_wayland:--disable-ecore-wayland} \
	--disable-ecore-win32 \
	--disable-ecore-wince \
	%{!?with_elocation:--disable-elocation} \
	%{!?with_emap:--disable-emap} \
	%{!?with_eweather:--disable-eweather} \
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/edje/modules/elm/%{efl_arch_tag}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/elementary/modules/*/%{elm_arch_tag}/*.la

mv $RPM_BUILD_ROOT%{_localedir}/ko{_KR,}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libelementary.la

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
%attr(755,root,root) %{_bindir}/elm_prefs_cc
%{_desktopdir}/elementary_config.desktop
%{_desktopdir}/elementary_test.desktop
%{_datadir}/elementary
%{_pixmapsdir}/elementary.png

%files libs -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libelementary.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libelementary.so.1
%dir %{_libdir}/edje/modules/elm
%dir %{_libdir}/edje/modules/elm/%{efl_arch_tag}
%attr(755,root,root) %{_libdir}/edje/modules/elm/%{efl_arch_tag}/module.so
%dir %{_libdir}/elementary
%dir %{_libdir}/elementary/modules
%dir %{_libdir}/elementary/modules/access_output
%dir %{_libdir}/elementary/modules/access_output/%{elm_arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/access_output/%{elm_arch_tag}/module.so
%dir %{_libdir}/elementary/modules/datetime_input_ctxpopup
%dir %{_libdir}/elementary/modules/datetime_input_ctxpopup/%{elm_arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/datetime_input_ctxpopup/%{elm_arch_tag}/module.so
%dir %{_libdir}/elementary/modules/prefs
%dir %{_libdir}/elementary/modules/prefs/%{elm_arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/prefs/%{elm_arch_tag}/module.so
%{_libdir}/elementary/modules/prefs/%{elm_arch_tag}/elm_prefs_swallow.edj
%dir %{_libdir}/elementary/modules/test_entry
%dir %{_libdir}/elementary/modules/test_entry/%{elm_arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/test_entry/%{elm_arch_tag}/module.so
%dir %{_libdir}/elementary/modules/test_map
%dir %{_libdir}/elementary/modules/test_map/%{elm_arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/test_map/%{elm_arch_tag}/module.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/elementary_codegen
%attr(755,root,root) %{_libdir}/libelementary.so
%{_includedir}/elementary-1
%{_pkgconfigdir}/elementary.pc
%{_libdir}/cmake/Elementary

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libelementary.a
%endif
