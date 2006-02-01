#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Session
Summary:	Catalyst::Plugin::Session - Generic Catalyst session plugin
Summary(pl):	Catalyst::Plugin::Session - ogólna wtyczka sesji dla Catalysta
Name:		perl-Catalyst-Plugin-Session
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f5b5ed59820e7b7dbf13b364e96fed5d
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Session/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.49
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-MockObject >= 1.01
BuildRequires:	perl-Object-Signature
BuildRequires:	perl-Test-Exception
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

%description -l pl
Wtyczka Session to podstawa dwóch powi±zanych czê¶ci funkcjonalno¶ci
wymaganej do zarz±dzania sesjami w aplikacjach WWW.

Pierwsza czê¶æ to obs³uga stanów (State) powoduj±ca, ¿e przegl±darka
powtarza klucz sesji, dziêki czemu aplikacja WWW mo¿e zidentyfikowaæ
klienta i logicznie ³±czyæ ze sob± kilka ¿±dañ w sesjê.

Druga czê¶æ to przechowywanie danych (Store) odpowiadaj±ce za w³a¶ciwe
przechowywanie informacji o kliencie. Te dane s± przechowywane w taki
sposób, ¿e mog± byæ odtworzone przy ka¿dym ¿±daniu wykonanym przez
tego samego klienta.

Ta wtyczka ³±czy te dwa elementy w ca³o¶æ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{perl_vendorlib}/Catalyst/Plugin/Session
%{_mandir}/man3/*
