
%define plugin	imonlcd
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define snap	20091026
%define rel	2

Summary:	VDR plugin: Control an iMON LCD
Name:		%name
Version:	%version
%if %snap
Release:	%mkrel 1.%snap.%rel
%else
Release:	%mkrel %rel
%endif
Group:		Video
License:	GPLv3
URL:		http://projects.vdr-developer.org/wiki/plg-imonlcd
%if %snap
# rm -rf vdr-plugin-imonlcd
# git clone git://community.xeatre.tv/vdr-plugin-imonlcd.git
# cd vdr-plugin-imonlcd
# git archive --prefix=imonlcd-$(date +%Y%m%d)/ --format=tar HEAD | bzip2 > ../vdr-imonlcd-$(date +%Y%m%d).tar.bz2
Source:		vdr-%plugin-%snap.tar.bz2
%else
Source:		vdr-%plugin-%version.tgz
%endif
# includes fontconfig.h but does not use it:
Patch0:		imonlcd-drop-extra-include.patch
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	pkgconfig(freetype2)
Requires:	vdr-abi = %vdr_abi
Requires:	kmod(lirc_imon)

%description
A Video Disk Recorder plugin that shows information about the
current state of VDR on an iMON LCD screen.

%prep
%if %snap
%setup -q -n %plugin-%snap
%else
%setup -q -n %plugin-%version
%endif
%patch0 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# Sets the lcd-device to other device than /dev/lcd0
var=LCD_DEVICE
param="-d LCD_DEVICE"
# sets the protocol of lcd-device:
# '0038'	For LCD with ID 15c2:0038 SoundGraph Inc (default)
# 'ffdc'	For LCD with ID 15c2:ffdc SoundGraph Inc
var=PROTOCOL
param="-p PROTOCOL"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


%changelog
* Mon Oct 26 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-1.20091026.1mdv2010.1
+ Revision: 459413
- do not include unused fontconfig header (drop-extra-include.patch)
- initial Mandriva release

