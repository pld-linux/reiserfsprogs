Summary:	Utilities belonging to the Reiser filesystem
Summary(pl):	Narzêdzia dla systemu plików Reiser
Summary(pt_BR):	Este pacote contém os utilitários para manipulação do sistema de arquivos ReiserFS
Name:		reiserfsprogs
Version:	3.x.0j
Release:	4
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.reiserfs.org/pub/reiserfsprogs/%{name}-%{version}.tar.gz
Patch0:		%{name}-mkstemp.patch
Patch1:		%{name}-endian-safe.patch
URL:		http://www.reiserfs.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%if %{?BOOT:1}%{!?BOOT:0}
BuildRequires:	glibc-static
%endif
Obsoletes:	reiserfs-utils

%define		_sbindir	/sbin

%description
The reiserfsprogs package contains programs for creating (mkreiserfs),
checking and correcting any inconsistencies (reiserfsck) and resizing
(resize_reiserfs) of a reiserfs filesystem.

%description -l pl
Pakiet zawiera programy do tworzenia (mkreiserfs), sprawdzania i
naprawiania b³êdów (reiserfsck) oraz zmiany wielko¶ci
(resize_reiserfs) systemu plików ReiserFS.

%description -l pt_BR
Este pacote contém os utilitários para manipulação do sistema de
arquivos ReiserFS.

%package BOOT
Summary:	%{name} for bootdisk
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System

%description BOOT
%{name} for bootdisk.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%if %{?BOOT:1}%{!?BOOT:0}
%configure
%{__make} LDFLAGS="-static -s"
mv -f mkreiserfs/mkreiserfs mkreiserfs-BOOT
%{__make} distclean
%endif

%configure
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_sbindir}
for i in *-BOOT; do
install $i $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_sbindir}/`basename $i -BOOT`
done
%endif

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s reiserfsck $RPM_BUILD_ROOT%{_sbindir}/fsck.reiserfs
ln -s mkreiserfs $RPM_BUILD_ROOT%{_sbindir}/mkfs.reiserfs

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bootdisk%{_sbindir}/*
%endif
