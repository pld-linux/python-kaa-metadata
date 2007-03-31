%define 	module	kaa-metadata

Summary:	Media metadata for Python
Summary(pl.UTF-8):	Metadane multimedialne dla Pythona
Name:		python-%{module}
Version:	0.6.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/freevo/%{module}-%{version}.tar.gz
# Source0-md5:	0df903aa873bdc1ce8ed0e8aa0b81e98
URL:		http://www.freevo.org/kaa/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-kaa-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module for retrieving information about media files.

%description -l pl.UTF-8
Moduł do uzyskiwania informacji o plikach multimedialnych.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# in python-mmpython package
# %attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.egg-info
%dir %{py_sitedir}/kaa/metadata
%attr(755,root,root) %{py_sitedir}/kaa/metadata/*.py[co]
%dir %{py_sitedir}/kaa/metadata/audio
%{py_sitedir}/kaa/metadata/audio/*.py[co]
%dir %{py_sitedir}/kaa/metadata/audio/eyeD3
%{py_sitedir}/kaa/metadata/audio/eyeD3/*.py[co]
%dir %{py_sitedir}/kaa/metadata/disc
%{py_sitedir}/kaa/metadata/disc/*.py[co]
%attr(755,root,root) %{py_sitedir}/kaa/metadata/disc/*.so
%dir %{py_sitedir}/kaa/metadata/games
%{py_sitedir}/kaa/metadata/games/*.py[co]
%dir %{py_sitedir}/kaa/metadata/image
%{py_sitedir}/kaa/metadata/image/*.py[co]
%dir %{py_sitedir}/kaa/metadata/misc
%{py_sitedir}/kaa/metadata/misc/*.py[co]
%dir %{py_sitedir}/kaa/metadata/video
%{py_sitedir}/kaa/metadata/video/*.py[co]
