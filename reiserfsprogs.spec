Summary:	Utilities belonging to the Reiser filesystem
Summary(pl.UTF-8):	Narzędzia dla systemu plików Reiser
Summary(pt_BR.UTF-8):	Este pacote contém os utilitários para manipulação do sistema de arquivos ReiserFS
Summary(uk.UTF-8):	Утиліти для роботы з файловою системою ReiserFS
Summary(ru.UTF-8):	Утилиты для работы с файловой системой ReiserFS
Name:		reiserfsprogs
Version:	3.6.20
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.namesys.com/pub/reiserfsprogs/%{name}-%{version}.tar.gz
# Source0-md5:	3b3392f59c5d302cf858bc4cf194b258
Patch0:		%{name}-bigendian-fix.patch
URL:		http://www.namesys.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libuuid-devel
Obsoletes:	reiserfs-utils
Conflicts:	progsreiserfs < 0.3.1-1.rc8.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
Pakiet zawiera programy do tworzenia (mkreiserfs), sprawdzania i
naprawiania błędów (reiserfsck) oraz zmiany wielkości
(resize_reiserfs) systemu plików ReiserFS.

%description -l pt_BR.UTF-8
Este pacote contém os utilitários para manipulação do sistema de
arquivos ReiserFS.

%description -l ru.UTF-8
Набор утилит для работы с файловой системой ReiserFS.

%description -l uk.UTF-8
Набір утиліт для роботи з файловою системою ReiserFS.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%ifarch alpha ppc ppc64 sparc sparcv9 sparc64
	ac_cv_header_asm_unaligned=no
%endif

%{__make} all \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf reiserfsck $RPM_BUILD_ROOT%{_sbindir}/fsck.reiserfs
ln -sf mkreiserfs $RPM_BUILD_ROOT%{_sbindir}/mkfs.reiserfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
