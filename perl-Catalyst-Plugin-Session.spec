#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Session
Summary:	Catalyst::Plugin::Session - Generic Catalyst session plugin
Summary(pl.UTF-8):   Catalyst::Plugin::Session - ogólna wtyczka sesji dla Catalysta
Name:		perl-Catalyst-Plugin-Session
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2d0560b93df902ce0d27d97701f4e31a
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Session/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.49
BuildRequires:	perl-Object-Signature
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-MockObject >= 1.01
# Not packaged
# BuildRequires:	perl-Test-WWW-Mechanize-Catalyst
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Session plugin is the base of two related parts of functionality
required for session management in web applications.

The first part, the State, is getting the browser to repeat back a
session key, so that the web application can identify the client and
logically string several requests together into a session.

The second part, the Store, deals with the actual storage of
information about the client. This data is stored so that the it may
be revived for every request made by the same client.

This plugin links the two pieces together.

%description -l pl.UTF-8
Wtyczka Session to podstawa dwóch powiązanych części funkcjonalności
wymaganej do zarządzania sesjami w aplikacjach WWW.

Pierwsza część to obsługa stanów (State) powodująca, że przeglądarka
powtarza klucz sesji, dzięki czemu aplikacja WWW może zidentyfikować
klienta i logicznie łączyć ze sobą kilka żądań w sesję.

Druga część to przechowywanie danych (Store) odpowiadające za właściwe
przechowywanie informacji o kliencie. Te dane są przechowywane w taki
sposób, że mogą być odtworzone przy każdym żądaniu wykonanym przez
tego samego klienta.

Ta wtyczka łączy te dwa elementy w całość.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Catalyst/Plugin/Session/State

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes TODO
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{perl_vendorlib}/Catalyst/Plugin/Session
%{_mandir}/man3/*
