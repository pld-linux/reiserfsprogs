Summary:	Utilities belonging to the Reiser filesystem
Summary(pl):	NarzЙdzia dla systemu plikСw Reiser
Summary(pt_BR):	Este pacote contИm os utilitАrios para manipulaГЦo do sistema de arquivos ReiserFS
Summary(uk):	Утил╕ти для роботы з файловою системою ReiserFS
Summary(ru):	Утилиты для работы с файловой системой ReiserFS
Name:		reiserfsprogs
Version:	3.6.9
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.namesys.com/pub/reiserfsprogs/%{name}-%{version}.tar.gz
# Source0-md5:	dce968da17b7ef4be77c831c3ae5c577
Patch0:		%{name}-acfix.patch
URL:		http://www.namesys.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	reiserfs-utils

%define		_sbindir	/sbin

%description
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms. The results when
compared to the ext2fs conventional block allocation based file system
running under the same operating system and employing the same
buffering code suggest that these algorithms are overall more
efficient, and are becoming more so every passing month. Loosely
speaking, every month we find another performance cranny that needs
work, and we fix it, and every month we find some way of improving our
overall general usage performance. The improvement in small file space
and time performance suggests that we may now revisit a common OS
design assumption that one should aggregate small objects using layers
above the file system layer. Being more effective at small files DOES
NOT make us less effective for other files, this is a general purpose
FS, and our overall traditional FS usage performance is high enough to
establish that. Reiserfs has a commitment to opening up the FS design
to contributions, and we are now now adding plug-ins so that you can
create your own types of directories and files.

%description -l pl
Pakiet zawiera programy do tworzenia (mkreiserfs), sprawdzania i
naprawiania bЁЙdСw (reiserfsck) oraz zmiany wielko╤ci
(resize_reiserfs) systemu plikСw ReiserFS.

%description -l pt_BR
Este pacote contИm os utilitАrios para manipulaГЦo do sistema de
arquivos ReiserFS.

%description -l ru
Набор утилит для работы с файловой системой ReiserFS.

%description -l uk
Наб╕р утил╕т для роботи з файловою системою ReiserFS.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make} LDFLAGS="%{rpmldflags}" all

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf reiserfsck $RPM_BUILD_ROOT%{_sbindir}/fsck.reiserfs
ln -sf mkreiserfs $RPM_BUILD_ROOT%{_sbindir}/mkfs.reiserfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
