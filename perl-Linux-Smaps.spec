#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Linux
%define	pnam	Smaps
Summary:	Linux::Smaps - a Perl interface to /proc/PID/smaps
Summary(pl.UTF-8):	Linux::Smaps - perlowy interfejs do /proc/PID/smaps
Name:		perl-Linux-Smaps
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/O/OP/OPI/Linux-Smaps-%{version}.tar.gz
# Source0-md5:	d8a3abec9265a0e583844dc7952e9134
URL:		http://search.cpan.org/~opi/Linux-Smaps/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::Member) >= 1.3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The /proc/PID/smaps files in modern linuxes provides very detailed
information about a processes memory consumption. It particularly
includes a way to estimate the effect of copy-on-write.
This module implements a Perl interface.

%description -l pl.UTF-8
Pliki /proc/PID/smaps w nowych linuksach dostarczają bardzo
szczegółowych informacji dotyczących zyżycia pamięci przez
procesy.
Ten moduł dostarcza interfejs perlowy do tych plików.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Linux/*.pm
%{_mandir}/man3/*
