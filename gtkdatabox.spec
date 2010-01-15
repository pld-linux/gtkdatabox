#
Summary:	GtkDatabox - a GTK+ widget for fast data display
Summary(pl.UTF-8):	GtkDatabox - widget dla GTK+ do szybkiego wyświetlania danych
Name:		gtkdatabox
Version:	0.9.1.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtkdatabox/%{name}-%{version}.tar.gz
# Source0-md5:	910921da2198ebd02ea8a7eb622916ce
URL:		http://www.eudoxos.de/gtk/gtkdatabox/
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	gtk+2-devel >= 1:2.8.0
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
Requires:	gtk+2-devel >= 2.8.0

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
Summary:	GTK+ API documentation
Summary(pl.UTF-8):	Dokumentacja API GTK+
Group:		Documentation
Requires:	gtk-doc-common
Provides:	gail-apidocs = 1.23.0
Obsoletes:	gail-apidocs

%description apidocs
GTK+ API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GTK+.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libgtkdatabox-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkdatabox-*.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkdatabox.so
%{_libdir}/libgtkdatabox.la
%{_includedir}/gtkdatabox*.h
%{_pkgconfigdir}/gtkdatabox.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkdatabox.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
