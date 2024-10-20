%{?_javapackages_macros:%_javapackages_macros}
Name:             weld-parent
Version:          26
Release:          1.1%{?dist}
Summary:          Parent POM for Weld

License:          ASL 2.0
URL:              https://seamframework.org/Weld

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

%changelog
* Tue Oct 22 2013 Marek Goldmann <mgoldman@redhat.com> - 26-1
- Upstream release 26

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Michal Srb <msrb@redhat.com> - 17-8
- Add ASL 2.0 license text
- Add missing BR: maven-plugin-build-helper, maven-install-plugin

* Tue Feb 19 2013 Marek Goldmann <mgoldman@redhat.com> - 17-7
- Added maven-shared BR

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 17-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Jul 23 2012 Marek Goldmann <mgoldman@redhat.com> - 17-4
- Fixed BR, removed maven plugins from R

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Marek Goldmann <mgoldman@redhat.com> 17-2
- Added build section

* Wed Mar 14 2012 Marek Goldmann <mgoldman@redhat.com> 17-1
- Initial packaging

