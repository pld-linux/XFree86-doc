Summary:	XFree86 Programmers documentation
Summary(pl):	XFree86 Dokumentacja dla programistów
Name:		XFree86-doc
Version:	4.0.1
Release:	1
License:	MIT
Group:		X11/XFree86
Group(pl):	X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/%{version}/source/X401src-3.tgz
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Basic programmers documentation, many information about X-Window
programming. In compressed PostScript format.

%description -l pl
Pakiet zawiera wiêkszo¶æ informacji niezbêdnych to rozpoczêcia
programowania apliakcji X Window. Format: skompresowany PostScript.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/
cd xc/doc/hardcopy
find . -name \*.PS -exec gzip -9nf {} \;
find . -name \*.txt -exec gzip -9nf {} \;
cp -ar * $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

%clean

%files
%defattr(644,root,root,755)
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/*
