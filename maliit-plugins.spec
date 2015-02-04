Name:          maliit-plugins
Version:       0.94.2
Release:       1
Summary:       Input method plugins

Group:         System/Libraries
License:       BSD
URL:           http://maliit.org/
Source0:       http://maliit.org/releases/%{name}/%{name}-%{version}.tar.bz2
Patch0:        olpc_xo_layout_modifications.patch

BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(maliit-framework)
BuildRequires: qt4-devel
BuildRequires: doxygen

%description
Maliit provides a flexible and cross-platform input method plugins. It has a
plugin-based client-server architecture where applications act as clients and
communicate with the Maliit server via input context plugins. The communication
link currently uses D-Bus.

%prep
%setup -q
%apply_patches

%build
%qmake_qt4 -r CONFIG+=notests CONFIG+=disable-nemo-keyboard LIBDIR=%{_libdir} MALIIT_DEFAULT_PROFILE=olpc-xo
%make

%install
%makeinstall INSTALL="install -p" INSTALL_ROOT=%{buildroot} DESTDIR=%{buildroot}

find %{buildroot} -name '*.moc' -exec rm -rf {} ';'
find %{buildroot} -name '*.gitignore' -exec rm -rf {} ';'
find %{buildroot} -name '*.olpc-layouts' -exec rm -rf {} ';'

chmod 0644 %{buildroot}%{_bindir}/maliit-keyboard*
%{__strip} %{buildroot}/%{_bindir}/maliit-keyboard*

%files
%doc LICENSE README VERSION
%{_bindir}/maliit-keyboard*
%{_libdir}/maliit/plugins/libmaliit-keyboard-plugin.so
%{_datadir}/maliit/plugins
