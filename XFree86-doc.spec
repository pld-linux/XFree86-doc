
%define		_sver %(echo %{version} | tr -d .)

Summary:	XFree86 Programmers documentation
Summary(pl):	XFree86 - dokumentacja dla programistów
Name:		XFree86-doc
Version:	4.3.0
Release:	1
License:	MIT
Group:		X11/XFree86
# X%{_sver}src-6.tgz contains docs in other formats
Source0:	ftp://ftp.xfree86.org/pub/XFree86/%{version}/source/X%{_sver}src-7.tgz
# Source0-md5:	e002e70f24098ca4f62fabd1c2809ed1
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Basic programmers documentation, many information about X-Window
programming. In compressed PostScript format.

%description -l pl
Pakiet zawiera wiêkszo¶æ informacji niezbêdnych to rozpoczêcia
programowania aplikacji X Window. Format: skompresowany PostScript.

%prep
%setup -q -c

find . -name Imakefile | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc xc/doc/hardcopy/*
