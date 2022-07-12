# TODO: use gtk4-update-icon-cache
Summary:	Explore the D-Bus
Summary(pl.UTF-8):	Eksplorator szyny D-Bus
Name:		dspy
Version:	1.2.1
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	https://download.gnome.org/sources/dspy/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	86cf82235173bb9b5e8ed06dde5aae5b
URL:		https://gitlab.gnome.org/GNOME/d-spy
BuildRequires:	glib2-devel >= 1:2.68
BuildRequires:	gtk4-devel >= 4.6
BuildRequires:	libadwaita-devel >= 1.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.68
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-Spy is a tool to explore and test end-points and interfaces on the
System or Session D-Bus. You can also connect to D-Bus peers by
address. D-Spy was originally part of GNOME Builder.

%description -l pl.UTF-8
D-Spy to narzędzie do badania i testowania końcówek oraz interfejsów
systemowej lub sesyjnej szyny D-Bus. Pozwala także łączyć się z
partnerami szyny po adresie. D-Spy pierwotnie był częścią projektu
GNOME Builder.

%package libs
Summary:	D-Spy shared library
Summary(pl.UTF-8):	Biblioteka współdzielona D-Spy
License:	LGPL v3+
Group:		Libraries
Requires:	glib2 >= 1:2.68
Requires:	gtk4 >= 4.6
Requires:	libadwaita >= 1.0

%description libs
D-Spy shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona D-Spy.

%package devel
Summary:	Header files for D-Spy library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki D-Spy
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.68
Requires:	gtk4-devel >= 4.6

%description devel
Header files for D-Spy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki D-Spy.

%package static
Summary:	D-Spy static library
Summary(pl.UTF-8):	Biblioteka statyczna D-Spy
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
D-Spy static library.

%description static -l pl.UTF-8
Biblioteka statyczna D-Spy.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/d-spy
%{_datadir}/appdata/org.gnome.dspy.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.dspy.gschema.xml
%{_desktopdir}/org.gnome.dspy.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.dspy.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.dspy.devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.dspy-symbolic.svg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdspy-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdspy-1.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdspy-1.so
%{_includedir}/dspy-1
%{_pkgconfigdir}/dspy-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdspy-1.a
