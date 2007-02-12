Summary:	XFree86 Programmers documentation
Summary(pl.UTF-8):   XFree86 - dokumentacja dla programistów
Name:		XFree86-doc
Version:	4.4.0
Release:	1
License:	MIT
Group:		Documentation
# XFree86-%{version}-src-6.tgz contains docs in other formats
Source0:	ftp://ftp.xfree86.org/pub/XFree86/%{version}/source/XFree86-%{version}-src-7.tgz
# Source0-md5:	947a34279a0ca2da2f300719c583845e
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Basic programmers documentation, many information about X-Window
programming. In compressed PostScript format.

%description -l pl.UTF-8
Pakiet zawiera większość informacji niezbędnych to rozpoczęcia
programowania aplikacji X Window. Format: skompresowany PostScript.

%prep
%setup -q -c

find . -name Imakefile | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc xc/doc/hardcopy/*
