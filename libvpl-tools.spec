# TODO: OpenCL (-DTOOLS_ENABLE_OPENCL=ON)?
Summary:	Intel Video Processing Library Tools
Summary(pl.UTF-8):	Narzędzia do biblioteki przetwarzania obrazu Intel VPL
Name:		libvpl-tools
Version:	1.0.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/intel/libvpl-tools/releases
Source0:	https://github.com/intel/libvpl-tools/archive/v%{version}/libvpl-tools-%{version}.tar.gz
# Source0-md5:	e83ecee5f45d83b450597d4f7b982e9a
Patch0:		%{name}-types.patch
URL:		https://www.intel.com/content/www/us/en/developer/tools/vpl/overview.html
BuildRequires:	cmake >= 3.13.0
BuildRequires:	libdrm-devel >= 2.4.91
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libva-devel >= 1.2
BuildRequires:	libva-drm-devel >= 1.2
BuildRequires:	libva-x11-devel >= 1.10.0
BuildRequires:	libvpl-devel >= 2.11.0
# xcb;xcb-dri3;x11-xcb;xcb-present
BuildRequires:	libxcb-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
# wayland-client
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.15
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libpciaccess-devel
Requires:	libvpl >= 2.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Intel Video Processing Library (Intel VPL) tools provide access to
accelerated video decode, encode, and frame processing capabilities on
Intel GPUs from the command line.

%description -l pl.UTF-8
Narzędzia biblioteki Intel Video Processing Library zapewniają dostęp
do akcelerowanego dekodowania, kodowania i możliwości przetwarzania
ramek obrazu GPU firmy Intel z linii poleceń.

%package examples
Summary:	Example programs for Intel VPL library
Summary(pl.UTF-8):	Przykładowe programy do biblioteki Intel VPL
Group:		Libraries
Requires:	libvpl >= 2.11.0
Obsoletes:	oneVPL-examples < 2024

%description examples
Example programs for Intel VPL library.

%description examples -l pl.UTF-8
Przykładowe programy do biblioteki Intel VPL.

%prep
%setup -q
%patch0 -p1

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/vpl-tools/licensing

%clean
rm -rf $RPM_BUILD_ROOT

%post	examples -p /sbin/ldconfig
%postun	examples -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md SECURITY.md third-party-programs.txt
%attr(755,root,root) %{_bindir}/val-surface-sharing
%attr(755,root,root) %{_bindir}/vpl-import-export
%attr(755,root,root) %{_bindir}/vpl-inspect
%dir %{_libdir}/vpl-tools
%attr(755,root,root) %{_libdir}/vpl-tools/libvpl_wayland.so

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/metrics_monitor
%attr(755,root,root) %{_bindir}/sample_decode
%attr(755,root,root) %{_bindir}/sample_encode
%attr(755,root,root) %{_bindir}/sample_multi_transcode
%attr(755,root,root) %{_bindir}/sample_vpp
%attr(755,root,root) %{_bindir}/system_analyzer
%attr(755,root,root) %{_libdir}/libcttmetrics.so
