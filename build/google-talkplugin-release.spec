Name:       google-talkplugin-release
Version:    1.0
Release:    3%{?dist}
Summary:    Google talkplugin repository configuration

Group:      System Environment/Base
License:    BSD
URL:        http://www.google.com/chat/video
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch

%description
Google talkplugin repository configuration.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 google-talkplugin.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY-google-talkplugin $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-google-talkplugin
%config(noreplace) /etc/yum.repos.d/google-talkplugin.repo

%changelog
* Sat Sep 7 2013 Chris Smart <csmart@kororaproject.org> - 1.0-3
- Disable repo by default so that users can just enable the repo to make it work

* Fri Nov 02 2012 Chris Smart <csmart@kororaproject.org> - 1.0-2
- Fix error in spec file, and set repo as noreplace config.

* Mon Dec 26 2011 Chris Smart <chris@kororaa.org> - 1.0-1
- Initial package.
