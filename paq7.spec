Summary:	File compressor and archiver
Name:		paq7
Version:	0
Release:	%mkrel 6
License:	GPL
Group:		Archiving/Compression
URL:		http://www2.cs.fit.edu/~mmahoney/compression/
Source0:	paq7asm.asm.bz2
Source1:	paq7.cpp.bz2
BuildRequires:	nasm
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PAQ7 is a file compressor and archiver.

%prep 

%setup -c -T

bzcat %{SOURCE0} > paq7asm.asm
bzcat %{SOURCE1} > paq7.cpp

%build

%ifarch %{ix86}
nasm -f elf paq7asm.asm
g++ paq7.cpp %{optflags} -s -o paq7 paq7asm.o
%endif

%ifarch x86_64
g++ paq7.cpp %{optflags} -DNOASM -s -o paq7
%endif

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 paq7 %{buildroot}%{_bindir}/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/paq7




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0-6mdv2010.0
+ Revision: 430236
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0-5mdv2009.0
+ Revision: 267986
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 0-2mdv2008.1
+ Revision: 171015
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0-1mdv2008.1
+ Revision: 136638
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0-1mdv2007.0
+ Revision: 115945
- Import paq7

* Fri Jan 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0-1mdk
- initial Mandriva package (for joeghi:))

