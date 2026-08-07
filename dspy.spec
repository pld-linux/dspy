# TODO: use gtk4-update-icon-cache
Summary:	Explore the D-Bus
Summary(pl.UTF-8):	Eksplorator szyny D-Bus
Name:		dspy
Version:	50.0
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	https://download.gnome.org/sources/d-spy/50/d-spy-%{version}.tar.xz
# Source0-md5:	ca55a222ddaa2d2855b79c2cf7dfc4c6
URL:		https://apps.gnome.org/Dspy/
BuildRequires:	glib2-devel >= 1:2.82
BuildRequires:	gtk4-devel >= 4.16
BuildRequires:	libadwaita-devel >= 1.7
BuildRequires:	libdex-devel >= 0.11
BuildRequires:	meson >= 1.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.82
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.82
Requires:	gtk4 >= 4.16
Requires:	libadwaita >= 1.7
Requires:	libdex >= 0.11
Obsoletes:	dspy-libs < 48
Obsoletes:	dspy-devel < 48
Obsoletes:	dspy-static < 48
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

%prep
%setup -q -n d-spy-%{version}

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang d-spy

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f d-spy.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/d-spy
%{_datadir}/dbus-1/services/org.gnome.dspy.service
%{_datadir}/glib-2.0/schemas/org.gnome.dspy.gschema.xml
%{_datadir}/metainfo/org.gnome.dspy.metainfo.xml
%{_desktopdir}/org.gnome.dspy.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.dspy.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.dspy-symbolic.svg
