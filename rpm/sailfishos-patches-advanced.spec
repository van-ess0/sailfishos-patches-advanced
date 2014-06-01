# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-patches-advanced

# >> macros
BuildArch: noarch
# << macros

Summary:    A set of advanced patches
Version:    0.0
Release:    1
Group:      Qt/Qt
License:    TODO
URL:        https://github.com/sailfishos-patches/sailfishos-patches-advanced
Source0:    %{name}-%{version}.tar.bz2
Source100:  sailfishos-patches-advanced.yaml
Requires:   patchmanager

%description
This package contains a set of advanced that might
require extra care when being applied.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager
for f in $(ls maintained); do
cp -r maintained/$f %{buildroot}/usr/share/patchmanager/adv-$f
done
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/adv-*
# >> files
# << files
