# TODO: use gtk4-update-icon-cache
Summary:	Explore the D-Bus
Summary(pl.UTF-8):	Eksplorator szyny D-Bus
Name:		dspy
Version:	48.0
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	https://download.gnome.org/sources/d-spy/48/d-spy-%{version}.tar.xz
# Source0-md5:	326480553615999c44d67dfbb0d5cad2
URL:		https://apps.gnome.org/Dspy/
BuildRequires:	glib2-devel >= 1:2.76
BuildRequires:	gtk4-devel >= 4.12
BuildRequires:	libadwaita-devel >= 1.5
BuildRequires:	meson >= 1.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.76
Requires(post,postun):	gtk-update-icon-cache
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
%attr(755,root,root) %{_bindir}/d-spy
%{_datadir}/glib-2.0/schemas/org.gnome.dspy.gschema.xml
%{_datadir}/metainfo/org.gnome.dspy.appdata.xml
%{_desktopdir}/org.gnome.dspy.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.dspy.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.dspy-symbolic.svg
