Summary:	APNG Assembler - create APNG animation from PNG/TGA image sequence
Summary(pl.UTF-8):	APNG Assembler - tworzenie animacji APNG z sekwencji obrazów PNG/TGA
Name:		apngasm
Version:	2.91
Release:	1
License:	Zlib (BSD-like)
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/apngasm/%{name}-%{version}-src.zip
# Source0-md5:	0f914350c4defc58c64c9341d9891b4f
URL:		http://apngasm.sourceforge.net/
BuildRequires:	advancecomp-7z-devel
BuildRequires:	libpng-devel >= 2:1.6.26
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel >= 1.2.8
BuildRequires:	zopfli-devel
Requires:	libpng >= 2:1.6.26
Requires:	zlib >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
APNG Assembler creates APNG animation from PNG/TGA image sequence.

%description -l pl.UTF-8
APNG Assembler tworzy animacje APNG z sekwencji obrazów PNG/TGA.

%prep
%setup -q -c

%build
%{__cxx} %{rpmldflags} %{rpmcxxflags} %{rpmcppflags} -Wall -o apngasm apngasm.cpp image.cpp \
	-DFEATURE_7ZIP -DFEATURE_ZOPFLI \
	-I/usr/include/adv7z \
	-lpng -ladv7z -lzopfli -lz -lm

%install
rm -rf $RPM_BUILD_ROOT

install -D apngasm $RPM_BUILD_ROOT%{_bindir}/apngasm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/apngasm
