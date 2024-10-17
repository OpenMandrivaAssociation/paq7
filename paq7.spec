Summary:	File compressor and archiver
Name:		paq7
Version:	0
Release:	8
License:	GPL
Group:		Archiving/Compression
URL:		https://www2.cs.fit.edu/~mmahoney/compression/
Source0:	paq7asm.asm.bz2
Source1:	paq7.cpp.bz2
BuildRequires:	nasm

%define debug_package %{nil}

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
install -d %{buildroot}%{_bindir}
install -m0755 paq7 %{buildroot}%{_bindir}/

%files
%attr(0755,root,root) %{_bindir}/paq7
