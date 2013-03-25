Summary:	Utilities belonging to the Reiser filesystem
Summary(pl.UTF-8):	Narzędzia dla systemu plików Reiser
Summary(pt_BR.UTF-8):	Este pacote contém os utilitários para manipulação do sistema de arquivos ReiserFS
Summary(uk.UTF-8):	Утиліти для роботы з файловою системою ReiserFS
Summary(ru.UTF-8):	Утилиты для работы с файловой системой ReiserFS
Name:		reiserfsprogs
Version:	3.6.22
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/System
#Source0:	http://www.kernel.org/pub/linux/utils/fs/reiserfs/%{name}-%{version}.tar.gz
Source0:	https://www.kernel.org/pub/linux/kernel/people/jeffm/reiserfsprogs/v%{version}/%{name}-%{version}.tar.xz
Patch0:		%{name}-am.patch
# Source0-md5:	91d2fdb5eeaa15c8afcc9e815179690d
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libuuid-devel
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

# hack, otherwise configure failed
sed -i -e 's#AM_ENABLE_SHARED##g' configure.in

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README
%attr(755,root,root) %{_sbindir}/debugreiserfs
%attr(755,root,root) %{_sbindir}/fsck.reiserfs
%attr(755,root,root) %{_sbindir}/mkfs.reiserfs
%attr(755,root,root) %{_sbindir}/mkreiserfs
%attr(755,root,root) %{_sbindir}/reiserfsck
%attr(755,root,root) %{_sbindir}/reiserfstune
%attr(755,root,root) %{_sbindir}/resize_reiserfs
%{_mandir}/man8/debugreiserfs.8*
%{_mandir}/man8/mkreiserfs.8*
%{_mandir}/man8/reiserfsck.8*
%{_mandir}/man8/reiserfstune.8*
%{_mandir}/man8/resize_reiserfs.8*
