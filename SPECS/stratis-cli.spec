Name:           stratis-cli
Version:        2.4.2
Release:        1%{?dist}
Summary:        Command-line tool for interacting with the Stratis daemon

License:        ASL 2.0
URL:            https://github.com/stratis-storage/stratis-cli
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{_bindir}/a2x

Requires:       platform-python
Requires:       python3-dateutil
Requires:       python3-psutil
Requires:       python3-dbus-client-gen >= 0.4
Requires:       python3-dbus-python-client-gen >= 0.7
Requires:       python3-justbytes >= 0.14

# It runs without, but totally useless
Requires:       stratisd >= 2.4

# stratisd only available on certain arches
ExclusiveArch:  %{rust_arches} noarch
ExcludeArch:    i686
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
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  shell-completion/bash/stratis
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  shell-completion/zsh/_stratis
%{__install} -Dpm0644 -t %{buildroot}%{_mandir}/man8 docs/stratis.8

%files
%license LICENSE
%doc README.rst
%{_bindir}/stratis
%{_mandir}/man8/stratis.8*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/stratis
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_stratis
%{python3_sitelib}/stratis_cli/
%{python3_sitelib}/stratis_cli-*.egg-info/

%changelog
* Wed Jun 16 2021  Bryan Gurney <bgurney@redhat.com> - 2.4.2-1
- Update to 2.4.2
- Resolves: rhbz#1931670
- Remove requirement for python3-semantic_version
- Resolves: rhbz#1972355
- Remove unnecessary keyutils Requires line

* Thu Jun 03 2021  Bryan Gurney <bgurney@redhat.com> - 2.4.1-1
- Update to 2.4.1
- Resolves: rhbz#1931670

* Fri May 07 2021  Bryan Gurney <bgurney@redhat.com> - 2.4.0-3
- Update to 2.4.0
- Resolves: rhbz#1931670

* Mon Jan 11 2021  Dennis Keefe <dkeefe@redhat.com> - 2.3.0-3
- Update to 2.3.0
- Resolves: rhbz#1885329
 
* Mon Jul 13 2020  Dennis Keefe <dkeefe@redhat.com> - 2.1.1-6
- Update to 2.1.1
- Resolves: rhbz#1791472
- Update RPM spec file
- Resolves: rhbz#1827360
- Error messages when creating a pool are more helpful
- Resolves: rhbz#1734496
- Support per-pool encryption of devices that form a pools data tier
- Resolves: rhbz#1768580
- Improve error handling on partial unlock failure of encrypted pools
- Resolves: rhbz#1855520
 
* Sun Nov 10 2019  Dennis Keefe <dkeefe@redhat.com> - 2.0.0-2
- Update to 2.0.0
- Allow the user to interact with the daemon under conditions
  where a pool, filesystem, or blockdev is not fully functional.
- Resolves: rhbz#1730493
- Establish an environment variable for D-Bus timeout parameter.
- Resolves: rhbz#1678631
- Return detailed error messages on all error-appearing user actions.
- Resolves: rhbz#1642393
- Resolves: rhbz#1687869
- Exit with error code 0 and error message on stderr for all command-line
  parsing errors.
- Resolves: rhbz#1747564
- Show more complete error messages on D-Bus method call failures.
- Resolves: rhbz#1717460
- Add version numbers to required packages
- Resolves: rhbz#1717489
 
* Mon Jun 3 2019 Dennis Keefe <dkeefe@redhat.com> - 1.0.4-2
- Update to 1.0.4

* Tue Dec 11 2018 Andy Grover <agrover@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Wed Nov 7 2018 Andy Grover <agrover@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Wed Oct 3 2018 Andy Grover <agrover@redhat.com> - 1.0.0-2
- Bump stratisd req

* Tue Oct 2 2018 Andy Grover <agrover@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Fri Aug 3 2018 Andy Grover <agrover@redhat.com> - 0.5.5-2
- Remove zsh completion package and own completion dirs as needed

* Thu Aug 2 2018 Andy Grover <agrover@redhat.com> - 0.5.5-1
- Update to 0.5.5
- Add zsh completion subpackage
