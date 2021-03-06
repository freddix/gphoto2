Summary:	Command-line frontend to libgphoto2
Name:		gphoto2
Version:	2.5.4
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5:	55e062dfb09a9589b4f9d6d545724c60
URL:		http://www.gphoto.org/
BuildRequires:	libexif-devel
BuildRequires:	libgphoto2-devel >= 2.5.4
BuildRequires:	libjpeg-devel
BuildRequires:	pkg-config
BuildRequires:	popt-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gphoto2 is a command-line frontend to libgphoto2.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gphoto2
%{_mandir}/man1/*

