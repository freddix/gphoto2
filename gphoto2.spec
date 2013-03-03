Summary:	Command-line frontend to libgphoto2
Name:		gphoto2
Version:	2.5.1
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5:	03cda6d5b7c647ac4c90d0081f2cb7c7
URL:		http://www.gphoto.org/
BuildRequires:	libexif-devel
BuildRequires:	libgphoto2-devel >= 2.5.1
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

