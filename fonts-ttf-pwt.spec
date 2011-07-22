%define pkgname pwtfont

Summary: Fonts to replace commonly used Microsoft Windows Fonts
Name: fonts-ttf-pwt
Version: 0.5
Release: %mkrel 1
License: open
Group: System/Fonts/True type
URL: http://www.pingwinsoft.ru/system/uploads/7/original/fonts_test.zip?1276003553
Source0: %{pkgname}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: freetype-tools

%description
The PingWin Typography (PWT) fonts are intended to be replacements for most 
commonly used fonts on Microsoft systems: Tahoma, Arial, Courier, Verdana, Times New Roman

%prep
%setup -q -n %{pkgname}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/pwt

install -m 644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/pwt
ttmkfdir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/pwt > $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/pwt/fonts.dir
ln -s fonts.dir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/pwt/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/pwt \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-pwt:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi


%files
%defattr(-,root,root,-)
%doc License.txt 
#COPYING
%dir %{_datadir}/fonts/TTF/pwt
%{_datadir}/fonts/TTF/pwt/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/pwt/fonts.dir
%{_datadir}/fonts/TTF/pwt/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-pwt:pri=50

