# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-zc.lockfile
Epoch: 100
Version: 2.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Basic inter-process locks
License: ZPL-2.1
URL: https://github.com/zopefoundation/zc.lockfile/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to
lock files, but to simply provide locks with an implementation based on
file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation
uses file locks to mediate access to file-storage database files. The
database files and lock file files are separate files.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-zc.lockfile
Summary: Basic inter-process locks
Requires: python3
Provides: python3-zc.lockfile = %{epoch}:%{version}-%{release}
Provides: python3dist(zc.lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-zc.lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(zc.lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-zc.lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(zc.lockfile) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-zc.lockfile
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to
lock files, but to simply provide locks with an implementation based on
file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation
uses file locks to mediate access to file-storage database files. The
database files and lock file files are separate files.

%files -n python%{python3_version_nodots}-zc.lockfile
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-zc.lockfile
Summary: Basic inter-process locks
Requires: python3
Provides: python3-zc.lockfile = %{epoch}:%{version}-%{release}
Provides: python3dist(zc.lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-zc.lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(zc.lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-zc.lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(zc.lockfile) = %{epoch}:%{version}-%{release}

%description -n python3-zc.lockfile
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to
lock files, but to simply provide locks with an implementation based on
file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation
uses file locks to mediate access to file-storage database files. The
database files and lock file files are separate files.

%files -n python3-zc.lockfile
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-zc-lockfile
Summary: Basic inter-process locks
Requires: python3
Provides: python3-zc-lockfile = %{epoch}:%{version}-%{release}
Provides: python3dist(zc.lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-zc.lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(zc.lockfile) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-zc.lockfile = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(zc.lockfile) = %{epoch}:%{version}-%{release}

%description -n python3-zc-lockfile
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically to
lock files, but to simply provide locks with an implementation based on
file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation
uses file locks to mediate access to file-storage database files. The
database files and lock file files are separate files.

%files -n python3-zc-lockfile
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
