Summary:	I/O on in-core objects like strings and arrays for Perl
Name:		perl-IO-stringy
Version:	2.110
Release:	10.1%{?dist}
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/IO-stringy/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DS/DSKOLL/IO-stringy-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl(ExtUtils::MakeMaker)

%description
This toolkit primarily provides Perl modules for performing both
traditional and object-oriented I/O) on things *other* than normal
filehandles; in particular, IO::Scalar, IO::ScalarArray, and IO::Lines.

%prep
%setup -q -n IO-stringy-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}
/usr/bin/find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
/usr/bin/find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{__chmod} -R u+w %{buildroot}/*

%check
%{__make} test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING examples
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::*.3pm*

%changelog
* Wed Dec 09 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.110-10.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.110-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.110-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.110-8
- Rebuild for perl 5.10 (again)

* Tue Jan 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.110-7
- rebuild for new perl

* Mon Aug 13 2007 Paul Howarth <paul@city-fan.org> 2.110-6
- clarify license as GPL v1 or later, or Artistic (same as perl)

* Wed Apr 18 2007 Paul Howarth <paul@city-fan.org> 2.110-5
- buildrequire perl(ExtUtils::MakeMaker)

* Sun Sep 17 2006 Paul Howarth <paul@city-fan.org> 2.110-4
- add dist tag
- fix argument order in find command with -depth

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 2.110-3
- use search.cpan.org download URL
- use full paths for all commands used in build
- assume rpm knows about %%check and %%{perl_vendorlib}
- cosmetic spec file changes

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Feb 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:2.110-1
- 2.110.
- Some specfile cleanups, bringing it closer to spectemplate-perl.spec.

* Wed Dec 31 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.109-0.fdr.1
- Update to 2.109.

* Thu Oct  2 2003 Michael Schwendt <rh0212ms[AT]arcor.de> 0:2.108-0.fdr.4
- Package is now using vendor directories

* Sat Aug 16 2003 Dams <anvil[AT]livna.org> 0:2.108-0.fdr.3
- Package is now noarch
- rm-ing perllocal.pod instead of excluding it

* Fri Jul 11 2003 Dams <anvil[AT]livna.org> 0:2.108-0.fdr.2
- Changed Group tag value
- "make test" in build section
- Added missing directory

* Sun Jun 15 2003 Dams <anvil[AT]livna.org>
- Initial build.
