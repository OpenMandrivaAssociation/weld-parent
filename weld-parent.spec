Name:             weld-parent
Version:          61
Release:          1
Summary:          Parent POM for Weld

License:          ASL 2.0
URL:              https://github.com/weld/parent

Source0:          https://github.com/weld/parent/archive/refs/tags/%{version}.tar.gz

BuildArch:        noarch
BuildSystem:	maven
BuildOption:	validate

%description
Parent POM for Weld

%prep
%setup -q -n parent-%{version}

%files -f .mfiles
%doc LICENSE
