Summary:	Utilities belonging to the Reiser filesystem
Summary(pl):	Narzêdzia dla systemu plików Reiser
Name:		reiserfsprogs
Version:	3.x.0j
Release:	1
Copyright:	2001 Hans Reiser
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.reiserfs.org/pub/reiserfsprogs/%{name}-%{version}.tar.gz
URL:		http://www.reiserfs.org/
Obsoletes:	reiserfs-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
The reiserfsprogs package contains programs for creating (mkreiserfs),
checking and correcting any inconsistencies (reiserfsck) and resizing
(resize_reiserfs) of a reiserfs filesystem.

%description -l pl
Pakiet zawiera programy do tworzenia (mkreiserfs), sprawdzania i
naprawiania b³êdów (reiserfsck) oraz zmiany wielko¶ci
(resize_reiserfs) systemu plików ReiserFS.

%prep
%setup -q

%build
%configure

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln $RPM_BUILD_ROOT%{_sbindir}/reiserfsck $RPM_BUILD_ROOT%{_sbindir}/fsck.reiserfs
ln $RPM_BUILD_ROOT%{_sbindir}/mkreiserfs $RPM_BUILD_ROOT%{_sbindir}/mkfs.reiserfs

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755, root, root) %{_sbindir}
%{_mandir}/man*/*
