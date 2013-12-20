%_javapackages_macros
Name:             weld-parent
Version:          26
Release:          2.0%{?dist}
Summary:          Parent POM for Weld

License:          ASL 2.0
URL:              http://seamframework.org/Weld

Source0:          http://repo1.maven.org/maven2/org/jboss/weld/%{name}/%{version}/%{name}-%{version}.pom
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-shared
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-build-helper
BuildRequires:    maven-install-plugin

%description
Parent POM for Weld

%prep
cp %{SOURCE0} pom.xml
cp %{SOURCE1} LICENSE

%pom_remove_plugin ":maven-remote-resources-plugin"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
