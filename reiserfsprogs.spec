Summary:	Utilities belonging to the Reiser filesystem
Name:		reiserfsprogs
Version:	3.x.0h
Release:	1
Copyright:	2001 Hans Reiser
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.reiserfs.org/reiserfsprogs/%{name}-%{version}.tar.gz
Obsoletes:	reiserfs-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The reiserfsprogs package contains programs for creating (mkreiserfs),
checking and correcting any inconsistencies (reiserfsck) and resizing
(resize_reiserfs) of a reiserfs filesystem.

%prep
%setup -q

%build
%configure \
	--sbindir=/sbin

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln $RPM_BUILD_ROOT/sbin/reiserfsck $RPM_BUILD_ROOT/sbin/fsck.reiserfs
ln $RPM_BUILD_ROOT/sbin/mkreiserfs $RPM_BUILD_ROOT/sbin/mkfs.reiserfs

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755, root, root) /sbin/*
%{_mandir}/man8/*
