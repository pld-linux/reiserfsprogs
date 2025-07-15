Summary:	Utilities belonging to the Reiser filesystem
Summary(pl.UTF-8):	Narzędzia dla systemu plików Reiser
Summary(pt_BR.UTF-8):	Este pacote contém os utilitários para manipulação do sistema de arquivos ReiserFS
Summary(uk.UTF-8):	Утиліти для роботы з файловою системою ReiserFS
Summary(ru.UTF-8):	Утилиты для работы с файловой системой ReiserFS
Name:		reiserfsprogs
Version:	3.6.27
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/System
#Source0:	http://www.kernel.org/pub/linux/utils/fs/reiserfs/%{name}-%{version}.tar.gz
Source0:	https://www.kernel.org/pub/linux/kernel/people/jeffm/reiserfsprogs/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	90c139542725efc6da3a6b1709695395
Patch0:		%{name}-am.patch
Patch1:		glibc.patch
URL:		https://reiser4.wiki.kernel.org/index.php/Reiserfsprogs
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	libcom_err-devel
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
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

%package libs
Summary:	ReiserFS Core library
Summary(pl.UTF-8):	Biblioteka ReiserFS Core
Group:		Libraries

%description libs
ReiserFS Core library.

%description libs -l pl.UTF-8
Biblioteka ReiserFS Core.

%package devel
Summary:	Header files for ReiserFS Core library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ReiserFS Core
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	libcom_err-devel

%description devel
Header files for ReiserFS Core library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ReiserFS Core.

%package static
Summary:	Static ReiserFS Core library
Summary(pl.UTF-8):	Biblioteka statyczna ReiserFS Core
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static ReiserFS Core library.

%description static -l pl.UTF-8
Biblioteka statyczna ReiserFS Core.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libreiserfscore.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README
%attr(755,root,root) %{_sbindir}/debugfs.reiserfs
%attr(755,root,root) %{_sbindir}/debugreiserfs
%attr(755,root,root) %{_sbindir}/fsck.reiserfs
%attr(755,root,root) %{_sbindir}/mkfs.reiserfs
%attr(755,root,root) %{_sbindir}/mkreiserfs
%attr(755,root,root) %{_sbindir}/reiserfsck
%attr(755,root,root) %{_sbindir}/reiserfstune
%attr(755,root,root) %{_sbindir}/resize_reiserfs
%attr(755,root,root) %{_sbindir}/tunefs.reiserfs
%{_mandir}/man8/debugfs.reiserfs.8*
%{_mandir}/man8/debugreiserfs.8*
%{_mandir}/man8/fsck.reiserfs.8*
%{_mandir}/man8/mkfs.reiserfs.8*
%{_mandir}/man8/mkreiserfs.8*
%{_mandir}/man8/reiserfsck.8*
%{_mandir}/man8/reiserfstune.8*
%{_mandir}/man8/resize_reiserfs.8*
%{_mandir}/man8/tunefs.reiserfs.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreiserfscore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libreiserfscore.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libreiserfscore.so
%{_includedir}/reiserfs
%{_pkgconfigdir}/reiserfscore.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libreiserfscore.a
