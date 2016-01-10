Summary:	GtkDatabox - a GTK+ widget for fast data display
Summary(pl.UTF-8):	GtkDatabox - widget dla GTK+ do szybkiego wyświetlania danych
Name:		gtkdatabox
Version:	0.9.1.3
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gtkdatabox/%{name}-%{version}.tar.gz
# Source0-md5:	60a3eebd61a4ca36879d7e60d1aca727
Patch0:		new-gtk.patch
URL:		http://sourceforge.net/projects/gtkdatabox/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	libglade2-devel
BuildRequires:	libgladeui-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	cairo >= 1.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkDatabox is a widget for the Gtk+-library designed to display large
amounts of numerical data fast and easy.

%description -l pl.UTF-8
GtkDatabox jest widgetem dla biblioteki Gtk+ zaprojektowanym do
wyświetlania dużych ilości danych numerycznych prosto i szybko.

%package devel
Summary:	Header files for GtkDatabox library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GtDatabox
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.4.0
Requires:	gtk+2-devel >= 2:2.8.0

%description devel
Header files for GtkDatabox library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GtkDatabox.

%package static
Summary:	Static GtkDatabox library
Summary(pl.UTF-8):	Statyczna biblioteka GtkDatabox
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GtkDatabox library.

%description static -l pl.UTF-8
Statyczna biblioteka GtkDatabox.

%package apidocs
Summary:	GtkDatabox API documentation
Summary(pl.UTF-8):	Dokumentacja API GtkDatabox
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
GtkDatabox API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GtkDatabox.

%package -n glade3-%{name}
Summary:	GtkDatabox support for Glade 3
Summary(pl.UTF-8):	Wsparcie dla GtkDatabox w Glade 3
Group:		Development/Building
Requires:	glade3

%description -n glade3-%{name}
GtkDatabox support for Glade 3.

%description -n glade3-%{name} -l pl.UTF-8
Wsparcie dla GtkDatabox w Glade 3.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--enable-libglade \
	--enable-glade \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgtkdatabox.la \
	$RPM_BUILD_ROOT%{_libdir}/glade3/modules/libgladedatabox.{la,a} \
	$RPM_BUILD_ROOT%{_libdir}/libglade/2.0/libdatabox.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libgtkdatabox-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkdatabox-0.9.1.so.3
%attr(755,root,root) %{_libdir}/libglade/2.0/libdatabox.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkdatabox.so
%{_includedir}/gtkdatabox*.h
%{_pkgconfigdir}/gtkdatabox.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkdatabox.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files -n glade3-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glade3/modules/libgladedatabox.so
%{_datadir}/glade3/catalogs/gtkdatabox.xml
