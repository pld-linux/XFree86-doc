Summary:	XFree86 Programmers documentation
Summary(pl):	XFree86 Dokumentacja dla programistów
Name:		XFree86-doc
Version:	3.3.3.1
Release:	54
Copyright:	GPL
Group:		X11/XFree86
Group(pl):	X11/XFree86
Source:		ftp://ftp.xfree86.org/pub/XFree86/3.3.3/source/X333src-3.tgz
Buildarch:	noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Basic programmers documentation, many information about X-Window programming.
In compressed PostScript format.

%description -l pl
Pakiet zawiera większość informacji niezbędnych to rozpoczęcia programowania _pod_ X-y. 
Format: skompresowany PostScript

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/
cd xc/doc/hardcopy
find . -name \*.Z -exec compress -d {} \;
find . -type f -exec gzip -9nf {} \;
cp -ar * $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

%clean

%files
%defattr(644,root,root,755)
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/*

%changelog
* Wed Jun 23 1999 Jan Rękorajski <baggins@pld.org.pl>
  [3.3.3.1-54]
- FHS 2.0

* Fri Dec 11 1998 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [3.3.3-1]
- added gzipping all docs,
- /usr/doc/%%{name}-%%{version} marked as %docdir,
- added "Autoreqprov: no",
- "cp -ar" instead tar in %nstall.

* Thu Dec 03 1998 Wojciech "Sas" Cięciwa <cieciwa@alpha.zarz.agh.edu.pl>
- separate documetation from main package.

* Tue Dec 01 1998 Wojciech "Sas" Cięciwa <cieciwa@alpha.zarz.agh.edu.pl>
- building RPM.
