%define upstream_name    App-Cmd
%define upstream_version 0.319
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.319
Release:	2

Summary:	"app cmd --subcmd" style subdispatching
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/App/App-Cmd-0.319.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Load)
BuildRequires:	perl(Getopt::Long::Descriptive)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(IO::TieCombine)
BuildRequires:	perl(String::RewritePrefix)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Test::More) >= 0.960.0

BuildArch: noarch

Requires:	perl(IO::TieCombine)

%description
App::Cmd is intended to make it easy to write complex command-line
applications without having to think about most of the annoying things
usually involved.

For information on how to start using App::Cmd, see App::Cmd::Tutorial.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.311.0-2mdv2011.0
+ Revision: 657382
- rebuild for updated spec-helper

* Sat Mar 19 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.311.0-1
+ Revision: 646930
- update to new version 0.311

* Thu Dec 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 622418
- update to new version 0.310

* Sun Nov 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.309.0-1mdv2011.0
+ Revision: 597484
- adding missing buildrequires:
- update to 0.309

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.308

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.307.0-2mdv2011.0
+ Revision: 561924
- adding missing requires:

* Tue Mar 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.307.0-1mdv2011.0
+ Revision: 517120
- adding missing buildrequires:
- update to 0.307
- update to 0.306

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.304.0-1mdv2010.1
+ Revision: 474731
- update to 0.304

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.303.0-1mdv2010.1
+ Revision: 471064
- update to 0.303

* Thu Sep 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.301.0-1mdv2010.0
+ Revision: 427476
- update to 0.301

* Sat Aug 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 422079
- update to 0.300

* Fri Aug 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.207.0-1mdv2010.0
+ Revision: 421835
- update to 0.207
- update to 0.207

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.206.0-1mdv2010.0
+ Revision: 418407
- update to 0.206

* Mon Jun 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.204.0-1mdv2010.0
+ Revision: 390519
- update to new version 0.204

* Sat Jun 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.203.0-1mdv2010.0
+ Revision: 383326
- updating buildrequires:
- updating buildrequires:
- adding missing buildrequires:
- import perl-App-Cmd


* Fri May 29 2009 cpan2dist 0.203-1mdv
- initial mdv release, generated with cpan2dist


