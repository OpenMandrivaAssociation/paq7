Summary:	File compressor and archiver
Name:		paq7
Version:	0
Release:	%mkrel 7
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


