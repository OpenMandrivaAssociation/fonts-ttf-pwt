%define pkgname pwtfont

Summary: Fonts to replace commonly used Microsoft Windows Fonts
Name: fonts-ttf-pwt
Version: 0.5
Release: 3
License: open
Group: System/Fonts/True type
URL: https://www.pingwinsoft.ru/system/uploads/7/original/fonts_test.zip?1276003553
Source0: %{pkgname}.tar.bz2
BuildArch: noarch
BuildRequires: freetype-tools

%description
The PingWin Typography (PWT) fonts are intended to be replacements for most 
commonly used fonts on Microsoft systems: Tahoma, Arial, Courier, Verdana,
Times New Roman

%prep
%setup -q -n %{pkgname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/pwt

install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/pwt
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/pwt > %{buildroot}%{_datadir}/fonts/TTF/pwt/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/pwt/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/pwt \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-pwt:pri=50

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



%changelog
* Mon Oct 10 2011 Александр Казанцев <kazancas@mandriva.org> 0.5-1edm2012.0
+ Revision: 704075
- imported package fonts-ttf-pwt

  + Sergey Zhemoitel <serg@mandriva.org>
    - imported package fonts-ttf-pwt


* Thu Jun 17 2010 Alexander Kazancev <kazancas@mandriva.ru>
- Initial build.
