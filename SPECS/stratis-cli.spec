Name:           stratis-cli
Version:        3.4.1
Release:        1%{?dist}
Summary:        Command-line tool for interacting with the Stratis daemon

License:        ASL 2.0
URL:            https://github.com/stratis-storage/stratis-cli
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{_bindir}/a2x
# It runs without, but totally useless
Requires:       (stratisd >= 3.4.0 with stratisd < 4.0.0)

# stratisd only available on certain arches
ExclusiveArch:  %{rust_arches} noarch
%if 0%{?rhel} && !0%{?eln}
ExcludeArch:    i686
%endif
BuildArch:      noarch

%description
stratis provides a command-line interface (CLI) for
interacting with the Stratis daemon, stratisd. stratis
interacts with stratisd via D-Bus.

%prep
%autosetup

%build
%py3_build
a2x -f manpage docs/stratis.txt

%install
%py3_install
# Do not install tab-completion files for RHEL
%if !0%{?rhel}
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  shell-completion/bash/stratis
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  shell-completion/zsh/_stratis
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d \
  shell-completion/fish/stratis.fish
%endif
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man8 docs/stratis.8

%files
%license LICENSE
%doc README.rst
%{_bindir}/stratis
%{_mandir}/man8/stratis.8*
%if !0%{?rhel}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/stratis
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_stratis
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/stratis.fish
%endif
%{python3_sitelib}/stratis_cli/
%{python3_sitelib}/stratis_cli-*.egg-info/

%changelog
* Mon Jan 09 2023 Bryan Gurney <bgurney@redhat.com> - 3.4.1-1
- send_uevent: remove strict parameter
- Resolves: rhbz#2158914

* Wed Nov 23 2022 Bryan Gurney <bgurney@redhat.com> - 3.4.0-1
- Update to version 3.4.0
- Resolves: rhbz#2124977
- Return no-op on overprovision command on error
- Resolves: rhbz#2131934
- Return error on init-cache if cache is present
- Resolves: rhbz#2141223

* Fri Jul 08 2022 Bryan Gurney <bgurney@redhat.com> - 3.2.0-1
- Add the ability to stop and start pools
- Resolves: rhbz#2105061

* Tue May 31 2022 Bryan Gurney <bgurney@redhat.com> - 3.1.0-1
- Update to 3.1.0
- Resolves: rhbz#2039946
- Revise stratis-cli.spec file to unified format

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 2.4.3-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jul 19 2021 Bryan Gurney <bgurney@redhat.com> - 2.4.3-1
- Remove psutil dependency from setup.py
- Resolves: rhbz#1983689

* Mon Jun 28 2021 Bryan Gurney <bgurney@redhat.com> - 2.4.2-3
- Remove semantic_version and wcwidth dependencies from setup.py
- Resolves: rhbz#1976731

* Thu Jun 17 2021 Bryan Gurney <bgurney@redhat.com> - 2.4.2-2
- Remove unnecessary keyutils Requires line
- Resolves: rhbz#1914316

* Thu Jun 17 2021 Bryan Gurney <bgurney@redhat.com> - 2.4.2-1
- Update to 2.4.2
- Resolves: rhbz#1914316
- Remove requirement for python3-semantic_version
- Resolves: rhbz#1972353

* Fri Jun 11 2021 Bryan Gurney <bgurney@redhat.com> - 2.4.1-1
- Update to 2.4.1
- Resolves: rhbz#1914316

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.3.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 mulhern <amulhern@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Tue Nov 10 2020 mulhern <amulhern@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 mulhern <amulhern@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Thu Jul 9 2020 mulhern <amulhern@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.9

* Wed Feb 19 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sat Sep 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Sat Nov 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-3
- Make package archful

* Thu Sep 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-2
- Bump stratisd req

* Thu Sep 27 2018 Andy Grover <agrover@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Fri Aug 31 2018 Andy Grover <agrover@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Fri Aug 3 2018 Andy Grover <agrover@redhat.com> - 0.5.5-3
- Remove zsh completions subpackage
- Own completion directories

* Thu Aug 2 2018 Andy Grover <agrover@redhat.com> - 0.5.5-1
- Update to 0.5.5
- Add zsh completions subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-2
- Rebuilt for Python 3.7

* Mon Jun 4 2018 Andy Grover <agrover@redhat.com> - 0.5.3-1
- Update to 0.5.3

* Tue May 1 2018 Andy Grover <agrover@redhat.com> - 0.5.2-1
- Update to 0.5.2

* Wed Apr 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-3
- Fix dependency on stratisd

* Tue Apr 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Relax stratisd dependency

* Thu Mar 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.5-3
- Enable usage of dependency generator

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.5-2
- Include manpage

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.5-1
- Initial package
