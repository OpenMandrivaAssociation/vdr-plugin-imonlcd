%define plugin	imonlcd
%define snap	0

Summary:	VDR plugin: Control an iMON LCD
Name:		vdr-plugin-%plugin
Version:	1.0.1
%if %snap
Release:	1.%snap.1
%else
Release:	1
%endif
Group:		Video
License:	GPLv3
URL:		http://projects.vdr-developer.org/projects/plg-imonlcd
%if %snap
# rm -rf vdr-plugin-imonlcd
# git clone git://community.xeatre.tv/vdr-plugin-imonlcd.git
# cd vdr-plugin-imonlcd
# git archive --prefix=imonlcd-$(date +%Y%m%d)/ --format=tar HEAD | bzip2 > ../vdr-imonlcd-$(date +%Y%m%d).tar.bz2
Source:		vdr-%plugin-%snap.tar.bz2
%else
Source:		vdr-%plugin-%{version}.tgz
%endif
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	pkgconfig(freetype2)
Requires:	vdr-abi = %vdr_abi

%description
A Video Disk Recorder plugin that shows information about the
current state of VDR on an iMON LCD screen.

%prep
%if %snap
%setup -q -n %plugin-%snap
%else
%setup -q -n %plugin-%{version}
%endif
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
%doc README HISTORY
