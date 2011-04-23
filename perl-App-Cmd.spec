%define upstream_name    App-Cmd
%define upstream_version 0.311

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    "app cmd --subcmd" style subdispatching
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Class::Load)
BuildRequires: perl(Getopt::Long::Descriptive)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(IO::TieCombine)
BuildRequires: perl(String::RewritePrefix)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More) >= 0.960.0

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(IO::TieCombine)

%description
App::Cmd is intended to make it easy to write complex command-line
applications without having to think about most of the annoying things
usually involved.

For information on how to start using App::Cmd, see App::Cmd::Tutorial.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
