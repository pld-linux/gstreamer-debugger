%define		gst_ver		1.7.0
%define		gstmm_ver	1.4.0

Summary:	Remote GStreamer Debugger
Summary(pl.UTF-8):	Zdalny debugger dla GStreamera
Name:		gstreamer-debugger
Version:	0.90.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gst-debugger/0.90/gst-debugger-%{version}.tar.xz
# Source0-md5:	846cba176ba5326a257f63b8139c4329
Patch0:		%{name}-include.patch
Patch1:		%{name}-link.patch
URL:		https://github.com/GNOME/gst-debugger
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	boost-devel >= 1.55
BuildRequires:	glib2-devel >= 1:2.41.1
BuildRequires:	graphviz-devel >= 2.38
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	gstreamermm-devel >= %{gstmm_ver}
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	gtkmm3-devel >= 3.14.0
BuildRequires:	libsigc++-devel >= 2.5.1
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	protobuf-c-devel >= 1.1.1
BuildRequires:	protobuf-devel >= 2.6.1
Requires:	glib2 >= 1:2.41.1
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamermm >= %{gstmm_ver}
Requires:	gtk+3-devel >= 3.14.0
Requires:	gtkmm3-devel >= 3.14.0
Requires:	libsigc++-devel >= 2.5.1
Requires:	protobuf-c >= 1.1.1
Requires:	protobuf-libs >= 2.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remote GStreamer Debugger.

%description -l pl.UTF-8
Zdalny debugger dla GStreamera.

%package devel
Summary:	Header files for gst-debugger
Summary(pl.UTF-8):	Pliki nagłówkowe gst-debuggera
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-devel >= %{gst_ver}
Requires:	protobuf-c-devel >= 1.1.1
Requires:	protobuf-devel >= 2.6.1

%description devel
Header files for gst-debugger.

%description devel -l pl.UTF-8
Pliki nagłówkowe gst-debuggera.

%prep
%setup -q -n gst-debugger-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I build -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
# module loaded through glib
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstdebugserver.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/gst-debugger-1.0
%attr(755,root,root) %{_libdir}/libgst-debugger-common-c-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgst-debugger-common-c-0.1.so.0
%attr(755,root,root) %{_libdir}/libgst-debugger-common-cpp-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgst-debugger-common-cpp-0.1.so.0
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstdebugserver.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgst-debugger-common-c-0.1.so
%attr(755,root,root) %{_libdir}/libgst-debugger-common-cpp-0.1.so
%{_includedir}/gst-debugger-0.1
%{_pkgconfigdir}/libgst-debugger-common-0.1.pc
