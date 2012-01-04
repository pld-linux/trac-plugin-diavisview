%define		trac_ver	0.11
%define		plugin		diavisview
Summary:	Automaticaly creates a bitmap render of Dia MS Visio diagrams
Name:		trac-plugin-%{plugin}
Version:	8100
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/diavisviewplugin?old_path=/&format=zip#/%{plugin}-%{version}.zip
# Source0-md5:	94e5f8bbf40d9163956317af6e176230
URL:		http://trac-hacks.org/wiki/DiaVisViewPlugin
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
# if 0.12 cames into play, can simplify this
Requires:	trac >= %{trac_ver}.7-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin automatically creates a bitmapped render of Dia and MS Visio VDX 
diagrams when attaching them to objects in Trac.

This has taken the original DiaViewPlugin and modified it for use with Trac 
0.11, and at the same time included support for vdx and compressed files.
It has had very little testing. It has been set up as a separate hack to the 
original DiaViewPlugin so as not to break DiaViewPlugin for Trac &lt; 0.11.

If the width was changed in the macro argument the displayed image would 
scale, however the source file stayed the same. To overcome this the width 
is checked using the image library, and if different it is re-rendered. 

Please see the link below for the image library.
http://www.pythonware.com/products/pil/ 


%prep
%setup -qc
mv %{plugin}plugin/%{trac_ver}/* .

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT
	
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*
