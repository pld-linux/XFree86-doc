Summary:     XFree86 Programmers documentation
Summary(pl): XFree86 Dokumentacja dla programistów
Name:        XFree86-doc
Version:     3.3.3
Release:     1
Copyright:   GPL
Group:       X11
Source:      ftp://ftp.xfree86.org/pub/XFree86/3.3.3/source/X333src-3.tgz
Buildarch:   noarch
Autoreqprov: no
Buildroot:   /tmp/%{name}-%{version}-root

%description
Basic programmers documentation, many information about X-Window programming.
In compressed PostScript format.

%description -l pl
Pakiet zawiera wiêkszo¶æ informacji niezbêdnych to rozpoczêcia programowania
_pod_ X-y. 
Format: skompresowany PostScript

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}/
cd xc/doc/hardcopy
find . -name \*.Z -exec compress -d {} \;
find . -type f -exec gzip -9nf {} \;
cp -ar * $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}

%clean

%files
%defattr(644, root, root, 755)
%docdir /usr/doc/%{name}-%{version}

%changelog
* Fri Dec 11 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.3.3-1]
- added gzipping all docs,
- /usr/doc/%%{name}-%%{version} marked as %docdir,
- added "Autoreqprov: no",
- "cp -ar" instead tar in %nstall.

* Thu Dec 03 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- separate documetation from main package.

* Tue Dec 01 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- building RPM.
